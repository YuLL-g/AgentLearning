"""Build slide 21: choose and combine development approaches."""

from pathlib import Path


HERE = Path(__file__).parent


def card(x: int, width: int, accent: str, number: str, title: str, detail: str, symbol: str, kind: str) -> str:
    return f'''
  <g filter="url(#card-shadow)">
    <rect x="{x}" y="526" width="{width}" height="272" rx="24" fill="#0d293d" stroke="{accent}" stroke-opacity=".6" stroke-width="2"/>
  </g>
  <rect x="{x}" y="526" width="{width}" height="5" rx="2.5" fill="{accent}"/>
  <circle cx="{x + 53}" cy="584" r="27" fill="{accent}" fill-opacity=".14" stroke="{accent}" stroke-opacity=".6" stroke-width="1.5"/>
  <text x="{x + 53}" y="593" class="sans" text-anchor="middle" fill="{accent}" font-size="27" font-weight="760">{symbol}</text>
  <text x="{x + 31}" y="659" class="mono" fill="{accent}" font-size="21" font-weight="750">{number}</text>
  <text x="{x + width - 29}" y="593" class="sans" text-anchor="end" fill="{accent}" fill-opacity=".8" font-size="18" font-weight="650">{kind}</text>
  <text x="{x + 31}" y="704" class="sans" fill="#f7fbff" font-size="37" font-weight="750">{title}</text>
  <text x="{x + 31}" y="750" class="sans" fill="#bbd0dc" font-size="22">{detail}</text>
'''


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" role="img" aria-labelledby="choice-title choice-desc">
  <title id="choice-title">实际开发中用什么模式？</title>
  <desc id="choice-desc">没有固定的最佳模式，应按需求清晰度、项目约束与人工审核成本选择，也可以组合使用。课堂实践从工程骨架出发，经 Grill Me 澄清需求、Plan 模式制定计划、TDD 逐步实现与验证，可选用 /code-review 审查当前改动。</desc>
  <defs>
    <radialGradient id="bg-glow" cx="73%" cy="44%" r="82%">
      <stop offset="0" stop-color="#17475e" stop-opacity=".42"/>
      <stop offset=".55" stop-color="#0c2b41" stop-opacity=".19"/>
      <stop offset="1" stop-color="#071423" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="choice-band" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#133a4e"/>
      <stop offset="1" stop-color="#0d2b41"/>
    </linearGradient>
    <filter id="card-shadow" x="-15%" y="-20%" width="140%" height="155%">
      <feDropShadow dx="0" dy="17" stdDeviation="18" flood-color="#000" flood-opacity=".26"/>
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
  <rect x="954" width="966" height="1080" fill="url(#dot-grid)"/>
  <circle cx="1548" cy="690" r="490" fill="none" stroke="#72d2ff" stroke-opacity=".045" stroke-width="2"/>
  <circle cx="1548" cy="690" r="355" fill="none" stroke="#72d2ff" stroke-opacity=".055" stroke-width="2"/>

  <text x="116" y="105" class="sans" fill="#72d2ff" font-size="25" font-weight="700" letter-spacing="3">实践 08 · 方法选择</text>
  <rect x="116" y="128" width="107" height="5" rx="2.5" fill="#ffc17b"/>
  <text x="116" y="207" class="sans" fill="#f5f8fc" font-size="70" font-weight="760" letter-spacing="-1.5">实际开发中用什么模式？</text>
  <text x="118" y="274" class="sans" fill="#d8e8f0" font-size="30" font-weight="540">没有固定的最佳模式；按项目情况选择，也可以组合使用。</text>

  <rect x="116" y="324" width="1688" height="112" rx="20" fill="url(#choice-band)" stroke="#4f7e96" stroke-opacity=".76" stroke-width="1.5"/>
  <text x="150" y="375" class="sans" fill="#ffc17b" font-size="24" font-weight="760">选择时看</text>
  <path d="M303 343v74" stroke="#65879a" stroke-opacity=".55" stroke-width="1.5"/>
  <g class="sans" font-size="27" font-weight="650" fill="#e8f2f7">
    <circle cx="358" cy="379" r="5" fill="#72d2ff"/>
    <text x="380" y="388">需求是否清晰</text>
    <circle cx="810" cy="379" r="5" fill="#93bfff"/>
    <text x="832" y="388">项目与交付约束</text>
    <circle cx="1344" cy="379" r="5" fill="#ffc17b"/>
    <text x="1366" y="388">人工审核成本</text>
  </g>

  <text x="116" y="494" class="sans" fill="#d9e8f1" font-size="29" font-weight="670">接下来，一起从工程骨架出发，走一遍组合流程</text>
  <path d="M116 509h1688" stroke="#638da1" stroke-opacity=".42" stroke-width="1.4"/>

  {card(116, 289, '#a3d8e8', 'START', '工程骨架', '目录结构 + CLAUDE.md', '⌂', '起点')}
  {card(445, 385, '#ffc17b', '01  ·  CLARIFY', 'Grill Me', '反复追问，澄清要什么', '?', '第三方 Skill')}
  {card(870, 385, '#93bfff', '02  ·  PLAN', 'Plan 模式', '形成可审阅的实施计划', '≡', 'Claude Code 模式')}
  {card(1295, 509, '#72d2ff', '03  ·  BUILD', 'TDD', '测试先行，小步实现与验证', '✓', '开发流程')}

  <g fill="none" stroke="#9bb5c4" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round">
    <path d="M412 661h22m-8-8 8 8-8 8"/>
    <path d="M837 661h22m-8-8 8 8-8 8"/>
    <path d="M1262 661h22m-8-8 8 8-8 8"/>
  </g>

  <path d="M118 840h1686" stroke="#4d7185" stroke-opacity=".5" stroke-width="1.5"/>
  <path d="M1549 798v44" stroke="#ffc17b" stroke-opacity=".7" stroke-width="2" stroke-dasharray="5 6"/>
  <text x="116" y="892" class="sans" fill="#a8c2d2" font-size="23" font-weight="700">TDD 循环</text>
  <rect x="253" y="853" width="140" height="58" rx="13" fill="#173d51" stroke="#72d2ff" stroke-opacity=".5"/>
  <rect x="429" y="853" width="160" height="58" rx="13" fill="#173d51" stroke="#72d2ff" stroke-opacity=".5"/>
  <rect x="625" y="853" width="165" height="58" rx="13" fill="#173d51" stroke="#72d2ff" stroke-opacity=".5"/>
  <g class="mono" fill="#dcf4ff" font-size="25" font-weight="740" text-anchor="middle">
    <text x="323" y="891">Red</text>
    <text x="509" y="891">Green</text>
    <text x="707" y="891">Review</text>
  </g>
  <g fill="none" stroke="#77b6d1" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M400 882h19m-7-7 7 7-7 7"/>
    <path d="M596 882h19m-7-7 7 7-7 7"/>
  </g>

  <rect x="979" y="844" width="825" height="76" rx="17" fill="#123247" stroke="#ffc17b" stroke-opacity=".62" stroke-width="1.5"/>
  <rect x="1001" y="864" width="84" height="35" rx="9" fill="#ffc17b" fill-opacity=".15"/>
  <text x="1043" y="889" class="sans" fill="#ffc17b" font-size="20" font-weight="760" text-anchor="middle">可选</text>
  <text x="1104" y="892" class="mono" fill="#fff2e0" font-size="26" font-weight="740">/code-review</text>
  <text x="1357" y="891" class="sans" fill="#d3e2ea" font-size="22">审查当前改动，人工判断问题</text>

  <text x="116" y="989" class="sans" fill="#8da8ba" font-size="21">AI 编码训练营 · 实践篇</text>
</svg>
'''

(HERE / "mode-choice.svg").write_text(svg, encoding="utf-8")
print("Wrote mode-choice.svg")
