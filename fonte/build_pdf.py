# -*- coding: utf-8 -*-
"""
Gera o PDF principal do kit ROUANET 31/10 a partir de HTML (Chromium/Playwright).

Uso:
    python3 fonte/build_pdf.py
Saída:
    produto/ROUANET-31-10-Checklist-de-Emergencia.pdf
    fonte/_build/rouanet-31-10.html (HTML intermediário)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from checklist_final import ITENS  # noqa: E402
from conteudo import PAGES  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BUILD = os.path.join(HERE, "_build")
OUT = os.path.join(ROOT, "produto", "ROUANET-31-10-Checklist-de-Emergencia.pdf")
FONTS = os.path.join(HERE, "fonts")

CSS = """
@font-face { font-family: 'Inter'; font-weight: 400; src: url('file://%(f)s/inter-latin-400-normal.woff2'); }
@font-face { font-family: 'Inter'; font-weight: 600; src: url('file://%(f)s/inter-latin-600-normal.woff2'); }
@font-face { font-family: 'Inter'; font-weight: 800; src: url('file://%(f)s/inter-latin-800-normal.woff2'); }
@font-face { font-family: 'Archivo Black'; src: url('file://%(f)s/archivo-black-latin-400-normal.woff2'); }
:root {
  --navy: #1F2A44; --orange: #E85D04; --ink: #1d2433; --muted: #5b6477; --line: #d9dee7;
  --blue: #2563eb; --blue-bg: #eaf1ff; --green: #15803d; --green-bg: #e8f6ec;
  --red: #c0262d; --red-bg: #fdecec; --yellow: #a16207; --yellow-bg: #fff6d6; --paper: #ffffff; --soft: #f5f7fa;
}
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--paper); color: var(--ink);
  font-family: 'Inter', 'Liberation Sans', sans-serif; font-size: 10.2pt; line-height: 1.45; }
.page { width: 210mm; height: 297mm; padding: 20mm 16mm 18mm 16mm; position: relative; overflow: hidden; page-break-after: always; }
.page:last-child { page-break-after: auto; }
.runhead { position: absolute; top: 8mm; left: 16mm; right: 16mm; display: flex; justify-content: space-between;
  font-size: 7.5pt; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); border-bottom: 1px solid var(--line); padding-bottom: 2mm; }
.runhead b { color: var(--orange); }
.foot { position: absolute; bottom: 7mm; left: 16mm; right: 16mm; display: flex; justify-content: space-between; font-size: 7.5pt; color: var(--muted); }
h1, h2, h3 { font-family: 'Archivo Black', 'Inter', sans-serif; font-weight: 400; color: var(--navy); margin: 0 0 3mm 0; line-height: 1.12; }
h1 { font-size: 24pt; } h2 { font-size: 16pt; margin-top: 2mm; } h3 { font-size: 11.5pt; margin-top: 3mm; }
p { margin: 0 0 2.5mm 0; }
.kicker { font-size: 8pt; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; color: var(--orange); margin-bottom: 1.5mm; }
.lead { font-size: 11.5pt; color: var(--muted); }
.box { border-radius: 3mm; padding: 3.2mm 4mm; margin: 0 0 3mm 0; border-left: 2.2mm solid; break-inside: avoid; }
.box .t { font-weight: 800; font-size: 8.4pt; letter-spacing: .1em; text-transform: uppercase; margin-bottom: 1.2mm; }
.box ul, .box ol { margin: 0; padding-left: 5mm; } .box li { margin-bottom: .8mm; }
.box p:last-child { margin-bottom: 0; }
.what { background: var(--blue-bg); border-color: var(--blue); } .what .t { color: var(--blue); }
.do { background: var(--green-bg); border-color: var(--green); } .do .t { color: var(--green); }
.wrong { background: var(--red-bg); border-color: var(--red); } .wrong .t { color: var(--red); }
.warn { background: var(--yellow-bg); border-color: #d99a00; } .warn .t { color: var(--yellow); }
.check { background: #fff; border: 1.2px solid var(--navy); border-left: 2.2mm solid var(--orange); } .check .t { color: var(--navy); }
.check ul { list-style: none; padding-left: 0; } .check li { padding-left: 6mm; text-indent: -6mm; }
.check li::before { content: "☐  "; font-size: 11pt; color: var(--orange); }
.new { display: inline-block; background: var(--orange); color: #fff; font-weight: 800; font-size: 7.4pt; letter-spacing: .06em;
  padding: .6mm 2mm; border-radius: 1.2mm; margin: 0 1mm 1mm 0; }
.pill { display: inline-block; white-space: nowrap; align-self: start; border-radius: 10mm; padding: .5mm 2.4mm; font-size: 8pt; font-weight: 800; }
.p-red { background: var(--red-bg); color: var(--red); } .p-yel { background: var(--yellow-bg); color: var(--yellow); } .p-grn { background: var(--green-bg); color: var(--green); }
table { width: 100%%; border-collapse: collapse; margin: 0 0 3mm 0; font-size: 8.4pt; break-inside: auto; }
th { background: var(--navy); color: #fff; text-align: left; padding: 1.6mm 2mm; font-weight: 800; font-size: 7.8pt; vertical-align: bottom; }
td { border-bottom: 1px solid var(--line); padding: 1.5mm 2mm; vertical-align: top; }
tr:nth-child(even) td { background: var(--soft); }
table.compact td, table.compact th { padding: 1.1mm 1.6mm; font-size: 7.9pt; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3mm; }
.muted { color: var(--muted); } .small { font-size: 8.3pt; } .tiny { font-size: 7.4pt; }
.big { font-size: 13pt; font-weight: 800; color: var(--navy); }
.rule { font-family: 'Archivo Black'; font-size: 15pt; color: #fff; background: var(--navy); padding: 5mm 6mm; border-radius: 3mm; margin: 3mm 0; line-height: 1.25; }
.rule small { display: block; font-family: 'Inter'; font-size: 9pt; color: #c9d2e3; margin-top: 2mm; }
.field { border: 1px solid var(--line); border-radius: 2mm; padding: 2mm 3mm; margin-bottom: 2.2mm; break-inside: avoid; }
.field .lab { font-weight: 800; color: var(--navy); font-size: 8.8pt; }
.field .hint { color: var(--muted); font-size: 7.8pt; }
.field .lines { height: 17mm; background: repeating-linear-gradient(transparent, transparent 5.6mm, #cfd6e2 5.6mm, #cfd6e2 5.9mm); margin-top: 1mm; }
.field .lines.l3 { height: 35mm; }
.step { display: flex; gap: 3mm; align-items: stretch; margin-bottom: 1.6mm; break-inside: avoid; }
.step .n { flex: 0 0 9mm; height: 9mm; border-radius: 50%%; background: var(--orange); color: #fff; font-family: 'Archivo Black'; font-size: 11pt;
  display: flex; align-items: center; justify-content: center; }
.step .c { flex: 1; border: 1px solid var(--line); border-radius: 2mm; padding: 1.4mm 3mm; font-size: 8.6pt; }
.step .c b { color: var(--navy); }
.salicmap { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm; }
.sm { border-radius: 2mm; padding: 2mm 2.5mm; border: 1.2px solid var(--navy); background: #fff; font-size: 8pt; position: relative; min-height: 19mm; }
.sm .n { font-family: 'Archivo Black'; color: var(--orange); font-size: 13pt; line-height: 1; }
.sm .h { font-weight: 800; color: var(--navy); font-size: 8.8pt; margin: .6mm 0; }
.sm.phase-a { border-color: #64748b; } .sm.phase-b { border-color: var(--blue); } .sm.phase-c { border-color: var(--green); } .sm.phase-d { border-color: var(--orange); }
.legend span { display: inline-block; margin-right: 4mm; font-size: 8pt; }
.legend i { display: inline-block; width: 3mm; height: 3mm; border-radius: .6mm; margin-right: 1mm; vertical-align: -0.3mm; }
.cover { background: var(--navy); color: #fff; padding: 24mm 18mm; }
.cover h1 { color: #fff; font-size: 54pt; letter-spacing: -.01em; margin-top: 14mm; }
.cover .sub { font-size: 17pt; font-family: 'Archivo Black'; color: var(--orange); line-height: 1.2; margin: 3mm 0 8mm 0; }
.cover .desc { font-size: 12.5pt; color: #dfe5f0; max-width: 150mm; }
.cover .tag { position: absolute; left: 18mm; bottom: 20mm; right: 18mm; font-size: 8.5pt; color: #a9b4c9; border-top: 1px solid #3b4866; padding-top: 4mm; }
.cover .date { display: inline-block; border: 2px solid var(--orange); color: var(--orange); font-family: 'Archivo Black'; padding: 2mm 4mm; border-radius: 2mm; font-size: 12pt; }
.cover .chips span { display: inline-block; border: 1px solid #54627f; border-radius: 10mm; padding: 1mm 3.5mm; margin: 0 1.5mm 1.5mm 0; font-size: 8.5pt; color: #dfe5f0; }
.divider { background: var(--navy); color: #fff; }
.divider h1 { color: #fff; font-size: 34pt; margin-top: 60mm; }
.divider .num { font-family: 'Archivo Black'; color: var(--orange); font-size: 90pt; line-height: 1; }
.divider p { color: #dfe5f0; font-size: 12.5pt; max-width: 150mm; }
.divider .runhead, .divider .foot { color: #8f9bb3; border-color: #3b4866; }
.flow { display: flex; flex-wrap: wrap; gap: 1.6mm; align-items: center; margin: 1mm 0 3mm; font-size: 8pt; }
.flow span { background: var(--soft); border: 1px solid var(--line); border-radius: 1.5mm; padding: 1mm 2mm; font-weight: 600; }
.flow em { color: var(--orange); font-style: normal; font-weight: 800; }
.radar { border: 1.2px solid var(--line); border-radius: 3mm; padding: 3mm 4mm; margin-bottom: 3mm; break-inside: avoid; }
.radar h3 { margin: 0 0 1.5mm 0; }
.radar .row { display: grid; grid-template-columns: 31mm 1fr; gap: 2mm; margin-bottom: 1mm; font-size: 8.5pt; }
.checkcols { columns: 2; column-gap: 6mm; }
.fc { display: grid; grid-template-columns: 8mm 1fr 34mm; column-gap: 3mm; font-size: 8.8pt; border-bottom: 1px solid var(--line); padding: 1.7mm 0; break-inside: avoid; }
.fc .opts { color: var(--muted); white-space: nowrap; }
.fc-h { font-weight: 800; color: var(--orange); font-size: 8.4pt; margin: 2mm 0 .6mm; letter-spacing: .06em; }
.toc a { color: inherit; text-decoration: none; }
.toc .l { display: flex; justify-content: space-between; border-bottom: 1px dotted var(--line); padding: 1.3mm 0; font-size: 9.3pt; }
.toc .l b { color: var(--navy); } .toc .m { color: var(--orange); font-weight: 800; margin-right: 2mm; }
.two-col-list { columns: 2; column-gap: 6mm; }
"""


def page_ranges():
    """Substitui @@P:mod1|mod2@@ pelo intervalo de páginas desses módulos."""
    import re
    def rng(m):
        keys = m.group(1).split("|")
        nums = [i for i, pg in enumerate(PAGES, start=1) if pg.get("mod") in keys]
        if not nums:
            return "—"
        return str(nums[0]) if nums[0] == nums[-1] else f"{nums[0]}–{nums[-1]}"
    for pg in PAGES:
        pg["html"] = re.sub(r"@@P:(.+?)@@", rng, pg["html"])


def render_html():
    page_ranges()
    body = []
    total = len(PAGES)
    for i, pg in enumerate(PAGES, start=1):
        cls = pg.get("cls", "")
        head = "" if "cover" in cls else (
            f'<div class="runhead"><span><b>ROUANET 31/10</b> · Checklist de Emergência</span><span>{pg.get("mod", "")}</span></div>'
            f'<div class="foot"><span>Material de organização. Não garante aprovação nem captação. Base: IN MinC nº 29/2026 — verificação em 25/09/2026.</span><span>{i}/{total}</span></div>')
        body.append(f'<section class="page {cls}">{head}{pg["html"]}</section>')
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>ROUANET 31/10 — Checklist de Emergência</title>
<style>{CSS % {"f": FONTS}}</style></head><body>{''.join(body)}</body></html>"""


def main():
    os.makedirs(BUILD, exist_ok=True)
    html_path = os.path.join(BUILD, "rouanet-31-10.html")
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(render_html())
    from playwright.sync_api import sync_playwright
    exe = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
        pg = b.new_page()
        pg.goto("file://" + html_path)
        pg.wait_for_timeout(600)
        pg.pdf(path=OUT, format="A4", print_background=True, prefer_css_page_size=True)
        b.close()
    print(OUT, "páginas:", len(PAGES))


if __name__ == "__main__":
    main()
