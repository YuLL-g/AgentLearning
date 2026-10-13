# myls 教学仓库

本仓库用于练习把需求拆成可验证任务，并按 Red→Green→Review 用 AI 辅助开发一个精简版 `myls`。

- [Outline.md](Outline.md)：最终行为契约与课程大纲。
- [BrainStroming.md](BrainStroming.md)：讲师讲解和带做草稿。
- [AGENTS.md](AGENTS.md)：仓库内 AI 协作规则；Claude Code 另有 [CLAUDE.md](CLAUDE.md) 入口。
- `src/`：C 生产代码，目前仅有未实现占位程序。
- `include/`：后续需要的头文件。
- `tests/`：CLI 测试入口和用例说明。

在目标 Linux 环境准备 GCC 或 Clang、Make、Git 和 POSIX shell，然后执行：

```sh
make all
make test
make sanitize
make clean
```

基线 `make test` 只验证工程能构建，并提示尚无行为测试。第一轮实践先在 `tests/cases/` 加测试，确认它因功能缺失而失败，再实现最小功能。
