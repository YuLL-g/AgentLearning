"""不访问网络的 Agent 循环与工具边界测试。"""

import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import minimal_agent as agent


def call(name, **arguments):
    return {"id": "call_1", "function": {
        "name": name, "arguments": json.dumps(arguments),
    }}


class MinimalAgentTests(unittest.TestCase):
    def test_last_five_user_turns_are_remembered(self):
        requests = []

        def fake_model(messages, _api_key):
            requests.append(messages)
            return {"role": "assistant", "content": "收到"}

        answers = [f"问题{i}" for i in range(1, 7)] + ["退出"]
        with patch.dict(os.environ, {"DEEPSEEK_API_KEY": "test-only"}), \
             patch("builtins.input", side_effect=answers), \
             patch.object(agent, "ask_model", side_effect=fake_model), \
             contextlib.redirect_stdout(io.StringIO()):
            agent.main()

        self.assertEqual(len(requests), 6)
        self.assertEqual([m["content"] for m in requests[-1] if m["role"] == "user"],
                         answers[1:6])

    def test_tool_result_returns_to_model_before_output(self):
        replies = iter([
            {"role": "assistant", "content": None,
             "tool_calls": [call("count_outline_lines")]},
            {"role": "assistant", "content": "已完成"},
        ])
        requests = []

        def fake_model(messages, _api_key):
            requests.append(messages)
            return next(replies)

        output = io.StringIO()
        prompts = []
        answers = iter(["统计行数", "退出"])

        def fake_input(prompt):
            prompts.append(prompt)
            return next(answers)

        with patch.dict(os.environ, {"DEEPSEEK_API_KEY": "test-only"}), \
             patch("builtins.input", side_effect=fake_input), \
             patch.object(agent, "ask_model", side_effect=fake_model), \
             contextlib.redirect_stdout(output):
            agent.main()

        self.assertEqual(requests[1][-1]["role"], "tool")
        self.assertEqual(requests[1][-1]["content"],
                         str(len((agent.ROOT / "Outline.md").read_text(encoding="utf-8").splitlines())))
        self.assertIn("[输入]", prompts[0])
        for stage in ("[模型判断]", "[工具请求]", "[工具执行]",
                      "[观察结果]", "[上下文更新]", "[输出]"):
            self.assertIn(stage, output.getvalue())

    def test_file_and_command_boundaries(self):
        with tempfile.TemporaryDirectory(dir=agent.ROOT) as directory:
            relative = Path(directory).relative_to(agent.ROOT)
            text_path = str(relative / "note.txt")
            program_path = Path(directory) / "demo.sh"
            program_path.write_text("#!/bin/sh\nprintf ok", encoding="utf-8")
            program_path.chmod(0o700)

            with patch.object(agent, "confirm", return_value=False):
                self.assertIn("拒绝", agent.execute_tool(call(
                    "write_file", path=text_path, content="hello")))
            self.assertFalse((Path(directory) / "note.txt").exists())

            with patch.object(agent, "confirm", return_value=True), \
                 patch.dict(os.environ, {"DEEPSEEK_API_KEY": "test-only"}):
                self.assertIn("已写入", agent.execute_tool(call(
                    "write_file", path=text_path, content="hello")))
                self.assertEqual(agent.execute_tool(call("read_file", path=text_path)), "hello")
                self.assertIn("stdout:\nok", agent.execute_tool(call(
                    "run_program", program=str(relative / "demo.sh"), args=[])))
                self.assertIn("stdout:\nunset", agent.execute_tool(call(
                    "run_shell", command='printf "${DEEPSEEK_API_KEY-unset}"')))

        self.assertIn("工具错误", agent.execute_tool(call("read_file", path="../outside")))
        self.assertIn("工具错误", agent.execute_tool(call("read_file", path=".git/config")))


if __name__ == "__main__":
    unittest.main()
