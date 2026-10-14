# CLI 测试写法

`make test` 目前会编译程序，并依次用 `sh` 执行 `tests/cases/*.sh`。每个用例通过环境变量 `MYLS_BIN` 获得可执行文件的绝对路径。脚本用非零退出码表示失败。基线尚无行为测试；按 `Outline.md` 5.1 添加 C 单元测试时，应将其编译和运行也接入 `make test`。

本目录的 shell 脚本既是 CLI 集成测试，也可通过临时目录、空目录和含空格名称等夹具覆盖文件系统场景；“文件系统场景测试”不要求另一套框架。C 单元测试直接调用可独立验证的小函数，不代替对真实 `myls` 输出的断言。

以下是**普通模式阶段**可用的示例；不要在讲师带做的路径阶段照搬排序断言。保存为 `tests/cases/plain.sh` 后，先运行 `make test` 看它因功能缺失变红，再实现对应行为。

```sh
#!/bin/sh
set -eu

work=$(mktemp -d)
trap 'rm -rf "$work"' 0 HUP INT TERM
mkdir "$work/input"
: > "$work/input/b"
: > "$work/input/a"

status=0
"$MYLS_BIN" "$work/input" > "$work/stdout" 2> "$work/stderr" || status=$?
printf 'a\nb\n' > "$work/expected"

[ "$status" -eq 0 ] || { printf 'unexpected exit: %s\n' "$status" >&2; exit 1; }
cmp "$work/expected" "$work/stdout" || exit 1
[ ! -s "$work/stderr" ] || { cat "$work/stderr" >&2; exit 1; }
```

写用例时先确定本轮任务卡：输入参数、目录状态、预期 stdout、预期 stderr、预期退出码。`stderr` 内容由系统错误文案决定时，只检查 `myls:` 前缀和“一行”，不逐字比较。含空格的路径和名称都要正确加引号。测试夹具应在临时目录中创建，并在退出时清理。
