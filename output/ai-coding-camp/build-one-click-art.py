"""Build the two illustrated states of the one-click Agent discussion slide."""

from pathlib import Path


HERE = Path(__file__).parent


def shell(body: str, description: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" role="img" aria-labelledby="title description">
  <title id="title">把交付目标直接交给 Agent，会怎样？</title>
  <desc id="description">{description}</desc>
  <defs>
    <radialGradient id="glow" cx="81%" cy="33%" r="84%">
      <stop offset="0" stop-color="#164963" stop-opacity=".47"/>
      <stop offset=".55" stop-color="#0a2941" stop-opacity=".24"/>
      <stop offset="1" stop-color="#071423" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#102c41"/>
      <stop offset="1" stop-color="#091e31"/>
    </linearGradient>
    <linearGradient id="agent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#245a70"/>
      <stop offset="1" stop-color="#0d304a"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="18" stdDeviation="25" flood-color="#000" flood-opacity=".27"/>
    </filter>
    <filter id="halo" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="18"/>
    </filter>
    <style><![CDATA[
      .cn{{font-family:'PingFang SC','Microsoft YaHei','Noto Sans SC',Arial,sans-serif}}
      .mono{{font-family:'JetBrains Mono','SFMono-Regular',Menlo,monospace}}
    ]]></style>
  </defs>

  <rect width="1920" height="1080" fill="#071423"/>
  <rect width="1920" height="1080" fill="url(#glow)"/>
  <circle cx="1615" cy="528" r="460" fill="none" stroke="#72d2ff" stroke-opacity=".045" stroke-width="2"/>
  <circle cx="1615" cy="528" r="335" fill="none" stroke="#72d2ff" stroke-opacity=".06" stroke-width="2"/>

  <text x="116" y="113" class="cn" fill="#72d2ff" font-size="26" font-weight="700" letter-spacing="2.5">实践 02 · 一键生成</text>
  <rect x="116" y="141" width="112" height="5" rx="2.5" fill="#ffc17b"/>
  <text x="116" y="227" class="cn" fill="#f5f8fc" font-size="73" font-weight="760" letter-spacing="-2">把交付目标直接交给 Agent，会怎样？</text>
  <text x="119" y="285" class="cn" fill="#a9c3d4" font-size="28">不加限制、不再澄清，直接请求它完成整个实现。</text>

  <g filter="url(#shadow)">
    <rect x="116" y="329" width="1688" height="598" rx="30" fill="url(#panel)" stroke="#386079" stroke-width="2"/>
  </g>
  {body}
  <text x="116" y="1005" class="cn" fill="#88a1b8" font-size="21">AI 编码训练营 · 实践篇</text>
</svg>
'''


before = '''
  <text x="156" y="387" class="mono" fill="#7eaac0" font-size="21" letter-spacing="2">ONE PROMPT → FULL IMPLEMENTATION</text>
  <rect x="172" y="451" width="425" height="239" rx="24" fill="#112f45" stroke="#4e748b" stroke-width="1.8"/>
  <rect x="202" y="480" width="78" height="92" rx="12" fill="#1c4c62" stroke="#72d2ff" stroke-opacity=".65" stroke-width="2"/>
  <path d="M219 507h43M219 523h34M219 539h41" stroke="#a4e6ff" stroke-width="5" stroke-linecap="round" opacity=".75"/>
  <path d="M203 586h360M203 613h299M203 640h334" stroke="#4e7c93" stroke-width="7" stroke-linecap="round" opacity=".72"/>
  <text x="301" y="513" class="mono" fill="#72d2ff" font-size="20" letter-spacing="2">INPUT</text>
  <text x="301" y="555" class="cn" fill="#f5f8fc" font-size="36" font-weight="700">交付目标</text>

  <path d="M631 570h181" stroke="#72d2ff" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 13" opacity=".78"/>
  <path d="m799 555 17 15-17 15" fill="none" stroke="#72d2ff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="720" y="532" class="cn" fill="#8eb4c9" font-size="20" text-anchor="middle">直接输入</text>

  <circle cx="961" cy="566" r="118" fill="#72d2ff" opacity=".14" filter="url(#halo)"/>
  <circle cx="961" cy="566" r="114" fill="url(#agent)" stroke="#72d2ff" stroke-opacity=".65" stroke-width="2.5"/>
  <circle cx="961" cy="566" r="92" fill="none" stroke="#72d2ff" stroke-opacity=".29" stroke-width="2"/>
  <circle cx="961" cy="454" r="8" fill="#ffc17b"/>
  <circle cx="1054" cy="625" r="6" fill="#72d2ff"/>
  <circle cx="865" cy="628" r="6" fill="#72d2ff"/>
  <text x="961" y="576" class="mono" fill="#f5f8fc" font-size="43" font-weight="720" text-anchor="middle">Agent</text>
  <text x="961" y="613" class="cn" fill="#a3d7ea" font-size="19" text-anchor="middle">一次生成</text>

  <path d="M1108 570h181" stroke="#72d2ff" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 13" opacity=".78"/>
  <path d="m1276 555 17 15-17 15" fill="none" stroke="#72d2ff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="1200" y="532" class="cn" fill="#8eb4c9" font-size="20" text-anchor="middle">直接交付</text>

  <rect x="1325" y="451" width="425" height="239" rx="24" fill="#112f45" stroke="#4e748b" stroke-width="1.8"/>
  <rect x="1355" y="480" width="79" height="93" rx="12" fill="#314258" stroke="#ffc17b" stroke-opacity=".7" stroke-width="2"/>
  <text x="1394" y="544" class="mono" fill="#ffc17b" font-size="29" font-weight="700" text-anchor="middle">&#123; &#125;</text>
  <path d="M1356 586h360M1356 613h313M1356 640h337" stroke="#4e7c93" stroke-width="7" stroke-linecap="round" opacity=".72"/>
  <text x="1454" y="513" class="mono" fill="#ffc17b" font-size="20" letter-spacing="2">OUTPUT</text>
  <text x="1454" y="555" class="cn" fill="#f5f8fc" font-size="36" font-weight="700">全部代码</text>

  <path d="M727 755h466" stroke="#4c6c80" stroke-width="1.5"/>
  <text x="960" y="804" class="cn" fill="#e8f4fb" font-size="30" font-weight="580" text-anchor="middle">只输入目标、不约束过程，交付会怎样？</text>
'''


def card(x: int, y: int, number: str, title: str, detail: str, accent: str) -> str:
    return f'''
  <g>
    <rect x="{x}" y="{y}" width="484" height="178" rx="22" fill="#123249" stroke="#4a7188" stroke-width="1.7"/>
    <rect x="{x+23}" y="{y+22}" width="55" height="36" rx="10" fill="{accent}" fill-opacity=".12" stroke="{accent}" stroke-opacity=".42"/>
    <text x="{x+50}" y="{y+47}" class="mono" fill="{accent}" font-size="20" font-weight="700" text-anchor="middle">{number}</text>
    <circle cx="{x+444}" cy="{y+40}" r="6" fill="{accent}" fill-opacity=".75"/>
    <text x="{x+24}" y="{y+106}" class="cn" fill="#f5f8fc" font-size="31" font-weight="700">{title}</text>
    <text x="{x+25}" y="{y+149}" class="cn" fill="#b6cedd" font-size="23">{detail}</text>
  </g>'''


after = '''
  <text x="157" y="382" class="cn" fill="#c9e2ef" font-size="26" font-weight="650">一键生成后，重点检查这些问题</text>
  <rect x="1507" y="348" width="242" height="48" rx="24" fill="#3d342b" stroke="#9a7550" stroke-width="1.4"/>
  <circle cx="1536" cy="372" r="6" fill="#ffc17b"/>
  <text x="1555" y="380" class="cn" fill="#ffc17b" font-size="21" font-weight="600">可能出现的风险</text>
'''
after += card(156, 419, "01", "完全没有版本控制", "缺少可回溯的提交记录", "#72d2ff")
after += card(718, 419, "02", "项目结构不合适", "源码、测试与文档位置不清", "#72d2ff")
after += card(1280, 419, "03", "交付目录混杂", "构建产物混入交付目录", "#72d2ff")
after += card(156, 617, "04", "一次写完全部功能", "易出错，代码难审核、难维护", "#ffc17b")
after += card(718, 617, "05", "先写代码，再补测试", "测试可能迁就实现，只求变绿", "#ffc17b")
after += card(1280, 617, "…", "还有更多问题？", "留待现场演示继续观察", "#ffc17b")


(HERE / "one-click-before.svg").write_text(
    shell(before, "交付目标直接输入 Agent，一次生成全部代码的抽象流程；页面提问：只输入目标、不约束过程，交付会怎样？"),
    encoding="utf-8",
)
(HERE / "one-click-after.svg").write_text(
    shell(after, "点击按钮后揭示六类可能的问题：没有版本控制、结构不合适、交付目录混杂、一次写完全部功能、先写代码再补测试，以及现场演示中待观察的其他问题。"),
    encoding="utf-8",
)
