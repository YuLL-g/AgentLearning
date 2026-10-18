"""Build slide 22: a course assignment and personal branch rules."""

from pathlib import Path


HERE = Path(__file__).parent

svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" role="img" aria-labelledby="assignment-title assignment-desc">
  <title id="assignment-title">实践任务：完成后续需求开发</title>
  <desc id="assignment-desc">依据需求列表与验收契约完成后续需求开发。在已有基线上创建自己的分支，分支名为工号1_工号2；只在新建的个人分支上提交，不要提交到 develop 或 master。页面下方提供课堂代码仓库链接。</desc>
  <defs>
    <radialGradient id="bg-glow" cx="65%" cy="45%" r="84%">
      <stop offset="0" stop-color="#17475e" stop-opacity=".4"/>
      <stop offset=".56" stop-color="#0c2b41" stop-opacity=".17"/>
      <stop offset="1" stop-color="#071423" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="panel-fill" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#123449"/>
      <stop offset="1" stop-color="#0b2438"/>
    </linearGradient>
    <filter id="panel-shadow" x="-14%" y="-20%" width="135%" height="150%">
      <feDropShadow dx="0" dy="16" stdDeviation="21" flood-color="#000" flood-opacity=".26"/>
    </filter>
    <pattern id="dot-grid" x="0" y="0" width="34" height="34" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#72d2ff" opacity=".07"/>
    </pattern>
    <style><![CDATA[
      .sans{font-family:'PingFang SC','Microsoft YaHei','Noto Sans SC',Arial,sans-serif}
      .mono{font-family:'JetBrains Mono','SFMono-Regular',Menlo,monospace}
    ]]></style>
  </defs>
  <rect width="1920" height="1080" fill="#071423"/>
  <rect width="1920" height="1080" fill="url(#bg-glow)"/>
  <rect x="950" width="970" height="1080" fill="url(#dot-grid)"/>
  <circle cx="1510" cy="660" r="478" fill="none" stroke="#72d2ff" stroke-opacity=".045" stroke-width="2"/>
  <circle cx="1510" cy="660" r="345" fill="none" stroke="#72d2ff" stroke-opacity=".05" stroke-width="2"/>

  <text x="116" y="105" class="sans" fill="#72d2ff" font-size="25" font-weight="700" letter-spacing="3">实践 09 · 独立练习</text>
  <rect x="116" y="128" width="107" height="5" rx="2.5" fill="#ffc17b"/>
  <text x="116" y="207" class="sans" fill="#f6f9fc" font-size="68" font-weight="760" letter-spacing="-1.4">实践任务：完成后续需求开发</text>
  <text x="118" y="268" class="sans" fill="#c3d6e2" font-size="29">依据需求列表与验收契约，逐项实现并验证。</text>

  <g filter="url(#panel-shadow)">
    <rect x="116" y="328" width="779" height="442" rx="25" fill="url(#panel-fill)" stroke="#5c91a9" stroke-opacity=".85" stroke-width="2"/>
    <rect x="928" y="328" width="876" height="442" rx="25" fill="url(#panel-fill)" stroke="#5c91a9" stroke-opacity=".85" stroke-width="2"/>
  </g>
  <rect x="116" y="328" width="779" height="5" rx="2.5" fill="#72d2ff"/>
  <rect x="928" y="328" width="876" height="5" rx="2.5" fill="#ffc17b"/>

  <text x="153" y="386" class="sans" fill="#72d2ff" font-size="21" font-weight="760" letter-spacing="2">DEVELOPMENT</text>
  <text x="153" y="432" class="sans" fill="#f7fbff" font-size="39" font-weight="740">按已澄清的需求继续开发</text>
  <text x="154" y="474" class="sans" fill="#b7ccda" font-size="23">以两份材料为输入，以验收结果为准</text>

  <rect x="154" y="520" width="306" height="77" rx="15" fill="#173b51" stroke="#6aaac7" stroke-opacity=".65"/>
  <rect x="154" y="615" width="306" height="77" rx="15" fill="#173b51" stroke="#6aaac7" stroke-opacity=".65"/>
  <path d="M180 541h22l9 9v25h-31zM202 541v9h9M180 636h22l9 9v25h-31zM202 636v9h9" fill="none" stroke="#72d2ff" stroke-width="2.2" stroke-linejoin="round"/>
  <text x="229" y="569" class="sans" fill="#e9f5fb" font-size="27" font-weight="680">需求列表</text>
  <text x="229" y="664" class="sans" fill="#e9f5fb" font-size="27" font-weight="680">验收契约</text>
  <path d="M485 606h62m-15-15 15 15-15 15" fill="none" stroke="#8cd4ec" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="572" y="532" width="277" height="147" rx="19" fill="#0b3044" stroke="#72d2ff" stroke-opacity=".75" stroke-width="2"/>
  <circle cx="616" cy="577" r="18" fill="#72d2ff" fill-opacity=".16" stroke="#72d2ff" stroke-opacity=".6"/>
  <path d="m607 577 6 6 12-13" fill="none" stroke="#9be4f5" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="647" y="586" class="sans" fill="#f7fbff" font-size="28" font-weight="720">开发与验证</text>
  <text x="603" y="631" class="sans" fill="#bbd1de" font-size="22">完成后续需求</text>

  <text x="965" y="386" class="sans" fill="#ffc17b" font-size="21" font-weight="760" letter-spacing="2">BRANCH RULES</text>
  <text x="965" y="432" class="sans" fill="#f7fbff" font-size="39" font-weight="740">先建个人分支，再提交</text>
  <text x="966" y="474" class="sans" fill="#b7ccda" font-size="23">从已有基线创建自己的分支</text>

  <path d="M1005 566h395m-16-16 16 16-16 16" fill="none" stroke="#78a2b9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="1010" cy="566" r="11" fill="#163d52" stroke="#9ac2d5" stroke-width="3"/>
  <text x="966" y="533" class="sans" fill="#c7dbe5" font-size="22">已有基线</text>
  <rect x="1415" y="520" width="344" height="91" rx="18" fill="#244437" stroke="#9bd6a9" stroke-opacity=".75" stroke-width="2"/>
  <circle cx="1452" cy="565" r="19" fill="#9bd6a9" fill-opacity=".17"/>
  <path d="m1443 565 7 7 12-14" fill="none" stroke="#a9e4b3" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="1484" y="549" class="sans" fill="#a9e4b3" font-size="18" font-weight="700">分支名</text>
  <text x="1484" y="585" class="mono" fill="#e6ffea" font-size="29" font-weight="760">工号1_工号2</text>

  <rect x="965" y="642" width="405" height="79" rx="15" fill="#173d3f" stroke="#7bcda3" stroke-opacity=".6"/>
  <text x="994" y="689" class="sans" fill="#ccf5da" font-size="25" font-weight="680">✓ 只在自己的新分支提交</text>
  <rect x="1391" y="642" width="368" height="79" rx="15" fill="#3b2b34" stroke="#ee9aa6" stroke-opacity=".6"/>
  <text x="1417" y="674" class="sans" fill="#f3bac3" font-size="21" font-weight="690">不要提交到</text>
  <text x="1417" y="704" class="mono" fill="#ffd7dd" font-size="23" font-weight="720">develop / master</text>

  <rect x="116" y="811" width="1688" height="142" rx="22" fill="#103247" stroke="#578aa1" stroke-opacity=".85" stroke-width="1.8"/>
  <rect x="116" y="811" width="5" height="142" rx="2.5" fill="#72d2ff"/>
  <text x="153" y="856" class="sans" fill="#72d2ff" font-size="22" font-weight="740" letter-spacing="1">代码仓库 · 点击打开</text>
  <text x="153" y="919" class="mono" fill="#e9f5fb" font-size="24">https://gitlab.zte.com.cn/person/#/admin/projects/10355114/AI_Coding_RCH_202610</text>
  <path d="M1765 854h-33m33 0v33m0-33-55 55" fill="none" stroke="#72d2ff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="116" y="1002" class="sans" fill="#8ca7b9" font-size="21">AI 编码训练营 · 实践篇</text>
</svg>
'''

(HERE / "practice-assignment.svg").write_text(svg, encoding="utf-8")
print("Wrote practice-assignment.svg")
