"""Build slide 19's static comparison illustration.

The three paths share the same project skeleton and task wording. Instructor
expectations stay out of this artwork and the common prompt; the HTML slide
reveals them separately on request.
"""

from pathlib import Path
from xml.sax.saxutils import escape


HERE = Path(__file__).parent
TASK = "开始需求开发，需求场景：无路径参数；行为：列出当前目录"


def text_lines(lines: list[str], x: int, first_y: int, *, size: int = 25, color: str = "#eaf3f8", step: int = 32) -> str:
    return "".join(
        f'<text x="{x}" y="{first_y + i * step}" class="sans" fill="{color}" font-size="{size}">{escape(line)}</text>'
        for i, line in enumerate(lines)
    )


def flow(x: int, labels: tuple[str, str, str], accent: str) -> str:
    widths = (122, 143, 155)
    gaps = (24, 24)
    starts = (x + 28, x + 28 + widths[0] + gaps[0], x + 28 + widths[0] + gaps[0] + widths[1] + gaps[1])
    cells = []
    for i, (start, width, label) in enumerate(zip(starts, widths, labels)):
        cells.append(
            f'<rect x="{start}" y="627" width="{width}" height="60" rx="13" fill="#0a2639" stroke="{accent}" stroke-opacity="{.64 if i == 0 else .38}" stroke-width="1.5"/>'
            f'<text x="{start + width / 2}" y="665" class="sans" fill="#eaf3f8" font-size="21" font-weight="650" text-anchor="middle">{escape(label)}</text>'
        )
        if i < 2:
            middle = start + width + 12
            cells.append(
                f'<path d="M{middle - 3} 656h16m-5-5 5 5-5 5" fill="none" stroke="#83aabd" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
            )
    return "".join(cells)


def card(
    x: int,
    number: str,
    title: str,
    tag: str,
    accent: str,
    icon: str,
    labels: tuple[str, str, str],
    summary: list[str],
    footer: str = "",
) -> str:
    return f'''
  <g filter="url(#card-shadow)">
    <rect x="{x}" y="518" width="530" height="374" rx="25" fill="url(#card-fill)" stroke="{accent}" stroke-opacity=".53" stroke-width="2"/>
  </g>
  <rect x="{x}" y="518" width="530" height="5" rx="2.5" fill="{accent}" opacity=".84"/>
  <rect x="{x + 29}" y="547" width="55" height="38" rx="10" fill="#17394e" stroke="{accent}" stroke-opacity=".7"/>
  <text x="{x + 56.5}" y="573" class="mono" fill="{accent}" font-size="20" font-weight="750" text-anchor="middle">{number}</text>
  <text x="{x + 101}" y="575" class="sans" fill="#f5f8fc" font-size="32" font-weight="740">{escape(title)}</text>
  <text x="{x + 435}" y="572" class="sans" fill="{accent}" font-size="19" text-anchor="end">{escape(tag)}</text>
  <path d="M{x + 30} 598h470" stroke="#496c7f" stroke-width="1.3"/>
  {icon}
  {flow(x, labels, accent)}
  {text_lines(summary, x + 31, 740, size=23, step=33)}
  <path d="M{x + 30} 826h470" stroke="#3d6175" stroke-opacity=".8" stroke-width="1.2"/>
  <text x="{x + 31}" y="858" class="sans" fill="#9dbacc" font-size="19">{escape(footer)}</text>
'''


normal_icon = '<path d="M625 551l-10 13h10l-4 13 15-18h-10l5-8Z" fill="#72d2ff" opacity=".9"/>'
plan_icon = '<path d="M1192 549l-9 5-9-5-9 5v22l9-5 9 5 9-5Z" fill="none" stroke="#93bfff" stroke-width="2.1" stroke-linejoin="round"/><path d="M1174 549v22m9-17v22" stroke="#93bfff" stroke-width="1.8"/>'
grill_icon = '<path d="M1765 548h-28a8 8 0 0 0-8 8v12a8 8 0 0 0 8 8h7l6 6v-6h15a8 8 0 0 0 8-8v-12a8 8 0 0 0-8-8Z" fill="none" stroke="#ffc17b" stroke-width="2"/><circle cx="1742" cy="562" r="2" fill="#ffc17b"/><circle cx="1751" cy="562" r="2" fill="#ffc17b"/><circle cx="1760" cy="562" r="2" fill="#ffc17b"/>'

cards = "".join(
    (
        card(
            116, "01", "普通模式", "普通对话", "#72d2ff", normal_icon,
            ("交任务", "Agent 判断", "进入实现"),
            ["直接开始处理任务；", "缺口是否被问出，取决于", "执行中的判断。"],
            "现场观察实际行为",
        ),
        card(
            695, "02", "Plan 模式", "Claude Code", "#93bfff", plan_icon,
            ("只读探索", "提出计划", "审查后实施"),
            ["先探索项目并提出计划，", "供开发者审查；批准后", "再进入实现。"],
        ),
        card(
            1274, "03", "Grill Me", "第三方 Skill", "#ffc17b", grill_icon,
            ("多轮提问", "明确决策", "再交给开发"),
            ["通过多轮追问，把任务中", "隐含的决策逐一说清，", "直到形成共同理解。"],
        ),
    )
)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" role="img" aria-labelledby="mode-title mode-desc">
  <title id="mode-title">同一任务，三条开工路径</title>
  <desc id="mode-desc">相同目录结构和 CLAUDE.md、相同任务提示词下，比较普通对话直接开工、Claude Code Plan 模式先规划、第三方 Grill Me Skill 先追问的流程。</desc>
  <defs>
    <radialGradient id="bg-glow" cx="78%" cy="26%" r="85%">
      <stop offset="0" stop-color="#16455f" stop-opacity=".47"/>
      <stop offset=".58" stop-color="#0a2a40" stop-opacity=".2"/>
      <stop offset="1" stop-color="#071423" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="card-fill" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#12334a"/>
      <stop offset="1" stop-color="#0a2033"/>
    </linearGradient>
    <filter id="card-shadow" x="-20%" y="-25%" width="140%" height="155%">
      <feDropShadow dx="0" dy="18" stdDeviation="21" flood-color="#000" flood-opacity=".28"/>
    </filter>
    <pattern id="dot-grid" x="0" y="0" width="34" height="34" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#72d2ff" opacity=".075"/>
    </pattern>
    <style><![CDATA[
      .sans{{font-family:'PingFang SC','Microsoft YaHei','Noto Sans SC',Arial,sans-serif}}
      .mono{{font-family:'JetBrains Mono','SFMono-Regular',Menlo,monospace}}
    ]]></style>
  </defs>
  <rect width="1920" height="1080" fill="#071423"/>
  <rect width="1920" height="1080" fill="url(#bg-glow)"/>
  <rect x="1000" y="0" width="920" height="1080" fill="url(#dot-grid)"/>
  <circle cx="1505" cy="597" r="480" fill="none" stroke="#72d2ff" stroke-opacity=".045" stroke-width="2"/>
  <circle cx="1505" cy="597" r="355" fill="none" stroke="#72d2ff" stroke-opacity=".055" stroke-width="2"/>

  <text x="116" y="105" class="sans" fill="#72d2ff" font-size="25" font-weight="700" letter-spacing="3">实践 06 · 同题对照</text>
  <rect x="116" y="128" width="107" height="5" rx="2.5" fill="#ffc17b"/>
  <text x="116" y="202" class="sans" fill="#f5f8fc" font-size="68" font-weight="760" letter-spacing="-1.5">同一任务，三条开工路径</text>
  <text x="118" y="253" class="sans" fill="#b8cadb" font-size="28">输入不变；观察开工前的交互方式如何改变开发过程。</text>

  <g filter="url(#card-shadow)">
    <rect x="116" y="301" width="1688" height="152" rx="25" fill="#0d2b40" stroke="#527991" stroke-width="2"/>
  </g>
  <rect x="139" y="320" width="486" height="114" rx="18" fill="#12374b" stroke="#5b9ab4" stroke-opacity=".6"/>
  <path d="M165 361h18l8 8h25v29h-51Z" fill="#26556b" stroke="#72d2ff" stroke-width="2" stroke-linejoin="round"/>
  <text x="233" y="360" class="sans" fill="#72d2ff" font-size="19" font-weight="700">相同项目骨架</text>
  <text x="233" y="399" class="sans" fill="#f5f8fc" font-size="29" font-weight="700">目录结构 + CLAUDE.md</text>
  <rect x="642" y="320" width="1138" height="114" rx="18" fill="#081e31" stroke="#607f8f" stroke-opacity=".8"/>
  <text x="835" y="359" class="sans" fill="#ffc17b" font-size="19" font-weight="700">相同任务提示词</text>
  <path d="M669 387l10 8-10 8" fill="none" stroke="#72d2ff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="694" y="404" class="sans" fill="#f5f8fc" font-size="28" font-weight="650">{escape(TASK)}</text>

  <path d="M960 453v25H381m579 0h579M381 478v40m579-40v40m579-40v40" fill="none" stroke="#6b9bb3" stroke-opacity=".82" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="381" cy="478" r="5.5" fill="#72d2ff"/><circle cx="960" cy="478" r="5.5" fill="#93bfff"/><circle cx="1539" cy="478" r="5.5" fill="#ffc17b"/>

  {cards}

  <rect x="116" y="926" width="1394" height="54" rx="14" fill="#0d283b" stroke="#395d72" stroke-width="1.3"/>
  <text x="141" y="960" class="sans" fill="#ffc17b" font-size="22" font-weight="700">课堂对照</text>
  <path d="M282 939v29" stroke="#486e82" stroke-width="1.2"/>
  <text x="305" y="960" class="sans" fill="#e3f0f7" font-size="22">先问什么</text>
  <circle cx="445" cy="952" r="3" fill="#72d2ff"/>
  <text x="471" y="960" class="sans" fill="#e3f0f7" font-size="22">何时写代码</text>
  <circle cx="638" cy="952" r="3" fill="#72d2ff"/>
  <text x="664" y="960" class="sans" fill="#e3f0f7" font-size="22">谁确认假设</text>
  <circle cx="833" cy="952" r="3" fill="#72d2ff"/>
  <text x="859" y="960" class="sans" fill="#e3f0f7" font-size="22">如何验证</text>
  <text x="116" y="1005" class="sans" fill="#88a1b8" font-size="21">AI 编码训练营 · 实践篇</text>
</svg>
'''

(HERE / "mode-compare.svg").write_text(svg, encoding="utf-8")
print("Wrote mode-compare.svg")
