"""Build three illustration states for the CLAUDE.md writing slide.

The prompt illustration is a preview only. The deck renders the prompt itself as
selectable HTML text so the classroom can copy the user's original wording.
"""

from pathlib import Path
from unicodedata import east_asian_width
from xml.sax.saxutils import escape


HERE = Path(__file__).parent

PROMPT = """交付目标：使用 C 语言实现精简版 myls，支持默认目录列表以及 -a、-l、-h、-t 四个选项，无第三方运行时依赖。
运行环境为 Linux，使用 GCC 或 Clang 和 POSIX 目录接口。
默认每行输出一个文件名，不实现多列布局、颜色、递归和多个路径参数。
只接收零个或一个路径参数，默认路径为当前目录。
-h 必须与 -l 同用，否则报参数错误；非法选项和非法参数必须返回非零退出码。
输出字段、排序规则、时间格式和错误行为以验收契约为准。
系统 ls 只作为部分语义的参考实现，不把所有平台相关输出直接做字节级比较。

开发原则：按已澄清的需求做最小实现，不自行扩展；一次只实现当前指派的一个任务；严格 TDD：Red → Green → Review；
构建与测试： make all：构建 myls、make test：构建并运行测试、make clean：清理构建产物"""


def base(body: str, title: str, description: str, *, subtitle: str = "") -> str:
    subtitle_markup = (
        f'<text x="119" y="260" class="sans" fill="#b8cadb" font-size="28">{escape(subtitle)}</text>'
        if subtitle else ""
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" role="img" aria-labelledby="writing-title writing-desc">
  <title id="writing-title">{escape(title)}</title>
  <desc id="writing-desc">{escape(description)}</desc>
  <defs>
    <radialGradient id="writing-bg" cx="80%" cy="25%" r="85%">
      <stop offset="0" stop-color="#17465e" stop-opacity=".45"/>
      <stop offset=".58" stop-color="#0b2940" stop-opacity=".19"/>
      <stop offset="1" stop-color="#071423" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="writing-panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#12344b"/>
      <stop offset="1" stop-color="#0a2033"/>
    </linearGradient>
    <filter id="writing-shadow" x="-15%" y="-18%" width="130%" height="145%">
      <feDropShadow dx="0" dy="20" stdDeviation="24" flood-color="#000" flood-opacity=".27"/>
    </filter>
    <filter id="writing-glow" x="-70%" y="-70%" width="240%" height="240%">
      <feGaussianBlur stdDeviation="22"/>
    </filter>
    <style><![CDATA[
      .sans{{font-family:'PingFang SC','Microsoft YaHei','Noto Sans SC',Arial,sans-serif}}
      .mono{{font-family:'JetBrains Mono','SFMono-Regular',Menlo,monospace}}
    ]]></style>
  </defs>
  <rect width="1920" height="1080" fill="#071423"/>
  <rect width="1920" height="1080" fill="url(#writing-bg)"/>
  <circle cx="1530" cy="590" r="532" fill="none" stroke="#72d2ff" stroke-opacity=".055" stroke-width="2"/>
  <circle cx="1530" cy="590" r="375" fill="none" stroke="#72d2ff" stroke-opacity=".07" stroke-width="2"/>
  <text x="116" y="105" class="sans" fill="#72d2ff" font-size="25" font-weight="700" letter-spacing="3">实践 05 · 写项目指令</text>
  <rect x="116" y="128" width="107" height="5" rx="2.5" fill="#ffc17b"/>
  <text x="116" y="204" class="sans" fill="#f5f8fc" font-size="71" font-weight="760" letter-spacing="-1.5">CLAUDE.md，该怎么写？</text>
  {subtitle_markup}
  {body}
  <text x="116" y="1005" class="sans" fill="#88a1b8" font-size="21">AI 编码训练营 · 实践篇</text>
</svg>
'''


question = '''
  <g filter="url(#writing-shadow)">
    <rect x="506" y="312" width="908" height="489" rx="31" fill="url(#writing-panel)" stroke="#456c82" stroke-width="2"/>
  </g>
  <rect x="545" y="354" width="830" height="383" rx="25" fill="#092033" stroke="#244a60" stroke-width="1.7" stroke-dasharray="8 13"/>
  <circle cx="960" cy="553" r="197" fill="#72d2ff" opacity=".105" filter="url(#writing-glow)"/>
  <path d="M836 394h214l61 61v248a16 16 0 0 1-16 16H836a16 16 0 0 1-16-16V410a16 16 0 0 1 16-16Z" fill="#17394f" stroke="#72d2ff" stroke-width="3"/>
  <path d="M1050 394v57a10 10 0 0 0 10 10h51" fill="#27546b" stroke="#72d2ff" stroke-width="3"/>
  <rect x="851" y="424" width="170" height="35" rx="10" fill="#0d293e" stroke="#48829a" stroke-width="1.3"/>
  <text x="937" y="448" class="mono" fill="#a7e6ff" font-size="20" font-weight="680" text-anchor="middle">CLAUDE.md</text>
  <path d="M854 605h214M854 633h167M854 661h194" stroke="#56869c" stroke-width="7" stroke-linecap="round" opacity=".6"/>
  <circle cx="962" cy="544" r="52" fill="#244b5e" stroke="#ffc17b" stroke-width="2.5"/>
  <text x="962" y="565" class="sans" fill="#ffc17b" font-size="61" font-weight="760" text-anchor="middle">?</text>
  <path d="M722 480c-37 4-63 28-65 65M1209 465c32 7 52 32 54 61" fill="none" stroke="#72d2ff" stroke-width="3" stroke-opacity=".54" stroke-linecap="round"/>
  <circle cx="670" cy="545" r="8" fill="#72d2ff"/>
  <circle cx="1259" cy="535" r="8" fill="#ffc17b"/>
  <text x="960" y="774" class="sans" fill="#d8ebf5" font-size="24" text-anchor="middle">先想清楚：由谁写第一稿，怎样把它改到适合项目？</text>
'''


methods = '''
  <g filter="url(#writing-shadow)">
    <rect x="116" y="307" width="813" height="600" rx="26" fill="url(#writing-panel)" stroke="#4b7588" stroke-width="2"/>
    <rect x="958" y="307" width="846" height="600" rx="26" fill="url(#writing-panel)" stroke="#8c7459" stroke-width="2"/>
  </g>

  <rect x="146" y="338" width="68" height="46" rx="13" fill="#173f53" stroke="#72d2ff" stroke-opacity=".45"/>
  <text x="180" y="369" class="mono" fill="#72d2ff" font-size="24" font-weight="760" text-anchor="middle">01</text>
  <text x="232" y="372" class="sans" fill="#f5f8fc" font-size="35" font-weight="730">直接手写 Markdown</text>
  <path d="M150 406H895" stroke="#4a6e82" stroke-width="1.4"/>

  <g>
    <rect x="159" y="447" width="305" height="327" rx="20" fill="#0a2235" stroke="#6096a9" stroke-width="1.8"/>
    <path d="M179 468h222l43 43v238a10 10 0 0 1-10 10H179a10 10 0 0 1-10-10V478a10 10 0 0 1 10-10Z" fill="#183c51" stroke="#72d2ff" stroke-opacity=".48" stroke-width="1.6"/>
    <path d="M401 469v36a9 9 0 0 0 9 9h34" fill="#28546b" stroke="#72d2ff" stroke-opacity=".55" stroke-width="1.6"/>
    <text x="195" y="547" class="mono" fill="#aee7ff" font-size="26" font-weight="700"># CLAUDE.md</text>
    <path d="M195 587h197M195 615h168M195 643h190M195 671h144M195 699h171" stroke="#6a9eb2" stroke-opacity=".7" stroke-width="7" stroke-linecap="round"/>
    <rect x="194" y="719" width="122" height="26" rx="8" fill="#1d5060"/>
    <text x="255" y="738" class="mono" fill="#aee7ff" font-size="17" text-anchor="middle">.md</text>
  </g>
  <text x="504" y="468" class="sans" fill="#ffc17b" font-size="24" font-weight="700">适合已经熟悉：</text>
  <circle cx="514" cy="522" r="8" fill="#72d2ff"/>
  <text x="538" y="531" class="sans" fill="#f5f8fc" font-size="27">项目目标与约束</text>
  <circle cx="514" cy="590" r="8" fill="#72d2ff"/>
  <text x="538" y="599" class="sans" fill="#f5f8fc" font-size="27">Markdown 语法</text>
  <circle cx="514" cy="658" r="8" fill="#72d2ff"/>
  <text x="538" y="667" class="sans" fill="#f5f8fc" font-size="27">CLAUDE.md 写入规则</text>
  <path d="M505 714h342" stroke="#486b80" stroke-width="1.4"/>
  <text x="506" y="760" class="sans" fill="#a6c8d8" font-size="23">创建文件 → 手写内容 → 自行维护</text>

  <rect x="990" y="338" width="68" height="46" rx="13" fill="#3b382f" stroke="#ffc17b" stroke-opacity=".5"/>
  <text x="1024" y="369" class="mono" fill="#ffc17b" font-size="24" font-weight="760" text-anchor="middle">02</text>
  <text x="1076" y="372" class="sans" fill="#f5f8fc" font-size="35" font-weight="730">/init 起草，人工迭代</text>
  <path d="M992 406H1769" stroke="#6c685e" stroke-width="1.4"/>
  <rect x="1004" y="437" width="754" height="127" rx="18" fill="#061a2b" stroke="#647885" stroke-width="1.6"/>
  <path d="M1029 467h10" stroke="#72d2ff" stroke-width="3" stroke-linecap="round"/>
  <text x="1053" y="475" class="mono" fill="#b8e8ff" font-size="26" font-weight="680">/init</text>
  <text x="1138" y="475" class="sans" fill="#adc7d6" font-size="21">先生成项目指令初稿</text>
  <path d="M1031 508h692" stroke="#29495c" stroke-width="1.2"/>
  <text x="1031" y="545" class="sans" fill="#ffc17b" font-size="23" font-weight="650">再给出提示词，让 AI 按目标起草和修订</text>

  <g>
    <rect x="1004" y="617" width="174" height="103" rx="15" fill="#1b4152" stroke="#72d2ff" stroke-opacity=".47"/>
    <circle cx="1032" cy="643" r="7" fill="#72d2ff"/>
    <text x="1048" y="650" class="mono" fill="#9fe1ff" font-size="18" font-weight="700">01</text>
    <text x="1020" y="686" class="sans" fill="#f5f8fc" font-size="23" font-weight="650">描述需求</text>
    <path d="M1184 667h24m-8-7 8 7-8 7" fill="none" stroke="#7fa9bd" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>

    <rect x="1214" y="617" width="174" height="103" rx="15" fill="#1b4152" stroke="#72d2ff" stroke-opacity=".47"/>
    <circle cx="1242" cy="643" r="7" fill="#72d2ff"/>
    <text x="1258" y="650" class="mono" fill="#9fe1ff" font-size="18" font-weight="700">02</text>
    <text x="1230" y="686" class="sans" fill="#f5f8fc" font-size="23" font-weight="650">AI 起草</text>
    <path d="M1394 667h24m-8-7 8 7-8 7" fill="none" stroke="#7fa9bd" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>

    <rect x="1424" y="617" width="174" height="103" rx="15" fill="#3b3940" stroke="#ffc17b" stroke-opacity=".57"/>
    <circle cx="1452" cy="643" r="7" fill="#ffc17b"/>
    <text x="1468" y="650" class="mono" fill="#ffd39e" font-size="18" font-weight="700">03</text>
    <text x="1440" y="686" class="sans" fill="#f5f8fc" font-size="23" font-weight="650">人工增删改</text>
    <path d="M1604 667h24m-8-7 8 7-8 7" fill="none" stroke="#7fa9bd" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>

    <rect x="1634" y="617" width="124" height="103" rx="15" fill="#1b4152" stroke="#72d2ff" stroke-opacity=".47"/>
    <circle cx="1659" cy="643" r="7" fill="#72d2ff"/>
    <text x="1675" y="650" class="mono" fill="#9fe1ff" font-size="18" font-weight="700">04</text>
    <text x="1650" y="685" class="sans" fill="#f5f8fc" font-size="22" font-weight="650">AI 优化</text>
  </g>
  <path d="M1696 730v28q0 12-12 12h-485q-12 0-12-12v-28m-8 9 8-9 8 9" fill="none" stroke="#8daebc" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="1326" y="756" width="231" height="29" rx="13" fill="#132f43"/>
  <text x="1441" y="777" class="sans" text-anchor="middle" fill="#b6ceda" font-size="19">循环到内容符合项目实际</text>
'''


def visual_lines(text: str, max_units: int = 111) -> list[str]:
    """Wrap the preview, keeping the original prompt in PROMPT untouched."""
    lines: list[str] = []
    for source_line in text.split("\n"):
        if not source_line:
            lines.append("")
            continue
        current = ""
        units = 0
        for char in source_line:
            size = 2 if east_asian_width(char) in "FW" else 1
            if current and units + size > max_units:
                lines.append(current)
                current = ""
                units = 0
            current += char
            units += size
        if current:
            lines.append(current)
    return lines


wrapped = visual_lines(PROMPT)
prompt_lines = []
for index, line in enumerate(wrapped):
    y = 350 + index * 38
    prompt_lines.append(
        f'<text x="165" y="{y}" class="sans" fill="#e4eff7" font-size="25">{escape(line)}</text>'
    )

prompt_preview = f'''
  <g filter="url(#writing-shadow)">
    <rect x="116" y="228" width="1688" height="699" rx="26" fill="url(#writing-panel)" stroke="#557b8e" stroke-width="2"/>
  </g>
  <path d="M116 312H1804" stroke="#51768a" stroke-width="1.5"/>
  <rect x="158" y="253" width="43" height="43" rx="11" fill="#173f53" stroke="#72d2ff" stroke-opacity=".45"/>
  <path d="M171 266h17M171 274h13M171 282h16" stroke="#a6e5ff" stroke-width="2.3" stroke-linecap="round"/>
  <text x="219" y="283" class="sans" fill="#f5f8fc" font-size="30" font-weight="710">给 Claude 的示例提示词</text>
  <text x="164" y="{350 + len(wrapped) * 38 + 12}" class="sans" fill="#88a9bb" font-size="19">提示词仅提供初稿材料；生成后仍需按真实项目和验收契约逐条检查。</text>
  {''.join(prompt_lines)}
'''


(HERE / "claude-writing-question.svg").write_text(
    base(
        question,
        "CLAUDE.md，该怎么写？",
        "以空白 CLAUDE.md 文档和问号开场，提示接下来展示两种编写项目指令的方法。",
        subtitle="给 Agent 的项目约定，第一稿从哪里来？",
    ),
    encoding="utf-8",
)
(HERE / "claude-writing-methods.svg").write_text(
    base(
        methods,
        "CLAUDE.md 的两种写法",
        "方法一是熟悉项目、Markdown 和项目指令规则后手写。方法二是在 Claude Code 中先运行 /init，再提供目标与约束，让 AI 起草，并由人增删改、交回 AI 优化，循环迭代。",
        subtitle="两条路径都要由人审核，让内容贴合真实项目。",
    ),
    encoding="utf-8",
)
(HERE / "claude-writing-prompt-preview.svg").write_text(
    base(
        prompt_preview,
        "可复制的示例提示词预览",
        "完整示例提示词的静态预览；实际幻灯片使用可选中、可复制的 HTML 文本呈现，右上角预留复制与返回按钮。",
    ),
    encoding="utf-8",
)

print(f"Wrote three SVG states. Prompt preview uses {len(wrapped)} visual lines; last baseline {350 + (len(wrapped)-1)*38}.")
