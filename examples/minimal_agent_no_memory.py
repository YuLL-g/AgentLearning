"""无记忆最小 Agent：与 minimal_agent.py 功能一致，但移除了跨轮次的上下文记忆。
每一轮用户输入都从空白上下文开始，不携带上一轮的输入、模型回复和工具结果，
用于和 minimal_agent.py 对比说明 Agent 的上下文能力。
单轮内的工具循环（回复 + 工具结果）仍保留在上下文中，多步工具调用不受影响。
"""
import json
import os
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
API_URL = "https://api.deepseek.com/chat/completions"
MAX_TOOL_TEXT = 10_000

def tool(name, description, properties, required=()):
    return {"type": "function", "function": {
        "name": name, "description": description,
        "parameters": {"type": "object", "properties": properties,
                       "required": list(required), "additionalProperties": False},
    }}

TEXT = {"type": "string"}
TOOLS = [
    tool("read_file", "读取仓库内的 UTF-8 文本文件", {"path": TEXT}, ("path",)),
    tool("write_file", "写入仓库内的 UTF-8 文本文件，需用户确认",
         {"path": TEXT, "content": TEXT}, ("path", "content")),
    tool("run_program", "直接运行仓库内的可执行文件，不经过 shell，需用户确认",
         {"program": TEXT, "args": {"type": "array", "items": TEXT}}, ("program",)),
    tool("run_shell", "在仓库目录执行 shell 命令，需用户确认",
         {"command": TEXT}, ("command",)),
]

def ask_model(messages, api_key):
    body = {"model": "deepseek-flash", "messages": messages, "tools": TOOLS,
            "thinking": {"type": "disabled"}}
    request = Request(
        API_URL, data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)["choices"][0]["message"]

def local_path(name):
    if not isinstance(name, str) or Path(name).is_absolute():
        raise ValueError("路径必须是仓库内的相对路径")
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT) or path.is_relative_to(ROOT / ".git"):
        raise ValueError("路径超出允许范围")
    return path

def confirm(action):
    return input(f"[确认] 允许{action}？[y/N] ").strip().lower() in ("y", "yes")

def run_command(argv):
    environment = os.environ.copy()
    environment.pop("DEEPSEEK_API_KEY", None)
    done = subprocess.run(argv, cwd=ROOT, env=environment, capture_output=True,
                          text=True, encoding="utf-8", errors="replace", timeout=15)
    return (f"exit_code={done.returncode}\nstdout:\n{done.stdout}"
            f"stderr:\n{done.stderr}")[:MAX_TOOL_TEXT]

def execute_tool(call):
    try:
        name = call["function"]["name"]
        args = json.loads(call["function"]["arguments"])
        if not isinstance(args, dict):
            raise ValueError("工具参数必须是 JSON 对象")
        if name == "read_file":
            path = local_path(args["path"])
            with path.open(encoding="utf-8") as file:
                content = file.read(MAX_TOOL_TEXT + 1)
            return content[:MAX_TOOL_TEXT] + ("\n[内容已截断]" if len(content) > MAX_TOOL_TEXT else "")
        if name == "write_file":
            path, content = local_path(args["path"]), args["content"]
            if not isinstance(content, str) or len(content) > MAX_TOOL_TEXT:
                raise ValueError("写入内容必须是 10000 字以内的文本")
            if not confirm(f"写入 {path.relative_to(ROOT)}，内容预览 {content[:80]!r}"):
                return "用户拒绝写入"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            return f"已写入 {path.relative_to(ROOT)}"
        if name == "run_program":
            path, argv = local_path(args["program"]), args.get("args", [])
            if not isinstance(argv, list) or not all(isinstance(x, str) for x in argv):
                raise ValueError("args 必须是字符串数组")
            if not confirm(f"直接运行 {path.relative_to(ROOT)} {argv}"):
                return "用户拒绝执行程序"
            return run_command([str(path), *argv])
        if name == "run_shell":
            command = args["command"]
            if not isinstance(command, str) or not command.strip():
                raise ValueError("command 必须是非空字符串")
            if not confirm(f"执行 shell 命令：{command!r}"):
                return "用户拒绝执行 shell 命令"
            return run_command(["/bin/sh", "-c", command])
        raise ValueError(f"未开放的工具：{name}")
    except (KeyError, TypeError, ValueError, OSError, subprocess.TimeoutExpired) as error:
        return f"工具错误：{error}"

def main():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise SystemExit("请先设置 DEEPSEEK_API_KEY 环境变量")
    while True:  # 无记忆：不再维护 turns，每轮独立
        try:
            user_text = input("[输入] 你 > ").strip()
        except EOFError:
            break
        if user_text.lower() in ("exit", "quit", "退出"):
            break
        if not user_text:
            continue
        current = [{"role": "user", "content": user_text}]
        # print("[记忆] 无记忆模式：本轮不携带任何历史输入")
        for _ in range(5):  # 单轮最多 5 次模型判断，避免无限调用
            messages = list(current)  # 上下文只有本轮消息
            print("[模型判断] 正在请求 DeepSeek...")
            reply = ask_model(messages, api_key)
            current.append(reply)
            calls = reply.get("tool_calls") or []
            if not calls:
                print("[输出]", reply.get("content") or "（空答复）")
                break
            for call in calls:
                name = call["function"]["name"]
                print(f"[工具请求] {name}")
                result = execute_tool(call)
                print(f"[工具执行] {name} 请求已处理")
                print("[观察结果]", repr(result[:200]))
                current.append({"role": "tool", "tool_call_id": call["id"], "content": result})
                print("[上下文更新] 工具结果已加入消息")
        else:
            print("[输出] 已达到单轮 5 次模型判断上限")

if __name__ == "__main__":
    main()
