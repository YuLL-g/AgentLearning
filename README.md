# AI 编码课程资料库

本仓库用于分析编码 Agent 的工作方式、整理授课思路并制作课程材料。`myls` 是课程中讨论需求拆解和 TDD 的**练习案例**；本仓库不提供它的可构建实现。课堂若要实际开发 `myls`，应另备独立的练习仓库或环境。

## 从哪里开始

- [Outline.md](Outline.md)：课程目标及 `myls` 练习项目的行为契约。
- [BrainStroming.md](BrainStroming.md)：讲师讲解路线与带做草稿。
- [Opening_AI_History.md](Opening_AI_History.md)：开场内容。
- [Agent_Framework_Notes.md](Agent_Framework_Notes.md)：Agent 组成与运行流程。
- [AGENTS.md](AGENTS.md)：本资料仓库的 AI 协作规则；[CLAUDE.md](CLAUDE.md) 是 Claude Code 的入口。

## 资料目录

- [`output/`](output/)：整理后的讲义、流程图、动画和幻灯片。
- [`assets/`](assets/)：课程图片素材。
- [`examples/`](examples/)：演示 Agent 工具调用与循环的小型 Python 程序，运行方法见 [示例说明](examples/README.md)。

检查示例代码可运行：

```sh
python3 -m unittest discover -s examples -p 'test_*.py'
```

此命令不调用模型 API。`Outline.md` 中出现的 `make all`、`make test` 等命令属于拟开展的 `myls` 练习项目，不是本资料仓库的命令。
