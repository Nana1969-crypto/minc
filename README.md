# ROUANET 31/10: Kit de Emergência do Primeiro Projeto

Produto digital de baixo ticket (R$ 37) para quem vai apresentar o **primeiro projeto** na Lei Rouanet e precisa organizar a proposta antes do prazo de **31/10/2026**.
Base normativa: Lei 8.313/1991, Decreto 11.453/2023 e **IN MinC nº 29/2026** (verificação em 25/09/2026).

> Material de organização e conferência. **Não garante aprovação nem captação** e não substitui análise profissional.

## O que está aqui

| Caminho | Conteúdo |
|---|---|
| `produto/ROUANET-31-10-Checklist-de-Emergencia.pdf` | PDF principal (61 páginas A4) |
| `produto/ROUANET-31-10-Planilhas.xlsx` | Planilhas em branco: Mapa do Projeto, Orçamento, Cronograma, Distribuição, Radar de Limites (calculadoras A–J), Matriz de Consistência, Checklists (Salic, documentos, final) e Controle Normativo |
| `produto/ROUANET-31-10-Planilhas-EXEMPLO.xlsx` | A mesma planilha preenchida com um projeto fictício |
| `ENTREGA-COMPLETA.md` | Documento-mestre: conceito, promessa, mecanismo, avatar, índice, resumos, Radar, checklists, planilhas, fórmulas, calculadoras, plano de 72 h, página de vendas, anúncios, criativos, FAQ, disclaimer, fontes, controle normativo e as 5 auditorias |
| `normas/BASE-NORMATIVA.md` | Tabela de regras (percentual, base de cálculo, sujeitos, exceções, dispositivo, link) e pendências de verificação |
| `fonte/` | Scripts que geram o PDF e as planilhas |

## Como regenerar

```bash
pip install openpyxl playwright
python3 fonte/build_xlsx.py   # gera as duas planilhas em produto/
python3 fonte/build_pdf.py    # gera o PDF em produto/ (usa Chromium)
```

- Limites normativos das planilhas: aba `PARAMETROS` (e o dicionário `params` em `fonte/build_xlsx.py`).
- Texto do PDF: `fonte/conteudo.py`. Checklist final (compartilhado com a planilha): `fonte/checklist_final.py`.
- Fontes tipográficas: Inter e Archivo Black (SIL Open Font License), em `fonte/fonts/`.
