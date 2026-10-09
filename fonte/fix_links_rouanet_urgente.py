"""Padroniza e completa os links oficiais de um PDF do guia Rouanet Urgente.
Uso: python3 -I fix_links.py entrada.pdf saida.pdf"""
import sys, pymupdf as fitz

IN29 = "https://www.gov.br/cultura/pt-br/acesso-a-informacao/legislacao-e-normativas/instrucao-normativa-minc-no-29-de-29-de-janeiro-de-2026"
LEI = "https://www.planalto.gov.br/ccivil_03/leis/l8313cons.htm"
LEI_COMPILADA = "https://www.planalto.gov.br/ccivil_03/leis/l8313compilada.htm"
PORTAL = "https://www.gov.br/cultura/pt-br/assuntos/lei-rouanet"
# A página "marcas-do-pronac" (Manuais e marcas) exige login no gov.br; usar o PDF público do manual.
MANUAIS = "https://www.gov.br/cultura/pt-br/centrais-de-conteudo/marcas-e-logotipos/marcas-rouanet/ManualdoProponenteIN2026DEFINITIVO2.pdf"
SALIC = "https://salic.cultura.gov.br/"

def remap(uri):
    u = uri or ""
    if "gamma.app" in u: return None
    if "planalto.gov.br" in u and "8313" in u: return LEI
    if "lei-rouanet-1" in u: return PORTAL
    if "ManualdoProponente" in u or "marcas-do-pronac" in u: return MANUAIS
    if "instrucao-normativa-minc-no-29" in u: return IN29
    if "salic.cultura.gov.br" in u: return SALIC
    return u

# frase visível -> destino (ordem importa: frases mais longas primeiro)
PHRASES = [
    ("https://www.planalto.gov.br/ccivil_03/leis/l8313compilada.htm", LEI_COMPILADA),
    ("https://salic.cultura.gov.br", SALIC),
    ("Instrução Normativa MinC nº 29, de 29 de janeiro de 2026", IN29),
    ("Instrução Normativa MinC nº 29/2026", IN29),
    ("IN MinC nº 29/2026", IN29),
    ("Anexo II", IN29),
    ("Lei nº 8.313/1991", LEI),
    ("Portal oficial da Lei Rouanet", PORTAL),
    ("Portal da Lei Rouanet", PORTAL),
    ("Salic — Sistema de Apoio às Leis de Incentivo à Cultura", SALIC),
    ("SALIC — Sistema de Apoio às Leis de Incentivo à Cultura", SALIC),
    ("Manual do Proponente", MANUAIS),
    ("Proponente/Manual de Apresentação de Propostas", MANUAIS),
    ("Manual/orientações oficiais", MANUAIS),
    ("manual oficial", MANUAIS),
    ("e o Manual", MANUAIS),
]

def line_rect(page, r):
    """Se a frase está numa linha curta (rótulo de lista), devolve a linha inteira."""
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            lb = fitz.Rect(l["bbox"])
            if lb.contains(fitz.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)):
                txt = "".join(s["text"] for s in l["spans"]).strip()
                return lb if len(txt) <= 90 else r
    return r

def main(src, dst):
    d = fitz.open(src)
    changed = added = 0
    for p in d:
        for l in p.get_links():
            new = remap(l.get("uri"))
            if new and new != l.get("uri"):
                l["uri"] = new; p.update_link(l); changed += 1
        covered = [fitz.Rect(l["from"]) for l in p.get_links() if "gamma.app" not in (l.get("uri") or "")]
        for phrase, uri in PHRASES:
            for r in p.search_for(phrase):
                if any(r.intersects(c) for c in covered):
                    continue
                rr = line_rect(p, r) if phrase[0].isupper() and len(phrase) > 15 else r
                if any(rr.intersects(c) for c in covered):
                    rr = r
                p.insert_link({"kind": fitz.LINK_URI, "from": rr, "uri": uri})
                covered.append(rr); added += 1
    d.save(dst, garbage=3, deflate=True)
    print(f"{src}: {changed} links corrigidos, {added} links novos")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
