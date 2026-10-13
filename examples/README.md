# 最小 Agent 演示

运行环境：Python 3.10+，仅使用标准库。此文件与 `myls` 的 C 实现、测试互不依赖。

```sh
export DEEPSEEK_API_KEY='你的 API Key'
python3 examples/minimal_agent.py
```

程序首轮要求模型调用 `count_outline_lines`；Python 读取 `Outline.md` 并返回行数；模型收到工具结果后再次判断，最后向用户输出答案。代码中的 `for` 循环就是流程图的反馈循环，`if not calls` 是输出分支。最多请求模型 5 次，防止演示时意外反复调用。

API 格式参考 [DeepSeek Tool Calls](https://api-docs.deepseek.com/guides/tool_calls/) 与 [Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion/)。这里关闭思考模式，使工具调用的上下文结构保持简短。
