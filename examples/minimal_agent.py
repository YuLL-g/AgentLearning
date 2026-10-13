"""最小 Agent：模型判断 → 工具执行 → 结果回传 → 再判断。"""

import json
import os
from pathlib import Path
from urllib.request import Request, urlopen


API_URL = "https://api.deepseek.com/chat/completions"
OUTLINE = Path(__file__).resolve().parents[1] / "Outline.md"
TOOLS = [{
    "type": "function",
    "function": {
        "name": "count_outline_lines",
        "description": "Count the lines in this repository's Outline.md file.",
        "parameters": {"type": "object", "properties": {}},
    },
}]


def ask_model(messages, api_key, require_tool):
    body = {
        "model": "deepseek-flash",
        "messages": messages,
        "tools": TOOLS,
        "tool_choice": "required" if require_tool else "auto",
        "thinking": {"type": "disabled"},
    }
    request = Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)["choices"][0]["message"]


def main():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise SystemExit("请先设置 DEEPSEEK_API_KEY 环境变量")

    messages = [{"role": "user", "content": "请调用工具，告诉我本仓库 Outline.md 有多少行。"}]
    for turn in range(5):
        reply = ask_model(messages, api_key, require_tool=(turn == 0))
        messages.append(reply)  # 把模型的工具调用或答复加入上下文
        calls = reply.get("tool_calls") or []
        if not calls:
            print("Agent 输出：", reply.get("content") or "（空答复）")
            return

        for call in calls:
            if call["function"]["name"] != "count_outline_lines":
                raise RuntimeError("模型请求了未开放的工具")
            if json.loads(call["function"]["arguments"]):
                raise RuntimeError("工具不接受参数")
            with OUTLINE.open(encoding="utf-8") as file:
                result = str(sum(1 for _ in file))
            print("工具执行：count_outline_lines →", result)
            messages.append({"role": "tool", "tool_call_id": call["id"], "content": result})

    raise SystemExit("达到最多 5 轮，停止循环")


if __name__ == "__main__":
    main()
