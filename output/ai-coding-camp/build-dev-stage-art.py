"""Build the illustrated practice slide about the first development steps."""

from pathlib import Path
from xml.sax.saxutils import escape


HERE = Path(__file__).parent


def step(index: int, y: int, title: str, detail: str, *, accent: str = "#72d2ff", extra: str = "") -> str:
    return f"""
  <g class="step{index}">
    <path d="M194 {y+51} H212" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>
    <rect x="212" y="{y}" width="712" height="102" rx="19" fill="#102d43" stroke="{accent}" stroke-opacity=".48" stroke-width="1.7"/>
    <rect x="212" y="{y}" width="7" height="102" rx="3.5" fill="{accent}"/>
    <circle cx="165" cy="{y+51}" r="29" fill="#14394e" stroke="{accent}" stroke-width="2.5"/>
    <text x="165" y="{y+59}" class="mono" fill="{accent}" font-size="23" font-weight="700" text-anchor="middle">{index:02d}</text>
    <text x="250" y="{y+42}" class="sans" fill="#f5f8fc" font-size="30" font-weight="710">{escape(title)}</text>
    <text x="250" y="{y+79}" class="sans" fill="#aac4d4" font-size="22">{escape(detail)}</text>
    {extra}
  </g>"""


commit = """
    <rect x="489" y="692" width="393" height="48" rx="14" fill="#40392f" stroke="#a98055" stroke-width="1.3"/>
    <circle cx="514" cy="716" r="7" fill="#ffc17b"/>
    <text x="535" y="724" class="mono" fill="#ffd7a7" font-size="20" font-weight="600">build project skeleton</text>"""

tdd = """
    <g aria-hidden="true">
      <circle cx="771" cy="828" r="8" fill="#ff897f"/>
      <path d="M782 828h24" stroke="#7fa9bd" stroke-width="2.3" stroke-linecap="round"/>
      <path d="m801 823 6 5-6 5" fill="none" stroke="#7fa9bd" stroke-width="2.3" stroke-linejoin="round"/>
      <circle cx="821" cy="828" r="8" fill="#7ee7a0"/>
      <path d="M832 828h24" stroke="#7fa9bd" stroke-width="2.3" stroke-linecap="round"/>
      <path d="m851 823 6 5-6 5" fill="none" stroke="#7fa9bd" stroke-width="2.3" stroke-linejoin="round"/>
      <circle cx="871" cy="828" r="8" fill="#72d2ff"/>
    </g>"""


def svg(root_class: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" class="{root_class}" role="img" aria-labelledby="dev-title dev-desc">
  <title id="dev-title">从需求契约进入开发</title>
  <desc id="dev-desc">按顺序初始化代码仓库、构建项目骨架、写 CLAUDE.md、以 build project skeleton 为信息初次提交，再用 TDD 做最小实现和增量开发。右侧展示 myls 项目树、CLAUDE.md 的四类重点，以及红、绿、重构的 TDD 循环。</desc>
  <defs>
    <radialGradient id="dev-bg" cx="88%" cy="16%" r="88%">
      <stop offset="0" stop-color="#17465e" stop-opacity=".48"/>
      <stop offset=".58" stop-color="#0a2a40" stop-opacity=".18"/>
      <stop offset="1" stop-color="#071423" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="dev-panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#102e44"/>
      <stop offset="1" stop-color="#0a2134"/>
    </linearGradient>
    <filter id="dev-shadow" x="-10%" y="-18%" width="120%" height="142%">
      <feDropShadow dx="0" dy="18" stdDeviation="23" flood-color="#000" flood-opacity=".29"/>
    </filter>
    <style><![CDATA[
      .sans{{font-family:'PingFang SC','Microsoft YaHei','Noto Sans SC',Arial,sans-serif}}
      .mono{{font-family:'JetBrains Mono','SFMono-Regular',Menlo,monospace}}
      .play .step1,.play .step2,.play .step3,.play .step4,.play .step5,.play .tree,.play .instructions,.play .link,.play .tdd-flow{{opacity:0}}
      .play .step1{{animation:rise .43s ease .25s both}}
      .play .step2{{animation:rise .43s ease .67s both}}
      .play .tree{{animation:rise .5s ease 1.04s both}}
      .play .step3{{animation:rise .43s ease 1.5s both}}
      .play .link{{animation:rise .3s ease 1.86s both}}
      .play .instructions{{animation:rise .5s ease 2.03s both}}
      .play .step4{{animation:rise .43s ease 2.52s both}}
      .play .step5{{animation:rise .43s ease 2.94s both}}
      .play .tdd-flow{{animation:rise .5s ease 3.3s both}}
      @keyframes rise{{from{{opacity:0;transform:translateY(17px)}}to{{opacity:1;transform:translateY(0)}}}}
      @media (prefers-reduced-motion:reduce){{.play .step1,.play .step2,.play .step3,.play .step4,.play .step5,.play .tree,.play .instructions,.play .link,.play .tdd-flow{{opacity:1;animation:none}}}}
    ]]></style>
  </defs>

  <rect width="1920" height="1080" fill="#071423"/>
  <rect width="1920" height="1080" fill="url(#dev-bg)"/>
  <circle cx="1590" cy="548" r="530" fill="none" stroke="#72d2ff" stroke-opacity=".055" stroke-width="2"/>
  <circle cx="1590" cy="548" r="380" fill="none" stroke="#72d2ff" stroke-opacity=".065" stroke-width="2"/>
  <text x="116" y="105" class="sans" fill="#72d2ff" font-size="25" font-weight="700" letter-spacing="3">实践 04 · 工程起步</text>
  <rect x="116" y="128" width="107" height="5" rx="2.5" fill="#ffc17b"/>
  <text x="116" y="204" class="sans" fill="#f5f8fc" font-size="71" font-weight="760" letter-spacing="-1.5">从需求契约进入开发</text>
  <text x="119" y="260" class="sans" fill="#b8cadb" font-size="28">先建立可构建、可测试、可回滚的基线，再按 TDD 小步实现。</text>

  <path d="M165 369 V845" stroke="#456c82" stroke-width="3.2" stroke-linecap="round"/>
  <path d="M165 369 V605" stroke="#72d2ff" stroke-opacity=".28" stroke-width="8" stroke-linecap="round"/>
  {step(1, 318, "初始化代码仓库", "让每次修改都有历史可追溯")}
  {step(2, 437, "构建项目骨架", "准备源码、头文件、测试与构建入口")}
  {step(3, 556, "写 CLAUDE.md", "写入项目特有、长期有效的协作约定")}
  {step(4, 675, "初次提交", "保存一个可回滚的工程基线", accent="#ffc17b", extra=commit)}
  {step(5, 794, "TDD 最小实现增量开发", "先写失败测试 → 最小实现 → 每步验证", extra=tdd)}

  <g class="tree" filter="url(#dev-shadow)">
    <rect x="970" y="275" width="834" height="279" rx="24" fill="url(#dev-panel)" stroke="#496d83" stroke-width="1.8"/>
    <path d="M994 276 H1780 Q1804 276 1804 300 V323 H970 V300 Q970 276 994 276Z" fill="#15384d"/>
    <path d="M970 323 H1804" stroke="#496d83" stroke-width="1.5"/>
    <path d="M1015 291h25l8 8h25v14h-58z" fill="none" stroke="#72d2ff" stroke-width="2.5" stroke-linejoin="round"/>
    <text x="1090" y="310" class="sans" fill="#f5f8fc" font-size="28" font-weight="700">项目骨架</text>
    <text x="1021" y="354" class="mono" fill="#72d2ff" font-size="24" font-weight="720">myls/</text>
    <text x="1021" y="383" class="mono" fill="#dcebf4" font-size="23">├── .gitignore</text>
    <rect x="1005" y="389" width="763" height="31" rx="9" fill="#584432" fill-opacity=".46" stroke="#ffc17b" stroke-opacity=".31"/>
    <text x="1021" y="412" class="mono" fill="#ffd19a" font-size="23" font-weight="700">├── CLAUDE.md</text>
    <text x="1021" y="441" class="mono" fill="#dcebf4" font-size="23">├── Makefile</text>
    <text x="1021" y="470" class="mono" fill="#dcebf4" font-size="23">├── include/</text>
    <text x="1021" y="499" class="mono" fill="#dcebf4" font-size="23">├── src/</text>
    <text x="1021" y="528" class="mono" fill="#dcebf4" font-size="23">└── tests/</text>
  </g>

  <g class="link" fill="none" stroke="#ffc17b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M1387 558v18"/>
    <path d="m1379 568 8 8 8-8"/>
  </g>

  <g class="instructions" filter="url(#dev-shadow)">
    <rect x="970" y="582" width="834" height="171" rx="24" fill="url(#dev-panel)" stroke="#8b7159" stroke-width="1.8"/>
    <path d="M994 583 H1780 Q1804 583 1804 607 V629 H970 V607 Q970 583 994 583Z" fill="#273c4b"/>
    <path d="M970 629 H1804" stroke="#8b7159" stroke-width="1.5"/>
    <rect x="1014" y="592" width="25" height="28" rx="4" fill="none" stroke="#ffc17b" stroke-width="2.2"/>
    <path d="M1020 601h13M1020 608h10M1020 615h12" stroke="#ffc17b" stroke-width="1.8" stroke-linecap="round"/>
    <text x="1056" y="614" class="sans" fill="#f5f8fc" font-size="27" font-weight="710">CLAUDE.md 的四个重点</text>
    <path d="M1387 641 V739" stroke="#496d83" stroke-opacity=".55" stroke-width="1.2"/>
    <circle cx="1015" cy="653" r="5" fill="#72d2ff"/>
    <text x="1031" y="661" class="sans" fill="#ffc17b" font-size="21" font-weight="710">项目与依据</text>
    <text x="1031" y="686" class="sans" fill="#dcebf4" font-size="19">C/POSIX myls · 已评审契约</text>
    <circle cx="1413" cy="653" r="5" fill="#72d2ff"/>
    <text x="1429" y="661" class="sans" fill="#ffc17b" font-size="21" font-weight="710">目录与命令</text>
    <text x="1429" y="686" class="sans" fill="#dcebf4" font-size="18.5">make all · make test · make clean</text>
    <circle cx="1015" cy="710" r="5" fill="#72d2ff"/>
    <text x="1031" y="718" class="sans" fill="#ffc17b" font-size="21" font-weight="710">开发边界</text>
    <text x="1031" y="743" class="sans" fill="#dcebf4" font-size="19">最小实现 · 测试先行</text>
    <circle cx="1413" cy="710" r="5" fill="#72d2ff"/>
    <text x="1429" y="718" class="sans" fill="#ffc17b" font-size="21" font-weight="710">验证与交付</text>
    <text x="1429" y="743" class="sans" fill="#dcebf4" font-size="19">构建 · 测试 · diff · 未验证项</text>
  </g>

  <g class="tdd-flow" filter="url(#dev-shadow)">
    <rect x="970" y="772" width="834" height="155" rx="24" fill="url(#dev-panel)" stroke="#608894" stroke-width="1.8"/>
    <path d="M994 773 H1780 Q1804 773 1804 797 V812 H970 V797 Q970 773 994 773Z" fill="#193b48"/>
    <path d="M970 812 H1804" stroke="#608894" stroke-width="1.5"/>
    <path d="M1014 793h25m-25 7h25m-25 7h25" stroke="#72d2ff" stroke-width="2.5" stroke-linecap="round"/>
    <text x="1056" y="801" class="sans" fill="#f5f8fc" font-size="26" font-weight="710">TDD 基本循环</text>
    <text x="1777" y="801" class="mono" text-anchor="end" fill="#90b8c9" font-size="17">每次只推进一小步</text>

    <rect x="1009" y="825" width="230" height="65" rx="13" fill="#422b35" stroke="#ff897f" stroke-opacity=".72" stroke-width="1.5"/>
    <circle cx="1032" cy="848" r="6" fill="#ff897f"/>
    <text x="1048" y="855" class="mono" fill="#ffaaa2" font-size="23" font-weight="750">RED</text>
    <text x="1027" y="880" class="sans" fill="#f5f8fc" font-size="18">先写测试，确认失败</text>

    <path d="M1248 857 H1271m-8-7 8 7-8 7" fill="none" stroke="#8fb7c6" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

    <rect x="1281" y="825" width="230" height="65" rx="13" fill="#1c3c3a" stroke="#7ee7a0" stroke-opacity=".72" stroke-width="1.5"/>
    <circle cx="1304" cy="848" r="6" fill="#7ee7a0"/>
    <text x="1320" y="855" class="mono" fill="#a4f2b9" font-size="23" font-weight="750">GREEN</text>
    <text x="1297" y="880" class="sans" fill="#f5f8fc" font-size="18">最小代码使测试通过</text>

    <path d="M1520 857 H1543m-8-7 8 7-8 7" fill="none" stroke="#8fb7c6" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

    <rect x="1553" y="825" width="230" height="65" rx="13" fill="#1b384b" stroke="#72d2ff" stroke-opacity=".72" stroke-width="1.5"/>
    <circle cx="1576" cy="848" r="6" fill="#72d2ff"/>
    <text x="1592" y="855" class="mono" fill="#9fe1ff" font-size="22" font-weight="750">REFACTOR</text>
    <text x="1569" y="880" class="sans" fill="#f5f8fc" font-size="18">重构，保持测试通过</text>

    <path d="M1668 895 V903 Q1668 909 1662 909 H1126 Q1120 909 1120 903 V896m-7 7 7-7 7 7" fill="none" stroke="#8fb7c6" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/>
    <rect x="1288" y="899" width="193" height="26" rx="12" fill="#102a3d"/>
    <text x="1385" y="918" class="sans" text-anchor="middle" fill="#aac4d4" font-size="17">下一条可验证需求</text>
  </g>
  <text x="116" y="1005" class="sans" fill="#88a1b8" font-size="21">AI 编码训练营 · 实践篇</text>
</svg>
'''


for kind in ("final", "play"):
    suffix = "final" if kind == "final" else "animated"
    (HERE / f"dev-stage-{suffix}.svg").write_text(svg(kind), encoding="utf-8")
