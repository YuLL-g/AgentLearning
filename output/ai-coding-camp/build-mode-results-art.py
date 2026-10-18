"""Build the slide 20 illustration: predictions plus complementary roles."""

from pathlib import Path
from xml.sax.saxutils import escape


HERE = Path(__file__).parent


def cell(x: int, y: int, lines: tuple[str, str], accent: str) -> str:
    return f'''
  <circle cx="{x + 24}" cy="{y + 35}" r="4.5" fill="{accent}"/>
  <text x="{x + 43}" y="{y + 44}" class="sans" fill="#eaf3f8" font-size="22" font-weight="630">{escape(lines[0])}</text>
  <text x="{x + 43}" y="{y + 75}" class="sans" fill="#b8cedb" font-size="22">{escape(lines[1])}</text>
'''


rows = [
    (
        "01", "需求澄清",
        ("可能按字面开工", "隐含条件易留下"),
        ("会列实施假设", "需求仍需人确认"),
        ("多轮追问关键选择", "更易暴露隐含假设"),
    ),
    (
        "02", "关键测试覆盖",
        ("按项目规则写测试", "覆盖取决于需求理解"),
        ("可在计划中列场景", "断言仍需审查"),
        ("先澄清测试边界", "覆盖仍需 TDD 落实"),
    ),
    (
        "03", "是否擅自扩展",
        ("可能自行补全细节", "需警惕超出契约"),
        ("实施前可审范围", "便于删去多余动作"),
        ("先问清要与不要", "后续仍要守边界"),
    ),
    (
        "04", "耗时与人工介入",
        ("启动较快", "返工风险看结果"),
        ("先投入方案审查", "可能减少盲目修改"),
        ("前期问答较多", "可能减少方向性返工"),
    ),
]

matrix_rows = []
for i, (number, label, normal, plan, grill) in enumerate(rows):
    y = 360 + i * 100
    matrix_rows.append(f'''
  <rect x="117" y="{y}" width="1686" height="100" fill="{'#0c2a3f' if i % 2 == 0 else '#0a2337'}"/>
  <path d="M116 {y}h1688" stroke="#426277" stroke-opacity=".65" stroke-width="1.2"/>
  <text x="144" y="{y + 47}" class="mono" fill="#72d2ff" font-size="19" font-weight="750">{number}</text>
  <text x="196" y="{y + 55}" class="sans" fill="#f5f8fc" font-size="25" font-weight="690">{escape(label)}</text>
  {cell(385, y, normal, "#72d2ff")}
  {cell(858, y, plan, "#93bfff")}
  {cell(1331, y, grill, "#ffc17b")}
''')


def role_card(x: int, accent: str, tag: str, title: str, line1: str, line2: str) -> str:
    return f'''
  <rect x="{x}" y="797" width="530" height="132" rx="21" fill="url(#role-fill)" stroke="{accent}" stroke-opacity=".58" stroke-width="1.8"/>
  <rect x="{x}" y="797" width="530" height="4" rx="2" fill="{accent}"/>
  <rect x="{x + 24}" y="815" width="108" height="32" rx="9" fill="{accent}" fill-opacity=".15" stroke="{accent}" stroke-opacity=".48"/>
  <text x="{x + 78}" y="837" class="sans" fill="{accent}" font-size="21" font-weight="760" text-anchor="middle">{escape(tag)}</text>
  <text x="{x + 150}" y="840" class="sans" fill="#f5f8fc" font-size="28" font-weight="740">{escape(title)}</text>
  <text x="{x + 25}" y="879" class="sans" fill="#e5f0f6" font-size="22">{escape(line1)}</text>
  <text x="{x + 25}" y="909" class="sans" fill="#b6cedb" font-size="22">{escape(line2)}</text>
'''


roles = "".join(
    [
        role_card(
            116, "#ffc17b", "要什么", "Grill Me",
            "逐层盘问决策与假设；",
            "先对齐共识，方案不是主要产物。",
        ),
        role_card(
            695, "#93bfff", "怎么做", "Plan 模式",
            "只读探索并提交可审查方案；",
            "人工批准后，再进入实现。",
        ),
        role_card(
            1274, "#72d2ff", "如何验证", "TDD",
            "测试先行、小步实现、回归审查；",
            "验证已写清的约定，不能代替澄清。",
        ),
    ]
)


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" role="img" aria-labelledby="results-title results-desc">
  <title id="results-title">三种路径，实践里差在哪？</title>
  <desc id="results-desc">演示前预测：普通模式、Plan 模式、Grill Me 在需求澄清、关键测试覆盖、是否擅自扩展、耗时与人工介入上的倾向。底部说明 Grill Me 澄清要什么，Plan 模式规划怎么做，TDD 用测试先行和回归审查检验实现。预测待现场核对。</desc>
  <defs>
    <radialGradient id="bg-glow" cx="80%" cy="27%" r="84%">
      <stop offset="0" stop-color="#17475e" stop-opacity=".45"/>
      <stop offset=".56" stop-color="#0c2b41" stop-opacity=".22"/>
      <stop offset="1" stop-color="#071423" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="role-fill" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#12354a"/>
      <stop offset="1" stop-color="#0a2033"/>
    </linearGradient>
    <filter id="panel-shadow" x="-15%" y="-18%" width="130%" height="145%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000" flood-opacity=".25"/>
    </filter>
    <pattern id="dot-grid" x="0" y="0" width="34" height="34" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#72d2ff" opacity=".07"/>
    </pattern>
    <style><![CDATA[
      .sans{{font-family:'PingFang SC','Microsoft YaHei','Noto Sans SC',Arial,sans-serif}}
      .mono{{font-family:'JetBrains Mono','SFMono-Regular',Menlo,monospace}}
    ]]></style>
  </defs>
  <rect width="1920" height="1080" fill="#071423"/>
  <rect width="1920" height="1080" fill="url(#bg-glow)"/>
  <rect x="975" y="0" width="945" height="1080" fill="url(#dot-grid)"/>
  <circle cx="1508" cy="585" r="488" fill="none" stroke="#72d2ff" stroke-opacity=".045" stroke-width="2"/>
  <circle cx="1508" cy="585" r="358" fill="none" stroke="#72d2ff" stroke-opacity=".055" stroke-width="2"/>

  <text x="116" y="105" class="sans" fill="#72d2ff" font-size="25" font-weight="700" letter-spacing="3">实践 07 · 同题预测</text>
  <rect x="116" y="128" width="107" height="5" rx="2.5" fill="#ffc17b"/>
  <text x="116" y="202" class="sans" fill="#f5f8fc" font-size="67" font-weight="760" letter-spacing="-1.5">三种路径，实践里差在哪？</text>
  <text x="118" y="253" class="sans" fill="#b8cadb" font-size="27">同一项目骨架、CLAUDE.md 与任务提示词；以下为演示前预测，待现场核对。</text>
  <rect x="1593" y="83" width="211" height="45" rx="13" fill="#17394e" stroke="#72d2ff" stroke-opacity=".55"/>
  <circle cx="1621" cy="105" r="5" fill="#ffc17b"/>
  <text x="1640" y="113" class="sans" fill="#cbeafe" font-size="21" font-weight="700">预测 · 待实测</text>

  <g filter="url(#panel-shadow)">
    <rect x="116" y="294" width="1688" height="466" rx="24" fill="#0a2438" stroke="#547c91" stroke-width="2"/>
  </g>
  <path d="M385 295v464M858 295v464M1331 295v464" stroke="#54748a" stroke-opacity=".74" stroke-width="1.3"/>
  <rect x="116" y="294" width="1688" height="66" rx="24" fill="#12374c"/>
  <rect x="116" y="333" width="1688" height="27" fill="#12374c"/>
  <rect x="385" y="294" width="473" height="4" fill="#72d2ff"/>
  <rect x="858" y="294" width="473" height="4" fill="#93bfff"/>
  <rect x="1331" y="294" width="473" height="4" fill="#ffc17b"/>
  <text x="144" y="337" class="sans" fill="#b9d2df" font-size="24" font-weight="700">比较维度</text>
  <text x="427" y="338" class="sans" fill="#72d2ff" font-size="28" font-weight="730">普通模式</text>
  <text x="900" y="338" class="sans" fill="#a9caff" font-size="28" font-weight="730">Plan 模式</text>
  <text x="1373" y="338" class="sans" fill="#ffc17b" font-size="28" font-weight="730">Grill Me</text>
  {''.join(matrix_rows)}
  <path d="M116 760h1688" stroke="#6d91a4" stroke-width="1.6"/>

  {roles}
  <path d="M659 863h24m-8-8 8 8-8 8" fill="none" stroke="#729aaf" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M1238 863h24m-8-8 8 8-8 8" fill="none" stroke="#729aaf" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="116" y="968" class="sans" fill="#a0bccc" font-size="19">三者可串联使用；预测仅用于提出观察问题，具体结果以课堂演示和验收为准。</text>
  <text x="116" y="1005" class="sans" fill="#88a1b8" font-size="21">AI 编码训练营 · 实践篇</text>
</svg>
'''

(HERE / "mode-results.svg").write_text(svg, encoding="utf-8")
print("Wrote mode-results.svg")
