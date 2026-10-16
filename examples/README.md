# 交互式最小 Agent 演示

运行环境：Python 3.10+，仅使用标准库。本示例独立于课程中的 `myls` 练习项目。

```sh
export DEEPSEEK_API_KEY='你的 API Key'
python3 examples/minimal_agent.py
```

离线检查（不调用 API）：`python3 -m unittest discover -s examples -p 'test_*.py'`。

在 `你 >` 后连续输入问题；输入 `退出`、`exit` 或 `quit` 结束。可先问“请用 read_file 工具读取 README.md 并概括仓库用途”，再问“刚才的仓库用途是什么？”来展示记忆。程序保留最近 **5 轮用户输入**，每轮连同模型回复和工具结果一起保存；关闭程序后记忆清空。单轮最多进行 5 次模型判断。

| 工具 | 作用 |
| --- | --- |
| `read_file` | 读取仓库内的 UTF-8 文本文件 |
| `write_file` | 写入仓库内的 UTF-8 文本文件 |
| `run_program` | 直接运行仓库内的可执行文件，不经过 shell |
| `run_shell` | 在仓库目录通过 `/bin/sh` 执行命令 |

终端会显示“输入、模型判断、工具请求、工具执行、观察结果、上下文更新、输出”各阶段。写入、直接执行和 shell 执行前必须在本机输入 `y` 确认；默认拒绝。文件路径限于仓库内（排除 `.git`），命令执行超时为 15 秒，且不会继承 `DEEPSEEK_API_KEY`。shell 命令经用户确认后仍能访问当前用户有权访问的其他路径，因此课堂演示应看清命令再确认。

API 格式参考 [DeepSeek Tool Calls](https://api-docs.deepseek.com/guides/tool_calls/) 与 [Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion/)。示例关闭思考模式，减少需要维护的消息字段。
