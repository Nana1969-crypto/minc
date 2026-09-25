# -*- coding: utf-8 -*-
"""Conteúdo do PDF ROUANET 31/10. Cada item de PAGES vira uma página A4."""
from checklist_final import ITENS

# ------------------------------------------------------------------ links oficiais
L_IN29 = "https://www.gov.br/cultura/pt-br/acesso-a-informacao/legislacao-e-normativas/instrucao-normativa-minc-no-29-de-29-de-janeiro-de-2026"
L_LEI = "https://www.planalto.gov.br/ccivil_03/leis/l8313cons.htm"
L_DEC = "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11453.htm"
L_MANUAL = "https://www.gov.br/cultura/pt-br/centrais-de-conteudo/marcas-e-logotipos/marcas-rouanet/ManualdoProponenteIN2026DEFINITIVO2.pdf"
L_APRESENTE = "https://www.gov.br/cultura/pt-br/assuntos/lei-rouanet/textos/apresente-seu-projeto"
L_QUEM = "https://www.gov.br/cultura/pt-br/assuntos/lei-rouanet/textos/quem-pode-participar-do-mecanismo-da-lei-rouanet"
L_NOTICIA = "https://www.gov.br/cultura/pt-br/assuntos/noticias/ministerio-da-cultura-moderniza-instrucao-normativa-da-lei-rouanet"
L_NOT_ACESS = "https://www.gov.br/cultura/pt-br/assuntos/noticias/minc-moderniza-gestao-da-instrucao-normativa-da-lei-rouanet-com-novas-regras-para-acessibilidade-e-nacionalizacao-dos-incentivos-fiscais"
L_SALIC = "https://salic.cultura.gov.br"
L_CONSULTA = "https://www.gov.br/participamaisbrasil/lei-rouanet-instrucao-normativa-do-mecanismo-incentivo-a-projetos-culturais-2026"
L_IN23 = "https://www.gov.br/cultura/pt-br/acesso-a-informacao/legislacao-e-normativas/instrucao-normativa-minc-no-23-de-5-de-fevereiro-de-2025"

NEW = '<span class="new">ATENÇÃO: REGRA ATUALIZADA EM 2026</span>'
FONTE_IN = "IN MinC nº 29/2026 (localize o dispositivo no texto oficial)"


# ------------------------------------------------------------------ helpers
def box(kind, t, inner):
    return f'<div class="box {kind}"><div class="t">{t}</div>{inner}</div>'


def ul(items, ordered=False):
    tag = "ol" if ordered else "ul"
    return f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"


def check(t, items):
    return box("check", t, ul(items))


def table(headers, rows, cls=""):
    h = "".join(f"<th>{x}</th>" for x in headers)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def chapter(o_que_e, fazer, errado, checklist, check_title="CHECKLIST"):
    """Estrutura obrigatória: O QUE É → O QUE FAZER → O QUE PODE DAR ERRADO → CHECKLIST."""
    return (box("what", "① O que é", o_que_e) + box("do", "② O que você precisa fazer", fazer)
            + box("wrong", "③ O que pode dar errado", errado) + check(f"④ {check_title}", checklist))


def P(mod, html, cls=""):
    return {"mod": mod, "html": html, "cls": cls}


def divider(num, title_, text, mod):
    return P(mod, f'<div class="num">{num}</div><h1>{title_}</h1><p>{text}</p>', "divider")


def field(lab, hint, lines=2):
    return f'<div class="field"><div class="lab">{lab}</div><div class="hint">{hint}</div><div class="lines {"l3" if lines == 3 else ""}"></div></div>'


PAGES = []
add = PAGES.append

# =================================================================== CAPA
add(P("", f"""
<div class="kicker" style="color:#E85D04">Kit de execução · primeiro projeto · Lei Rouanet</div>
<h1>ROUANET<br>31/10</h1>
<div class="sub">O Checklist de Emergência para o<br>Seu Primeiro Projeto</div>
<p class="desc">Um passo a passo prático para organizar sua proposta, conferir os principais limites e preparar seu cadastro no Salic antes do prazo.</p>
<p style="margin-top:10mm"><span class="date">PRAZO DE APRESENTAÇÃO: 31/10/2026</span></p>
<div class="chips" style="margin-top:8mm"><span>Mapa do Projeto</span><span>Mapa do Salic</span><span>Radar de Zona de Perigo</span><span>7 planilhas + calculadoras</span><span>Checklist final com 54 verificações</span><span>Plano de 72 horas</span></div>
<div class="tag">Baseado na Lei nº 8.313/1991, no Decreto nº 11.453/2023 e na Instrução Normativa MinC nº 29/2026. Última verificação normativa: 25/09/2026.
Este material organiza, orienta e ajuda a reduzir erros operacionais. Ele <b>não</b> garante aprovação do projeto, <b>não</b> garante captação de recursos e <b>não</b> substitui análise profissional individualizada.</div>
""", "cover"))

# =================================================================== SEGURANÇA
add(P("Antes de começar", f"""
<div class="kicker">Leia primeiro · 2 minutos</div>
<h1>Como usar este material com segurança</h1>
<div class="grid2">
{box("what", "O que este kit faz", ul(["Organiza a sua proposta em uma ordem lógica.", "Mostra o que preparar antes de abrir o Salic.", "Confere os principais limites com a base de cálculo certa.", "Aponta riscos comuns de iniciantes antes do envio."]))}
{box("wrong", "O que este kit NÃO faz", ul(["Não garante aprovação pelo Ministério da Cultura.", "Não garante captação de recursos.", "Não substitui a leitura da norma nem a análise profissional do seu caso.", "Não substitui o Manual do Proponente oficial."]))}
</div>
{box("warn", "Legislação muda. Siga estas 4 regras", ul([
    "Este material foi montado com base nas normas vigentes na data de verificação indicada abaixo.",
    "Antes de enviar, abra o texto oficial da IN MinC nº 29/2026 e confira os números que você usou. Se houver diferença, <b>vale sempre a norma oficial</b>.",
    "Material de anos anteriores (IN 1/2023, IN 11/2024, IN 23/2025, vídeos e cursos antigos) pode estar desatualizado. Veja a tabela da página seguinte.",
    "Na planilha, todos os limites ficam na aba <b>PARAMETROS</b>. Se a norma mudar, altere ali e as calculadoras se atualizam.",
], True))}
<h3>ÚLTIMA VERIFICAÇÃO NORMATIVA</h3>
{table(["Data", "Norma consultada", "Versão", "Alterações relevantes"], [
    ["25/09/2026", "Instrução Normativa MinC nº 29/2026", "29/01/2026, publicada no DOU em 30/01/2026", "Revogou a IN MinC nº 23/2025. Novos limites por proponente, documentos na apresentação, acessibilidade reforçada, execução em até 36 meses."],
    ["25/09/2026", "Lei nº 8.313/1991", "texto compilado", "Base legal do Pronac (arts. 18 e 26: enquadramento do incentivo)."],
    ["25/09/2026", "Decreto nº 11.453/2023", "vigente", "Regulamenta os mecanismos de fomento do Pronac."],
    ["25/09/2026", "Manual do Proponente — IN 2026", "publicado pelo MinC", "Passo a passo do Salic (telas e campos)."],
    ["___/___/2026", "Sua conferência:", "", "Anote aqui a data em que você abriu o texto oficial."],
], "compact")}
<p class="small"><b>Links oficiais:</b> IN 29/2026: <span class="tiny">{L_IN29}</span><br>
Manual do Proponente IN 2026: <span class="tiny">{L_MANUAL}</span><br>
Lei 8.313/1991: <span class="tiny">{L_LEI}</span> · Decreto 11.453/2023: <span class="tiny">{L_DEC}</span> · Salic: <span class="tiny">{L_SALIC}</span></p>
"""))

# =================================================================== ORDEM
steps = [
    ("Leia o mapa", "Tabela de regras 2026, os 6 valores que não são sinônimos e a tabela-mestra de limites."),
    ("Faça o diagnóstico", "Módulo 1 + checklist <b>“Posso começar?”</b>."),
    ("Preencha o Mapa do Projeto", "Módulo 2 + aba <b>MAPA DO PROJETO</b> da planilha."),
    ("Monte o orçamento", "Módulo 4 + aba <b>ORÇAMENTO</b>. Regra de ouro: sem justificativa, sem despesa."),
    ("Monte o cronograma", "Módulo 7 + aba <b>CRONOGRAMA</b>."),
    ("Passe pelo Radar de Zona de Perigo", "Módulo 5 + aba <b>RADAR DE LIMITES</b>. Zere os 🔴."),
    ("Faça o checklist", "Módulos 6, 8 e 9 + abas de checklist."),
    ("Entre no Salic", "Com tudo pronto em mãos. Use o <b>Mapa do Salic</b> (Módulo 3)."),
    ("Preencha", "Copie do Mapa do Projeto e da planilha. Nada de escrever do zero no sistema."),
    ("Revise", "Checklist final: zero “NÃO”. Pendências do Salic zeradas."),
    ("Envie", "Antes do último dia. Salve o comprovante."),
]
add(P("Comece aqui", f"""
<div class="kicker">Página mais importante do kit</div>
<h1>Se você nunca apresentou um projeto, faça nesta ordem:</h1>
<p class="lead">Não pule etapas. Não abra o Salic antes do passo 8.</p>
{''.join(f'<div class="step"><div class="n">{i}</div><div class="c"><b>{a}</b> — {b}</div></div>' for i, (a, b) in enumerate(steps, 1))}
<div class="rule">31/10/2026 cai num SÁBADO.<small>Não conte com prorrogação nem com o sistema tranquilo no último dia. Meta deste kit: enviar até <b>quarta-feira, 28/10/2026</b>. Confirme o prazo no site do MinC: a IN prevê a apresentação de propostas entre 1º de fevereiro e 31 de outubro.</small></div>
"""))

# =================================================================== ÍNDICE
toc = [
    ("", "Como usar com segurança · Ordem de execução", "@@P:Antes de começar|Comece aqui@@"),
    ("", "Regras que você não deve copiar de materiais antigos", "@@P:Atualização 2026@@"),
    ("", "Os 6 valores que não são sinônimos · Tabela-mestra de limites", "@@P:Conceitos-chave|Tabela-mestra@@"),
    ("M1", "Primeiro: descubra se você está pronto", "@@P:Módulo 1 · Posso começar?@@"),
    ("M2", "Transforme sua ideia em projeto + MAPA DO PROJETO", "@@P:Módulo 2 · Ideia → projeto@@"),
    ("M3", "O caminho dentro do Salic + MAPA DO SALIC", "@@P:Módulo 3 · Salic@@"),
    ("M4", "Orçamento sem cair nas armadilhas", "@@P:Módulo 4 · Orçamento@@"),
    ("M5", "Radar de Zona de Perigo (14 riscos)", "@@P:Módulo 5 · Radar de Zona de Perigo@@"),
    ("M6", "Acessibilidade e democratização do acesso", "@@P:Módulo 6 · Acessibilidade e democratização@@"),
    ("M7", "Cronograma que o orçamento consegue pagar", "@@P:Módulo 7 · Cronograma@@"),
    ("M8", "Documentação da apresentação", "@@P:Módulo 8 · Documentação@@"),
    ("M9", "Checklist final “Antes de clicar em enviar”", "@@P:Módulo 9 · Checklist final@@"),
    ("", "As planilhas e as calculadoras (como usar)", "@@P:Ferramentas@@"),
    ("", "12 erros concretos que derrubam iniciantes", "@@P:Erros concretos@@"),
    ("", "Desafio de 72 horas: Dia 1 · Dia 2 · Dia 3", "@@P:Desafio de 72 horas@@"),
    ("", "Fontes oficiais · Controle de atualização · Aviso legal", "@@P:Fontes e controle@@"),
]
add(P("Índice", f"""
<div class="kicker">Índice</div><h1>O que tem neste kit</h1>
<div class="toc">{''.join(f'<div class="l"><span><span class="m">{m}</span><b>{t}</b></span><span>{p}</span></div>' for m, t, p in toc)}</div>
<h3>Estrutura de cada capítulo</h3>
<div class="flow"><span>① O QUE É</span><em>→</em><span>② O QUE VOCÊ PRECISA FAZER</span><em>→</em><span>③ O QUE PODE DAR ERRADO</span><em>→</em><span>④ CHECKLIST</span></div>
<h3>Ferramentas que acompanham o PDF</h3>
{table(["Arquivo", "Para que serve"], [
    ["ROUANET-31-10-Planilhas.xlsx", "Versão em branco: Mapa do Projeto, Orçamento, Cronograma, Distribuição, Radar de Limites, Matriz de Consistência, Checklists (Salic, documentos, final) e Controle Normativo. Abre no Excel e no Google Sheets."],
    ["ROUANET-31-10-Planilhas-EXEMPLO.xlsx", "A mesma planilha preenchida com um projeto fictício, para você ver os alertas 🔴🟡🟢 funcionando."],
], "compact")}
<p class="small muted">Prioridade deste material: praticidade &gt; teoria · checklist &gt; texto longo · ferramenta &gt; explicação · ação &gt; conceito · clareza &gt; juridiquês.</p>
"""))

# =================================================================== REGRAS ANTIGAS
add(P("Atualização 2026", f"""
<div class="kicker">Tabela inicial obrigatória</div>
<h1>REGRAS QUE VOCÊ NÃO DEVE COPIAR DE MATERIAIS ANTIGOS</h1>
<p>A IN MinC nº 29/2026 revogou a IN MinC nº 23/2025. Vídeos, modelos e cursos antigos podem estar usando regras que já mudaram. {NEW}</p>
{table(["O que o material antigo diz", "O que vale em 2026 (IN 29/2026)", "Por que confunde"], [
    ["Pessoa jurídica pode ter até 16 projetos ativos; havia limite separado para optantes do Simples.", "Demais pessoas jurídicas: até <b>10</b> projetos ativos, teto global de <b>R$ 15 milhões</b>. Não há mais limite apartado para o Simples.", "Número mudou e categoria sumiu."],
    ["Limites de pessoa física e MEI de anos anteriores.", "PF: até <b>2</b> projetos ativos, teto global <b>R$ 500 mil</b>. MEI: até <b>4</b> projetos ativos, teto global <b>R$ 1,5 milhão</b>.", "Tetos globais por tipo de proponente."],
    ["A comprovação de atuação cultural podia vir automaticamente após a prestação de contas do 1º projeto.", "A habilitação passa a ser via <b>portfólio no Salic</b>. Primeiro projeto até <b>R$ 200 mil</b>: dispensa de comprovar atuação (leia a regra completa no Módulo 1).", "Muita gente acha que “o sistema resolve sozinho”."],
    ["Dava para mandar documento obrigatório depois de apresentar a proposta.", "Documentos obrigatórios devem estar anexados <b>na apresentação</b>.", "Deixar para depois agora é risco de a proposta não seguir."],
    ["Era preciso apresentar a proposta com antecedência mínima de 30 dias do início da execução.", "A exigência de antecedência mínima de 30 dias <b>foi retirada</b>.", "Muitos cronogramas antigos são montados com esse “respiro”."],
    ["Prazo de execução livre ou regras antigas de prorrogação.", "Projetos cadastrados com prazo <b>máximo de 36 meses</b> de execução, ajustado à realidade.", "Cronogramas longos demais."],
    ["Custos de administração: não concentrar mais de 50% em uma única despesa.", "Essa trava <b>caiu</b>. Regularização documental de bens de patrimônio passou a ser admitida como custo de administração.", "Continua o limite de 15% do valor do projeto."],
    ["Logomarca do Vale-Cultura obrigatória em atividades permanentes.", "Deixou de ser obrigatória. As marcas da Lei Rouanet, do MinC e do Governo Federal passam a ser obrigatórias também na comunicação de terceiros ligada ao projeto.", "Plano de divulgação e peças gráficas."],
    ["Cachê limitado a R$ 3 mil por artista (regra de 2019).", "Solo até <b>R$ 25 mil</b>, grupo até <b>R$ 50 mil</b>, músico de orquestra até <b>R$ 5 mil</b>, maestro até <b>R$ 25 mil</b>, palestrante até <b>R$ 5 mil</b> (valores por apresentação/participação; acima disso, outras fontes ou CNIC).", "Ainda circula muito na internet."],
    ["Divulgação podia chegar a 30% em certas regiões.", "Divulgação/comunicação: limite de <b>20% do valor do projeto</b>, segundo a redação encontrada da IN 29/2026. Confira no texto oficial se há alguma exceção regional.", "Regra regional antiga ainda aparece em materiais."],
    ["Acessibilidade como “parágrafo padrão”.", "Nenhum projeto deve seguir sem medidas de acessibilidade física, comunicacional e atitudinal. Consultor/coordenador de acessibilidade e equipe treinada entram nos custos.", "Texto genérico agora é risco alto."],
], "compact")}
<p class="tiny muted">Fontes: publicações que reproduzem o texto da IN MinC nº 29/2026 e comunicados oficiais do MinC sobre a norma (links na página “Fontes oficiais”). Onde a redação não pôde ser confirmada literalmente, o kit indica “confira no texto oficial”.</p>
"""))

# =================================================================== 6 VALORES
add(P("Conceitos-chave", f"""
<div class="kicker">Nunca trate estes termos como sinônimos</div>
<h1>Os 6 valores que confundem iniciantes</h1>
<p>A maior fonte de erro de cálculo é usar a base errada. Cada limite tem a sua <b>base de cálculo</b>. Grave esta página.</p>
{table(["Termo", "O que é, na prática", "É base de quê?"], [
    ["<b>VALOR DO PROJETO</b>", "O valor que você solicita via incentivo fiscal (Rouanet) para executar o projeto, conforme a definição da IN. No Salic, é o valor que o sistema calcula a partir do seu orçamento.", "Administração (15%), divulgação (20%), acessibilidade/comunicação/divulgação acessíveis (20%), captação (10%, teto R$ 150 mil)."],
    ["<b>VALOR TOTAL DO PROJETO</b>", "Tudo o que o projeto custa, somando incentivo + outras fontes (patrocínio direto, recursos próprios, apoio de parceiros).", "Visão geral de viabilidade. Para a dispensa de iniciante (R$ 200 mil), o kit recomenda, por prudência, conferir os dois valores."],
    ["<b>VALOR CAPTADO</b>", "O dinheiro que efetivamente entrou na conta do projeto vindo de incentivadores. Só existe DEPOIS da captação. Pode ser menor que o valor do projeto.", "Remuneração do proponente (20% ou 30%) e limite por fornecedor (20%)."],
    ["<b>CUSTOS VINCULADOS</b>", "Despesas de suporte do projeto que a norma agrupa e limita: custos de administração e custos de acessibilidade, comunicação e divulgação acessíveis. São gastos proporcionalmente à captação.", "Cada um tem seu limite sobre o VALOR DO PROJETO."],
    ["<b>REMUNERAÇÃO DO PROPONENTE</b>", "Pagamento ao próprio proponente por um SERVIÇO que ele presta ao projeto e que está no orçamento analítico. Pagamentos a cônjuge, companheiro(a), empresa coligada ou com sócio em comum somam aqui.", "Limite calculado sobre o VALOR CAPTADO."],
    ["<b>CAPTAÇÃO</b> (remuneração de captação)", "Pagamento ao profissional/empresa que busca incentivadores para o projeto. Serviço prestado ao proponente, pago proporcionalmente ao que for captado.", "Limite: menor valor entre 10% do VALOR DO PROJETO e R$ 150.000."],
])}
{box("warn", "Por que isso importa no seu bolso", "<p>Se você previu R$ 24.000 de remuneração num projeto de R$ 184.360 e captou só 50% (R$ 92.180), a remuneração passa a representar 26% do captado. Para pessoa física (limite de 30%) ainda passa; para uma PJ comum (limite de 20%) estouraria. <b>O limite em reais encolhe junto com a captação.</b> A aba RADAR DE LIMITES simula isso para você.</p>")}
"""))

# =================================================================== TABELA-MESTRA
lim_rows = [
    ["Remuneração do proponente — geral", "20%", "VALOR CAPTADO", "Proponente que presta serviço previsto no orçamento. Pagamentos a cônjuge/companheiro, coligada ou sócio em comum somam.", "Não se aplica a grupos artísticos familiares, corpos artísticos estáveis e grupos/coletivos que atuam na execução (confira a redação)."],
    ["Remuneração do proponente — PF ou MEI", "30%", "VALOR CAPTADO", "Proponente pessoa física ou microempreendedor individual.", "Continua exigindo serviço efetivo."],
    ["Mesmo fornecedor", "20%", "VALOR CAPTADO", "Qualquer fornecedor pago com recurso incentivado.", "Há exceções (ex.: conservação e restauro de bens culturais). Confira a lista completa."],
    ["Custos de administração", "15%", "VALOR DO PROJETO", "Todos.", "Pagos proporcionalmente ao captado."],
    ["Acessibilidade, comunicação e divulgação acessíveis", "20%", "VALOR DO PROJETO", "Todos.", "Proporcional à captação. É teto, não meta."],
    ["Divulgação / comunicação", "20%", "VALOR DO PROJETO", "Todos.", "Inclui assessoria de comunicação, divulgação e impulsionamento. Confira exceções."],
    ["Remuneração de captação", "10% e teto de R$ 150.000", "VALOR DO PROJETO", "Quem contrata captador.", "Vale o menor dos dois. Pago proporcionalmente ao captado. Proibido pagar serviço prestado ao incentivador."],
    ["Cachê artista solo", "R$ 25.000", "por apresentação", "Pago com incentivo.", "Acima: outras fontes ou apreciação da CNIC."],
    ["Cachê grupo/coletivo", "R$ 50.000", "por apresentação", "Idem.", "Idem."],
    ["Cachê músico de orquestra", "R$ 5.000", "por apresentação", "Idem.", "Idem."],
    ["Cachê maestro/regente", "R$ 25.000", "por apresentação", "Idem.", "Idem."],
    ["Cachê palestrante/conferencista", "R$ 5.000", "por participação", "Idem.", "Idem."],
    ["Primeiro projeto — dispensa de comprovar atuação", "até R$ 200.000", "valor do projeto (confira o termo exato)", "Quem apresenta o PRIMEIRO projeto ao Pronac.", "Dispensa só a comprovação de atuação cultural."],
    ["Projetos ativos — PF", "2 projetos / R$ 500 mil", "soma dos projetos ativos", "Pessoa física.", "—"],
    ["Projetos ativos — MEI", "4 projetos / R$ 1,5 mi", "soma dos projetos ativos", "MEI.", "—"],
    ["Projetos ativos — demais PJ", "10 projetos / R$ 15 mi", "soma dos projetos ativos", "Demais pessoas jurídicas.", "Há regras específicas para alguns casos; confira."],
    ["Distribuição gratuita promocional — patrocinador", "até 10%", "total de ingressos/produtos", "Projetos com ingressos/produtos.", "—"],
    ["Distribuição gratuita promocional — proponente", "até 10%", "total de ingressos/produtos", "Idem.", "Para ações de divulgação."],
    ["Distribuição gratuita social/educativa", "mínimo 10%", "total de ingressos/produtos", "Idem.", "—"],
    ["Comercialização a preço popular", "mínimo 20%, até R$ 50", "total de ingressos/produtos", "Idem.", "Projeto 100% gratuito: confirme como declarar."],
    ["Execução do projeto", "até 36 meses", "prazo", "Todos.", "Ajuste à realidade."],
    ["Apresentação de propostas", "1º/fev a 31/out", "calendário anual", "Todos.", "Confirme avisos do MinC sobre o ano corrente."],
]
add(P("Tabela-mestra", f"""
<div class="kicker">Consulta rápida · cada limite com sua base de cálculo</div>
<h1>Tabela-mestra de limites 2026 (1/2)</h1>
<p class="lead">Orçamento: remuneração, custos vinculados, captação e cachês.</p>
{table(["Regra", "Limite", "Base de cálculo", "Quem está sujeito", "Exceções / atenção"], lim_rows[:12], "compact")}
"""))
add(P("Tabela-mestra", f"""
<div class="kicker">Consulta rápida · cada limite com sua base de cálculo</div>
<h1>Tabela-mestra de limites 2026 (2/2)</h1>
<p class="lead">Proponente, carteira de projetos, distribuição e prazos.</p>
{table(["Regra", "Limite", "Base de cálculo", "Quem está sujeito", "Exceções / atenção"], lim_rows[12:], "compact")}
<p class="tiny muted">Fonte de todas as linhas: Instrução Normativa MinC nº 29/2026 — {L_IN29}. Números levantados em 25/09/2026 a partir de publicações que reproduzem o texto da IN e de comunicados oficiais do MinC. Antes do envio, localize cada dispositivo no texto oficial e anote o artigo na aba PARAMETROS (coluna “Status da verificação”). Se houver divergência, prevalece o texto oficial.</p>
"""))

add(P("Tabela-mestra", f"""
<div class="kicker">Como ler a tabela-mestra</div>
<h1>3 perguntas antes de usar qualquer limite</h1>
<div class="grid3">
{box("what", "1. Qual é a base?", "<p>Valor do projeto? Valor captado? Total de ingressos? Por apresentação? <b>Sem base, o percentual não significa nada.</b></p>")}
{box("warn", "2. Quem está sujeito?", "<p>PF, MEI, PJ, grupos artísticos familiares, corpos estáveis… A mesma regra pode ter números diferentes para cada um.</p>")}
{box("wrong", "3. Qual é a exceção?", "<p>Quase toda regra tem exceção. <b>Nunca</b> presuma que a sua situação é a exceção: confirme na redação oficial.</p>")}
</div>
<h3>Exemplo de leitura correta</h3>
<div class="rule">“A remuneração do proponente pessoa física pode chegar a 30% do VALOR CAPTADO, desde que ele preste serviço ao projeto previsto no orçamento analítico.”<small>Errado: “o proponente pode ficar com 30% do projeto”. Isso ignora a base (captado), a condição (serviço efetivo) e o orçamento analítico.</small></div>
<h3>Onde está cada limite na planilha</h3>
{table(["Limite", "Aba", "Linha/coluna"], [
    ["Remuneração do proponente", "RADAR DE LIMITES", "Calculadora A + cenários de captação"],
    ["Fornecedor", "ORÇAMENTO (coluna P) e RADAR", "Calculadora B"],
    ["Administração", "RADAR", "Calculadora C"],
    ["Acessibilidade/comunicação/divulgação acessíveis", "RADAR", "Calculadora D1"],
    ["Divulgação", "RADAR", "Calculadora D2"],
    ["Captação", "RADAR", "Calculadora E"],
    ["Distribuição / preço popular", "DISTRIBUICAO", "Calculadora F"],
    ["% por categoria", "RADAR", "Tabela G"],
    ["Valor por beneficiário", "RADAR", "Calculadora H"],
    ["Iniciante e carteira de projetos", "RADAR", "Linhas I e J"],
    ["Cachês", "ORÇAMENTO", "Coluna Q (alerta automático)"],
], "compact")}
"""))

# =================================================================== MÓDULO 1
M1 = "Módulo 1 · Posso começar?"
add(divider("01", "Primeiro: descubra se você está pronto", "Antes de escrever uma linha do projeto, confirme se você pode ser proponente, qual é o seu tipo e quais limites se aplicam a você. 20 minutos aqui evitam semanas de retrabalho.", M1))
add(P(M1, f"""
<div class="kicker">Módulo 1 · Capítulo 1.1</div><h2>Quem pode apresentar proposta</h2>
{chapter(
    "<p><b>Proponente</b> é a pessoa (física ou jurídica) que apresenta o projeto, assina, responde por ele e presta contas. Podem ser proponentes pessoas físicas com atuação na área cultural e pessoas jurídicas de natureza cultural (com ou sem fins lucrativos), inclusive MEI, nas condições da norma. O MinC mantém a página oficial <i>“Quem pode participar?”</i>.</p>",
    ul(["Defina se você vai apresentar como <b>pessoa física</b>, <b>MEI</b> ou <b>pessoa jurídica</b>.", "Se for PJ: confira se a finalidade/atividade cultural aparece no ato constitutivo (estatuto/contrato social) e na atividade econômica (CNAE) cadastrada.", "Confira quantos projetos ativos você já tem e a soma dos valores (limites por tipo de proponente).", "Separe quem é o <b>proponente</b> de quem vai operar o sistema (responsável/procurador)."]),
    ul(["Apresentar como PF um projeto grande demais para o teto de PF (R$ 500 mil somando projetos ativos).", "PJ sem finalidade cultural no ato constitutivo.", "Usar CPF/CNPJ de outra pessoa para “driblar” limite de projetos — isso é irregular.", "Confundir proponente com produtor contratado: quem responde e presta contas é o proponente."]),
    ["Sei se sou PF, MEI ou demais PJ.", "Sei quantos projetos ativos tenho e a soma dos valores.", "Se PJ, a natureza cultural está no ato constitutivo/CNAE.", "Li a página oficial “Quem pode participar?”."]
)}
{table(["Tipo", "Projetos ativos", "Teto global (soma dos ativos)", "Remuneração do proponente"], [
    ["Pessoa física", "até 2", "R$ 500 mil", "até 30% do valor captado"],
    ["MEI", "até 4", "R$ 1,5 milhão", "até 30% do valor captado"],
    ["Demais pessoas jurídicas", "até 10", "R$ 15 milhões", "até 20% do valor captado (com exceções)"],
], "compact")}
<p class="tiny muted">{NEW} Fonte: {FONTE_IN}. Link: {L_IN29}</p>
"""))

add(P(M1, f"""
<div class="kicker">Módulo 1 · Capítulo 1.2</div><h2>Proponente, responsável, cadastro e procuração</h2>
{chapter(
    "<p>O Salic é acessado com conta <b>gov.br</b>. O <b>cadastro do proponente</b> reúne os dados de quem responde pelo projeto. Em PJ, uma pessoa física (dirigente ou procurador) opera o sistema em nome da empresa/instituição. A <b>procuração</b> só é necessária quando outra pessoa age em nome do proponente.</p>",
    ul(["Crie ou recupere sua conta gov.br e teste o login no Salic <b>hoje</b>, não no dia do envio.", "Atualize e-mail e telefone: as diligências e comunicações chegam por ali.", "Em PJ, confira quem é o dirigente registrado e se o responsável que vai operar o Salic está vinculado corretamente.", "Se houver procurador, prepare a procuração conforme o Manual do Proponente.", "Anote os dados exatamente como no CNPJ/CPF: nome, endereço, natureza jurídica."]),
    ul(["Descobrir no último dia que a conta gov.br está bloqueada ou sem o nível de acesso exigido.", "E-mail antigo no cadastro → você perde o prazo de uma diligência sem saber.", "Dados divergentes entre cadastro, CNPJ e documentos anexados.", "Procurador operando sem vínculo formal."]),
    ["Login gov.br testado no Salic.", "Cadastro do proponente completo e atualizado.", "E-mail e telefone que eu acompanho.", "Responsável/procurador vinculado (se aplicável).", "Dados iguais em todos os documentos."]
)}
"""))

add(P(M1, f"""
<div class="kicker">Módulo 1 · Capítulo 1.3</div><h2>Portfólio e a regra do primeiro projeto</h2>
{box("what", "① O que é", f"<p>Para apresentar projetos, o proponente precisa <b>comprovar atuação na área cultural</b>. {NEW} Em 2026, essa comprovação passa a ocorrer pela apresentação de <b>portfólio no Salic</b> (deixou de existir a habilitação automática que alguns materiais antigos citam).</p>")}
<div class="rule">A EXCEÇÃO, SEM SIMPLIFICAR:<br>O proponente que apresenta o seu PRIMEIRO projeto ao Pronac fica dispensado de comprovar atuação na área cultural, se o valor do projeto for de até R$ 200.000,00.<small>Redação conforme o texto da IN MinC nº 29/2026 reproduzido em fontes consultadas. Confira o termo exato (“valor do projeto” ou “valor total do projeto”) no texto oficial.</small></div>
{table(["A dispensa É", "A dispensa NÃO É"], [
    ["Dispensa de comprovar <b>atuação na área cultural</b> (portfólio).", "Dispensa de cadastro, documentos obrigatórios, orçamento, acessibilidade ou democratização."],
    ["Para quem apresenta o <b>primeiro projeto ao Pronac</b>.", "Para quem já teve projeto no Pronac, mesmo que não tenha captado."],
    ["Para projeto de <b>até R$ 200.000,00</b>.", "Válida para projeto de R$ 200.000,01 ou mais — aí é preciso comprovar atuação."],
    ["Uma porta de entrada.", "Garantia de admissão, aprovação ou captação."],
], "compact")}
{box("do", "② O que você precisa fazer", ul(["Confirme no Salic se você (CPF/CNPJ) já tem projeto no Pronac.", "Perto de R$ 200 mil? <b>Por prudência</b>, mantenha abaixo do limite o valor do projeto e o valor total (com outras fontes).", "Mesmo dispensado, tenha currículo/portfólio da equipe. Não dispensado: portfólio (links, fotos, clipping, declarações) pronto no Salic."]))}
{box("wrong", "③ O que pode dar errado", ul(["Achar que a dispensa vale para “iniciante” em geral — ela é para o <b>primeiro projeto no Pronac</b> e até R$ 200 mil.", "Orçamento de R$ 201 mil “porque a diferença é pequena”.", "Depender da dispensa e deixar a equipe sem currículo nenhum."]))}
{check("④ CHECKLIST", ["Confirmei se é meu primeiro projeto no Pronac e conferi o valor contra R$ 200.000,00.", "Portfólio no Salic pronto (se não dispensado) e currículo da equipe em mãos."])}
"""))

add(P(M1, f"""
<div class="kicker">Módulo 1 · Capítulo 1.4</div><h2>Documentação e cuidados com dados</h2>
{chapter(
    f"<p>{NEW} Documentos obrigatórios devem ser anexados <b>no momento da apresentação</b>. A lista exata depende do tipo de proponente e do segmento do projeto e está no Manual do Proponente e na IN. O Módulo 8 traz o checklist completo.</p>",
    ul(["Baixe o Manual do Proponente IN 2026 e marque as páginas de documentos.", "Separe documentos do <b>proponente</b>, do <b>projeto</b>, <b>específicos</b> do segmento e <b>eventuais</b>.", "Digitalize em boa resolução, nomeie os arquivos com clareza (ex.: <i>01_Estatuto_Associacao_X.pdf</i>).", "Anote validades (certidões, atas de eleição de diretoria)."]),
    ul(["Deixar para anexar “depois” — em 2026 isso é risco alto.", "Ata de diretoria vencida; estatuto sem finalidade cultural.", "Arquivo ilegível ou com páginas faltando.", "Carta de anuência genérica, sem data e sem assinatura."]),
    ["Tenho a lista oficial de documentos para meu tipo e segmento.", "Todos os arquivos estão digitalizados, legíveis e nomeados.", "Validades anotadas na aba CHECKLIST DOCUMENTOS.", "Nada ficou para depois do envio."]
)}
"""))

add(P(M1, f"""
<div class="kicker">Módulo 1 · Ferramenta</div><h1>CHECKLIST “POSSO COMEÇAR?”</h1>
<p class="lead">Se houver qualquer “NÃO” nos itens marcados com ★, resolva antes de ir para o Módulo 2.</p>
{table(["", "Pergunta", "SIM", "NÃO", "N/A"], [[s, q, "☐", "☐", "☐"] for s, q in [
    ("★", "Tenho conta gov.br funcionando e consegui entrar no Salic."),
    ("★", "Sei se vou apresentar como pessoa física, MEI ou pessoa jurídica."),
    ("★", "Meu tipo de proponente comporta mais um projeto ativo (2 PF / 4 MEI / 10 PJ)."),
    ("★", "A soma dos meus projetos ativos + este cabe no teto global do meu tipo."),
    ("★", "Se PJ: a natureza cultural consta do ato constitutivo/atividade econômica."),
    ("★", "Tenho portfólio de atuação cultural OU estou na dispensa de primeiro projeto até R$ 200 mil."),
    ("", "Meu cadastro tem e-mail e telefone que eu acompanho."),
    ("", "Sei quem vai operar o Salic (eu, dirigente ou procurador com vínculo)."),
    ("", "Tenho a lista oficial de documentos do meu tipo e segmento."),
    ("", "Meus documentos estão dentro da validade."),
    ("", "Consigo descrever a ideia do projeto em 3 frases (o quê, onde, para quem)."),
    ("", "Tenho pelo menos 3 dias úteis antes do prazo final para trabalhar na proposta."),
    ("", "Li a tabela “Regras que você não deve copiar de materiais antigos”."),
    ("", "Entendi a diferença entre valor do projeto, valor total e valor captado."),
]], "compact")}
<div class="grid2">
{box("do", "Resultado: tudo ★ em SIM", "<p>Você pode começar. Vá para o Módulo 2 e abra a aba MAPA DO PROJETO.</p>")}
{box("wrong", "Resultado: algum ★ em NÃO", "<p>Pare aqui. Resolva o item (cadastro, tipo de proponente, portfólio, limite de carteira) antes de escrever o projeto.</p>")}
</div>
"""))

# =================================================================== MÓDULO 2
M2 = "Módulo 2 · Ideia → projeto"
add(divider("02", "Transforme sua ideia em projeto", "O Salic não é lugar de ter ideia: é lugar de colar respostas prontas. Neste módulo você escreve cada campo fora do sistema, com fórmulas simples e exemplos bons e ruins.", M2))
campos2 = [
    ("Nome do projeto", "Curto, específico, fácil de lembrar.", "“Projeto Cultural 2027”", "“Teatro na Praça: Circuito de Rua 2027”"),
    ("Resumo", "O QUÊ + ONDE + QUANDO + PARA QUEM + COMO, em até 5 linhas.", "“Projeto que visa promover a cultura e a cidadania.”", "“8 apresentações gratuitas de teatro de rua em 4 praças dos bairros X e Y (cidade/UF), de março a junho de 2027, com oficinas para jovens, Libras e audiodescrição.”"),
    ("Objeto", "A entrega concreta.", "“Fomentar a cultura.”", "“Circulação do espetáculo Z com 8 apresentações e 4 oficinas.”"),
    ("Objetivo geral", "1 frase, verbo no infinitivo, resultado cultural amplo.", "“Levar cultura para todos.”", "“Ampliar o acesso ao teatro em bairros sem equipamento cultural de [cidade].”"),
    ("Objetivos específicos", "3 a 5, cada um mensurável. Cada um vira meta e produto.", "“Valorizar a arte; promover a inclusão.”", "“Realizar 8 apresentações gratuitas; formar 60 jovens em 4 oficinas; garantir Libras e audiodescrição em 100% das sessões.”"),
]
add(P(M2, f"""
<div class="kicker">Módulo 2 · Capítulo 2.1</div><h2>Nome, resumo, objeto e objetivos</h2>
{box("what", "① O que é", "<p>São os campos que dizem <b>o que</b> o projeto é. Quem analisa precisa entender o projeto inteiro só lendo o resumo e os objetivos.</p>")}
{table(["Campo", "Fórmula", "❌ Ruim", "✅ Bom"], campos2, "compact")}
{box("do", "② O que você precisa fazer", ul(["Escreva primeiro os <b>objetivos específicos</b>: eles puxam metas, produtos e orçamento.", "Use números em tudo que puder contar.", "Evite adjetivos (“inovador”, “grandioso”) sem prova."]))}
{box("wrong", "③ O que pode dar errado", ul(["Objetivo que não vira produto (ex.: “sensibilizar a sociedade” sem ação concreta).", "Resumo que não diz onde nem quando.", "Nome diferente em cada campo/documento."]))}
{check("④ CHECKLIST", ["Resumo responde as 5 perguntas.", "Objetivo geral em 1 frase.", "Objetivos específicos têm número.", "Nome igual em tudo."])}
"""))

add(P(M2, f"""
<div class="kicker">Módulo 2 · Capítulo 2.2</div><h2>Justificativa e metodologia</h2>
{chapter(
    "<p><b>Justificativa</b> responde “por que este projeto, aqui, agora, com esta equipe?”. <b>Metodologia</b> responde “como, em que ordem e com quem?”. A metodologia é a ponte com o orçamento: toda etapa descrita precisa de despesa correspondente (ou explicação de por que não custa).</p>",
    "<p><b>Fórmula da justificativa (4 blocos):</b></p>" + ul(["<b>Contexto</b> — dado concreto do território/público (fonte e ano).", "<b>Lacuna</b> — o que falta hoje.", "<b>Resposta</b> — como o projeto preenche a lacuna.", "<b>Capacidade</b> — por que você/equipe consegue executar (histórico, parceiros)."], True) +
    "<p><b>Fórmula da metodologia:</b> para cada etapa → atividades → responsável → período → produto gerado.</p>",
    ul(["Justificativa copiada de outro projeto ou da internet (texto genérico chama atenção).", "Metodologia com etapa que não aparece no cronograma nem no orçamento.", "Dado sem fonte (“a cidade tem pouca cultura”).", "Relação com a Lei 8.313/1991 não explicada."]),
    ["Justificativa tem os 4 blocos.", "Todo dado tem fonte.", "Cada etapa da metodologia tem atividade, responsável e período.", "Cada etapa tem despesa no orçamento."]
)}
"""))

add(P(M2, f"""
<div class="kicker">Módulo 2 · Capítulo 2.3</div><h2>Público, beneficiários, local, período e etapas</h2>
{table(["Campo", "O que responder", "Erro comum"], [
    ["Público-alvo", "Perfil (idade, território, características) + estimativa numérica.", "“Público em geral.”"],
    ["Beneficiários", "Quem recebe gratuidade, formação ou acesso especial (escolas, comunidades, PcD).", "Confundir com público total."],
    ["Local", "Município/UF e tipo de espaço. Há anuência/cessão do espaço?", "Local “a definir” sem critério."],
    ["Período", "Início e fim da execução (máx. 36 meses — IN 29/2026).", "Datas que não cabem no cronograma."],
    ["Etapas", "Pré-produção, produção, pós-produção, divulgação, execução, encerramento.", "Esquecer encerramento/prestação de contas."],
], "compact")}
{chapter(
    "<p>Esses campos mostram <b>para quem, onde e quando</b>. Eles precisam conversar com o plano de distribuição (Módulo 6) e com o cronograma (Módulo 7).</p>",
    ul(["Estime público por produto (ex.: 8 sessões × 300 pessoas = 2.400).", "Liste os locais com endereço/bairro.", "Defina datas-marco: início, primeira atividade com público, encerramento."]),
    ul(["Público estimado incompatível com a capacidade do local.", "Número de pessoas diferente em cada campo.", "Local em outro município sem custo de deslocamento no orçamento."]),
    ["Público com número e perfil.", "Beneficiários identificados.", "Locais definidos e viáveis.", "Período dentro de 36 meses e coerente com o cronograma."]
)}
"""))

add(P(M2, f"""
<div class="kicker">Módulo 2 · Capítulo 2.4</div><h2>Produtos, metas e resultados esperados</h2>
{chapter(
    "<p><b>Produto</b> é o que o projeto entrega (apresentação, oficina, livro, exposição, vídeo). <b>Meta</b> é o número daquele produto. <b>Resultado</b> é o efeito esperado e como você vai comprovar.</p>",
    "<p>Monte a <b>cadeia de coerência</b> para cada objetivo:</p><div class='flow'><span>Objetivo</span><em>→</em><span>Meta (nº)</span><em>→</em><span>Produto</span><em>→</em><span>Despesas</span><em>→</em><span>Atividades/datas</span><em>→</em><span>Público/distribuição</span><em>→</em><span>Comprovação</span></div>" +
    ul(["Preencha essa cadeia na aba <b>MATRIZ CONSISTENCIA</b>: ela confere se o item do orçamento e a atividade do cronograma existem.", "Para cada resultado, defina a prova: fotos, listas de presença, vídeo, clipping, relatório."]),
    ul(["Meta sem número (“atender muitas pessoas”).", "Produto no plano de distribuição que não aparece nos objetivos.", "Resultado que você não consegue comprovar na prestação de contas."]),
    ["Todo objetivo tem meta numérica.", "Toda meta tem produto.", "Todo produto tem despesa e data.", "Todo resultado tem forma de comprovação."]
)}
{table(["Objetivo específico", "Meta", "Produto", "Comprovação"], [
    ["Realizar apresentações gratuitas", "8 apresentações / 2.400 pessoas", "Apresentação teatral", "Fotos, vídeo, contagem de público"],
    ["Formar jovens", "4 oficinas / 60 vagas", "Oficina", "Listas de presença, certificados"],
    ["Garantir acessibilidade", "100% das sessões com Libras e audiodescrição", "Apresentação acessível", "Contratos, fotos, vídeo com janela de Libras"],
], "compact")}
"""))

add(P(M2, f"""
<div class="kicker">Ferramenta · também na planilha (aba MAPA DO PROJETO)</div><h1>MAPA DO PROJETO — parte 1</h1>
<div class="grid2"><div>
{field("Nome do projeto", "Curto e específico.", 1)}
{field("Área", "Artes cênicas, música, audiovisual, patrimônio, artes visuais, humanidades…", 1)}
{field("Segmento", "Confira o segmento na tabela do Salic (define o enquadramento).", 1)}
{field("Resumo", "O QUÊ + ONDE + QUANDO + PARA QUEM + COMO.", 3)}
{field("Objetivo geral", "1 frase, verbo no infinitivo.", 2)}
</div><div>
{field("Objetivos específicos", "3 a 5, com número.", 3)}
{field("Justificativa", "Contexto → lacuna → resposta → capacidade.", 3)}
{field("Metodologia", "Etapa → atividades → responsável → período → produto.", 3)}
</div></div>
"""))

add(P(M2, f"""
<div class="kicker">Ferramenta · também na planilha (aba MAPA DO PROJETO)</div><h1>MAPA DO PROJETO — parte 2</h1>
<div class="grid2"><div>
{field("Público", "Perfil + número estimado.", 2)}
{field("Beneficiários", "Quem recebe gratuidade/formação/acesso.", 2)}
{field("Produtos", "Lista com quantidades.", 2)}
{field("Metas", "Números por produto.", 2)}
</div><div>
{field("Local", "Município/UF, espaços, anuências.", 2)}
{field("Período", "Início e fim (máx. 36 meses).", 1)}
{field("Etapas", "Pré-produção, produção, pós-produção, divulgação, execução, encerramento.", 2)}
{field("Resultados", "Efeito esperado + como vai comprovar.", 2)}
</div></div>
{box("warn", "Antes de ir para o orçamento", "<p>Leia o Mapa inteiro em voz alta. Se algum número mudar de um campo para outro (público, apresentações, datas), corrija agora. No Salic, você vai <b>copiar e colar</b> daqui.</p>")}
"""))

# =================================================================== MÓDULO 3
M3 = "Módulo 3 · Salic"
add(divider("03", "O caminho dentro do Salic", "Entrar no sistema sabendo o que vai preencher, em que ordem, e com o material pronto. Os nomes de telas podem mudar: siga sempre o Manual do Proponente vigente.", M3))
salic_steps = [
    ("a", "Acesso", "Login gov.br no Salic."),
    ("a", "Cadastro", "Proponente, contatos, vínculos, portfólio."),
    ("a", "Criação da proposta", "“Nova proposta” + declaração de responsabilidade."),
    ("b", "Identificação", "Nome, área/segmento, tipicidade e limites."),
    ("b", "Resumo", "Cole do Mapa do Projeto."),
    ("b", "Objetivos", "Geral e específicos."),
    ("b", "Justificativa", "E metodologia/etapas."),
    ("b", "Acessibilidade", "Física, comunicacional, atitudinal."),
    ("b", "Democratização", "Medidas concretas de acesso."),
    ("c", "Plano de distribuição", "Produtos, quantidades, faixas, preços."),
    ("c", "Localização", "País, UF, município."),
    ("c", "Cronograma", "Período de execução."),
    ("c", "Orçamento", "Itens por produto/etapa."),
    ("c", "Outras fontes", "Só as que existem."),
    ("d", "Documentação", "Anexe TUDO antes de enviar."),
    ("d", "Revisão", "Pendências zeradas + checklist final."),
    ("d", "Envio", "“Enviar proposta ao MinC” + comprovante."),
]
add(P(M3, f"""
<div class="kicker">Ferramenta visual</div><h1>MAPA DO SALIC — DO LOGIN AO ENVIO</h1>
<div class="legend"><span><i style="background:#64748b"></i>Entrada</span><span><i style="background:#2563eb"></i>Texto da proposta</span><span><i style="background:#15803d"></i>Números e logística</span><span><i style="background:#E85D04"></i>Fechamento</span></div><br>
<div class="salicmap">{''.join(f'<div class="sm phase-{ph}"><div class="n">{i:02d}</div><div class="h">{h}</div>{d}</div>' for i, (ph, h, d) in enumerate(salic_steps, 1))}
<div class="sm" style="border-style:dashed"><div class="h">Depois do envio</div>Acompanhe diligências no Salic e no e-mail. Responda dentro do prazo.</div></div>
<p class="tiny muted" style="margin-top:3mm">Ordem lógica de preparação baseada no Manual do Proponente IN 2026 ({L_MANUAL}). A ordem e os nomes exatos das abas/telas no sistema podem variar: siga o Manual vigente e o que o Salic exibir. O manual cita, entre outros: “Nova proposta”, declaração de responsabilidade, identificação (nome, tipicidade e limites de orçamento), resumo, informações complementares, período de realização, objetivos e justificativa, plano de distribuição, local de realização, despesas por produto e “Enviar proposta ao MinC”, com lista de pendências quando algo falta.</p>
"""))

salic_detail = [
    ("1. Acesso", "Conta gov.br com o nível exigido; navegador atualizado.", "Senha/2FA travada no último dia."),
    ("2. Cadastro", "Dados do proponente, contatos, vínculos, portfólio.", "E-mail desatualizado; PJ sem responsável vinculado."),
    ("3. Criação da proposta", "Ler a declaração de responsabilidade.", "Aceitar sem ler compromissos."),
    ("4. Identificação", "Nome, área/segmento, tipicidade e limites.", "Segmento errado muda o enquadramento."),
    ("5. Resumo", "Texto do Mapa do Projeto.", "Resumo genérico."),
    ("6. Objetivos", "Geral + específicos com números.", "Objetivos sem meta."),
    ("7. Justificativa", "4 blocos + metodologia.", "Texto copiado."),
    ("8. Acessibilidade", "Medidas por produto, com custo.", "Parágrafo padrão sem custo."),
    ("9. Democratização", "Medidas concretas com números.", "“O projeto é democrático” sem dados."),
    ("10. Plano de distribuição", "Cada produto com quantidades e preços por faixa.", "Faixas fora dos limites."),
    ("11. Localização", "UF/município de cada produto.", "Local sem despesa de deslocamento."),
    ("12. Cronograma", "Período de execução.", "Período incompatível com as atividades."),
    ("13. Orçamento", "Itens da aba ORÇAMENTO.", "Limites estourados; itens sem vínculo."),
    ("14. Outras fontes", "Fontes confirmadas.", "Fonte inventada para “fechar conta”."),
    ("15. Documentação", "Todos os obrigatórios.", "Deixar para depois (2026: risco alto)."),
    ("16. Revisão", "Pendências zeradas; checklist final.", "Enviar com pendência."),
    ("17. Envio", "Salvar comprovante/print.", "Enviar no último minuto."),
]
add(P(M3, f"""
<div class="kicker">Módulo 3 · Passo a passo</div><h2>O que ter pronto em cada passo</h2>
{table(["Passo", "O que você precisa ter em mãos", "O que costuma dar errado"], salic_detail, "compact")}
{box("do", "Regra de ouro do Salic", "<p>Preencha na ordem, <b>salve a cada campo</b> e cole textos já revisados. Se o sistema indicar pendências, resolva uma a uma usando a aba CHECKLIST SALIC.</p>")}
"""))

add(P(M3, f"""
<div class="kicker">Módulo 3 · Capítulo 3.1</div><h2>Entrar no Salic sem sustos</h2>
{chapter(
    "<p>O Salic é o sistema oficial onde a proposta é cadastrada, analisada e acompanhada. A proposta só existe para o MinC depois do clique de envio — rascunho não conta.</p>",
    ul(["Teste o acesso agora e abra uma proposta para conhecer as telas (sem enviar).", "Tenha abertos: Mapa do Projeto, planilha ORÇAMENTO, CRONOGRAMA, DISTRIBUICAO e a pasta de documentos.", "Preencha em blocos de 30–40 minutos, salvando sempre.", "Ao final, veja a lista de pendências e zere-a.", "Envie e salve o comprovante (print com data e hora)."]),
    ul(["Sessão expirar e você perder texto digitado direto no sistema.", "Colar texto com formatação estranha (use texto simples).", "Descobrir limite de caracteres na hora — escreva enxuto (a planilha mostra a contagem).", "Enviar no dia 31 e o sistema estar lento."]),
    ["Acesso testado com antecedência.", "Todo o conteúdo pronto fora do sistema.", "Pendências zeradas.", "Comprovante de envio salvo.", "Alerta no celular para acompanhar diligências."]
)}
"""))

# =================================================================== MÓDULO 4
M4 = "Módulo 4 · Orçamento"
add(divider("04", "Orçamento sem cair nas armadilhas", "É aqui que a maioria dos iniciantes erra. Não por má-fé, mas por não saber a base de cálculo, esquecer rubricas obrigatórias ou colocar despesas que não se explicam.", M4))
add(P(M4, f"""
<div class="rule">SE NÃO CONSIGO EXPLICAR POR QUE ESSA DESPESA EXISTE, NÃO COLOQUE A DESPESA.<small>Na planilha, a coluna M (“Por que essa despesa existe?”) é obrigatória. Linha sem resposta fica 🔴.</small></div>
<div class="kicker">Módulo 4 · Capítulo 4.1</div><h2>Orçamento analítico: a anatomia de uma linha</h2>
{table(["Etapa", "Item", "Descrição", "Unidade", "Qtd.", "Valor unit.", "Valor total", "Fonte", "Fornecedor", "Observação"], [
    ["Produção", "Intérprete de Libras", "Por sessão, 1h30", "sessão", "8", "R$ 600", "R$ 4.800", "Incentivo", "Intérprete G", "3 cotações guardadas"],
], "compact")}
{chapter(
    "<p><b>Orçamento analítico</b> é o orçamento detalhado item a item: etapa, item, unidade, quantidade, valor unitário, valor total e fonte. Cada linha precisa ter relação direta com o objeto do projeto e preço compatível com o mercado.</p>",
    ul(["Monte o orçamento <b>a partir da metodologia</b>: etapa por etapa, pergunte “o que preciso contratar/comprar para isso acontecer?”.", "Use unidades reais (sessão, diária, mês, hora, exemplar) — evite “verba” quando der para detalhar.", "Guarde cotações/referências de preço dos itens mais caros.", "Classifique cada linha na coluna <b>Categoria de limite</b> para as calculadoras funcionarem.", "Inclua tributos e encargos quando aplicáveis ao tipo de contratação (consulte um contador)."]),
    ul(["Valor total “redondo” sem memória de cálculo.", "Mesmo serviço em duas linhas com nomes diferentes.", "Unidade “verba” para tudo.", "Itens sem relação com o objeto (ex.: equipamento permanente sem justificativa de uso no projeto)."]),
    ["Toda linha tem unidade, quantidade e valor unitário.", "Toda linha tem justificativa (coluna M).", "Preços com referência.", "Categorias preenchidas."]
)}
"""))

add(P(M4, f"""
<div class="kicker">Módulo 4 · Capítulo 4.2</div><h2>Coerência, mercado e despesas diretas</h2>
{box("what", "① O que é", "<p>Três testes que toda despesa precisa passar: <b>vínculo</b> (existe por causa do projeto?), <b>coerência</b> (a metodologia pede isso?) e <b>preço</b> (é compatível com o mercado?).</p>")}
{table(["Teste", "Pergunta", "Se a resposta for não…"], [
    ["Vínculo", "Esta despesa existiria se o projeto não existisse?", "Se existiria mesmo sem o projeto (ex.: aluguel da sua sede para todas as atividades), não é despesa do projeto — ou precisa ser rateada e justificada."],
    ["Coerência", "Em que etapa da metodologia ela aparece?", "Se não aparece, ou a metodologia está incompleta ou a despesa sobra."],
    ["Quantidade", "Quantidade bate com metas e cronograma?", "8 apresentações × 1 diária de som = 8 diárias, não 20."],
    ["Preço", "Tenho referência de mercado?", "Faça cotação. Preço fora do mercado é risco alto."],
    ["Fonte", "Quem paga essa linha?", "Não pode haver duas fontes para a mesma despesa."],
], "compact")}
{box("do", "② O que você precisa fazer", ul(["Para cada linha, preencha colunas M (por quê), N (preço conferido) e O (outra fonte?).", "Faça 3 cotações para os itens que somam mais de 10% do projeto.", "Confira quantidades cruzando com metas (Módulo 2) e cronograma (Módulo 7)."]))}
{box("wrong", "③ O que pode dar errado", ul(["Despesa de estrutura permanente da instituição lançada inteira no projeto.", "Quantidades “de sobra” para garantir.", "Preço copiado de projeto de outra cidade/ano sem atualizar."]))}
{check("④ CHECKLIST", ["Nenhuma linha falha nos 5 testes.", "Cotações guardadas para itens relevantes.", "Quantidades conferidas com metas e cronograma."])}
"""))

add(P(M4, f"""
<div class="kicker">Módulo 4 · Capítulo 4.3</div><h2>As rubricas com limite: onde cada despesa entra</h2>
{table(["Rubrica", "Exemplos", "Limite e base", "Atenção"], [
    ["Remuneração do proponente", "Coordenação geral, direção artística feita pelo próprio proponente.", "20% (geral) ou 30% (PF/MEI) do <b>VALOR CAPTADO</b>.", "Só por serviço efetivo previsto. Cônjuge/companheiro, coligada e sócio em comum somam."],
    ["Custos de administração", "Contador, tarifas bancárias, material de escritório do projeto, regularização documental de patrimônio.", "15% do <b>VALOR DO PROJETO</b>.", "Pagos proporcionalmente ao captado. Não coloque produção aqui."],
    ["Divulgação / comunicação", "Assessoria de comunicação, peças, impulsionamento.", "20% do <b>VALOR DO PROJETO</b>.", "Materiais passam por aprovação do MinC; marcas obrigatórias."],
    ["Acessibilidade, comunicação e divulgação acessíveis", "Libras, audiodescrição, legendas, rampas removíveis, consultor de acessibilidade, equipe treinada.", "20% do <b>VALOR DO PROJETO</b>.", "Teto, não meta. Obrigatório prever medidas."],
    ["Remuneração de captação", "Captador ou empresa de captação.", "Menor entre 10% do <b>VALOR DO PROJETO</b> e R$ 150 mil.", "Proporcional ao captado. Nunca serviço ao incentivador."],
    ["Cachês", "Artistas, grupos, músicos, maestros, palestrantes.", "Valores por apresentação (ver tabela-mestra).", "Acima: outras fontes ou CNIC."],
    ["Tributos e encargos", "INSS, ISS, encargos de contratação, quando aplicáveis.", "Conforme natureza da contratação.", "Consulte contador; não invente percentuais."],
    ["Produção / atividade-fim", "Tudo que faz o produto existir.", "Sem percentual específico; limite por fornecedor vale.", "Precisa de vínculo e preço de mercado."],
], "compact")}
{box("wrong", "Classificação artificial", "<p>Não reclassifique despesa para “caber” no limite (ex.: chamar assessoria de imprensa de “produção” ou remuneração do proponente de “consultoria”). A classificação deve refletir a natureza real do serviço. Remuneração escondida em outra rubrica é risco alto.</p>")}
"""))

bom = [
    ["Pré-produção", "Produção executiva", "mês", "6", "R$ 3.500", "R$ 21.000", "Executa logística das 8 apresentações", "🟢"],
    ["Produção", "Cachê grupo teatral", "apresentação", "8", "R$ 6.000", "R$ 48.000", "Produto principal", "🟢 cachê ok · 🔴 fornecedor 26% do captado"],
    ["Produção", "Som e luz", "diária", "8", "R$ 1.800", "R$ 14.400", "Uma diária por apresentação", "🟢"],
    ["Acessibilidade", "Intérprete de Libras", "sessão", "8", "R$ 600", "R$ 4.800", "Objetivo 3", "🟢"],
    ["Administração", "Contador", "mês", "6", "R$ 700", "R$ 4.200", "Prestação de contas", "🟢"],
]
risco = [
    ["Produção", "Despesas gerais", "verba", "1", "R$ 30.000", "R$ 30.000", "(vazio)", "🔴 sem vínculo, sem detalhe"],
    ["Administração", "Produção executiva", "mês", "12", "R$ 5.000", "R$ 60.000", "“apoio”", "🔴 produção classificada como administração; estoura 15%"],
    ["Produção", "Consultoria artística (esposa do proponente)", "mês", "6", "R$ 6.000", "R$ 36.000", "“consultoria”", "🔴 soma no limite do proponente; remuneração escondida"],
    ["Divulgação", "Notebook e câmera", "unidade", "2", "R$ 9.000", "R$ 18.000", "“registro”", "🔴 bem permanente sem justificativa; rubrica errada"],
    ["Produção", "Som e luz", "diária", "20", "R$ 1.800", "R$ 36.000", "“por segurança”", "🔴 quantidade ≠ cronograma (8 apresentações)"],
]
add(P(M4, f"""
<div class="kicker">Módulo 4 · Diferencial do kit</div><h1>ORÇAMENTO BOM <span style="color:#c0262d">versus</span> ORÇAMENTO DE RISCO</h1>
<h3 style="color:#15803d">✅ Orçamento bom (trecho do projeto-exemplo)</h3>
{table(["Etapa", "Item", "Unid.", "Qtd", "Unit.", "Total", "Por que existe", "Radar"], bom, "compact")}
<p class="small">Mesmo o orçamento bom tem um alerta: o cachê do grupo (R$ 48 mil) passa de 20% do valor captado para um único fornecedor. <b>Soluções legítimas:</b> conferir se há exceção aplicável, reduzir o número/valor das apresentações ou financiar parte com outras fontes confirmadas. <b>Solução ilegítima:</b> dividir o mesmo fornecedor em nomes/CNPJs diferentes.</p>
<h3 style="color:#c0262d">❌ Orçamento de risco</h3>
{table(["Etapa", "Item", "Unid.", "Qtd", "Unit.", "Total", "Por que existe", "Radar"], risco, "compact")}
{box("do", "Como corrigir o orçamento de risco", ul(["“Despesas gerais” → quebre em itens reais ou retire.", "Produção executiva → rubrica de produção, com quantidade igual ao período real.", "Consultoria da esposa → se é serviço real, lance como remuneração vinculada e respeite o limite sobre o captado; se não é, retire.", "Equipamentos → prefira locação; compra só com justificativa forte e conforme regras de bens.", "Som e luz → 8 diárias, uma por apresentação."]))}
"""))

add(P(M4, f"""
<div class="kicker">Módulo 4 · Capítulo 4.4</div><h2>Outras fontes, dupla cobertura e captação</h2>
{chapter(
    "<p><b>Outras fontes</b> são recursos fora do incentivo (patrocínio direto, recursos próprios, apoio em serviços). <b>Dupla cobertura</b> é a mesma despesa paga por duas fontes. <b>Captação</b> é o serviço de buscar incentivadores.</p>",
    ul(["Declare outra fonte só se ela existe e está comprometida (carta, contrato, termo).", "Ligue cada outra fonte a linhas específicas do orçamento (coluna Fonte).", "Na coluna O, responda: “esta despesa é paga também por outra fonte?”.", "Se contratar captador: limite = menor entre 10% do valor do projeto e R$ 150 mil; pagamento proporcional ao captado; serviço prestado ao proponente."]),
    ul(["Inventar contrapartida para parecer mais robusto — depois você terá de comprovar.", "Mesma despesa no incentivo e em edital estadual/municipal.", "Captador pago como “consultor” para fugir do limite.", "Pagar captador por serviço prestado ao patrocinador (proibido)."]),
    ["Toda outra fonte tem documento.", "Nenhuma linha com “Sim” na coluna O.", "Captação dentro do menor limite.", "Contrato de captação prevê pagamento proporcional."]
)}
"""))

add(P(M4, f"""
<div class="kicker">Módulo 4 · Capítulo 4.5</div><h2>Remuneração, tributos e encargos</h2>
{chapter(
    "<p>Toda pessoa que trabalha no projeto deve ser remunerada por um serviço descrito, com unidade e quantidade. Tributos e encargos dependem da forma de contratação (PF, MEI, PJ, CLT) e do município.</p>",
    ul(["Descreva a função (ex.: “produção executiva — 6 meses”) e não a pessoa.", "Para cada contratação, confirme com contador os tributos/encargos incidentes e lance-os como linha própria quando aplicável.", "Se o proponente vai trabalhar no projeto, lance a função real e confira o limite na calculadora A.", "Simule captação parcial (75% e 50%) e veja se a remuneração continua dentro do limite."]),
    ul(["Esquecer encargos e faltar dinheiro na execução.", "Remuneração do proponente sem função descrita.", "Pagamento a parente/sócio sem computar no limite do proponente."]),
    ["Toda remuneração tem função, unidade e quantidade.", "Tributos/encargos conferidos com contador.", "Calculadora A 🟢 em 100% e em 50% de captação."]
)}
"""))

# =================================================================== MÓDULO 5 — RADAR
M5 = "Módulo 5 · Radar de Zona de Perigo"
add(divider("05", "Radar de Zona de Perigo", "14 riscos concretos, cada um com critério objetivo de 🔴 ALTO RISCO, 🟡 ATENÇÃO e 🟢 CONFERIDO. Use junto com a aba RADAR DE LIMITES.", M5))


def radar(n, t, red, yel, grn, fonte=""):
    f = f'<div class="tiny muted">Fonte: {fonte}</div>' if fonte else ""
    return (f'<div class="radar"><h3>{n}. {t}</h3>'
            f'<div class="row"><span class="pill p-red">🔴 ALTO RISCO</span><span>{red}</span></div>'
            f'<div class="row"><span class="pill p-yel">🟡 ATENÇÃO</span><span>{yel}</span></div>'
            f'<div class="row"><span class="pill p-grn">🟢 CONFERIDO</span><span>{grn}</span></div>{f}</div>')


add(P(M5, f"""
<div class="kicker">Radar · risco 1</div>
<h2>1. Remuneração do proponente</h2>
{table(["Ponto", "Regra 2026"], [
    ["Pode ser remunerado?", "Sim, com recursos captados."],
    ["Condição", "Precisa <b>prestar serviço ao projeto</b>, e o serviço precisa estar <b>previsto no orçamento analítico</b>."],
    ["Limite geral", "<b>20% do VALOR CAPTADO</b>."],
    ["Pessoa física ou MEI", "Limite de até <b>30% do VALOR CAPTADO</b>."],
    ["Cônjuge/companheiro(a)", "Pagamentos por serviços realizados por cônjuge ou companheiro(a) <b>entram no limite</b> do proponente."],
    ["Empresa coligada ou com sócio em comum", "Pagamentos em benefício de empresa coligada ou que tenha sócio em comum <b>entram no limite</b>."],
    ["Situações excepcionadas", "A limitação geral não se aplica a grupos artísticos familiares, corpos artísticos estáveis e grupos e coletivos culturais ou artístico-culturais que atuem na execução do projeto (confira a redação e as condições no texto oficial)."],
    ["Fonte", FONTE_IN],
], "compact")}
{radar(1, "Remuneração do proponente",
       "Remuneração acima do limite sobre o valor captado; proponente pago sem função no orçamento; pagamentos a cônjuge/coligada/sócio não computados; remuneração lançada como “consultoria” em outra rubrica.",
       "Está entre 90% e 100% do limite; ou só fica dentro se captar 100%; ou você declarou enquadramento em exceção (confirme).",
       "Função descrita, quantidade real, soma de proponente + vinculados dentro do limite também no cenário de 50% de captação.")}
<p class="small"><b>Na planilha:</b> ORÇAMENTO coluna L (pessoa vinculada) + RADAR calculadora A + tabela “E se eu captar menos?”.</p>
"""))

add(P(M5, f"""
<div class="kicker">Radar · riscos 2 e 3</div>
<h2>2. Custos vinculados</h2>
{table(["O que são", "Limite", "Base", "Regras de execução"], [
    ["Custos de administração", "15%", "VALOR DO PROJETO", "Pagos proporcionalmente às parcelas captadas. 2026: regularização documental de patrimônio admitida; caiu a trava de 50% em uma única despesa."],
    ["Custos de acessibilidade, comunicação e divulgação acessíveis", "20%", "VALOR DO PROJETO", "Gastos proporcionalmente à captação. Inclui consultor/coordenador de acessibilidade e equipe treinada para PcD."],
], "compact")}
<p class="small"><b>Relação entre rubricas:</b> administração e acessibilidade têm limites <b>separados</b> — um não “empresta” espaço ao outro. Divulgação/comunicação comum tem limite próprio (20% do valor do projeto). Não classifique produção como administração para “aproveitar” espaço, nem administração como produção para fugir do limite.</p>
{radar(2, "Custos vinculados",
       "Administração acima de 15% do valor do projeto; despesa de produção disfarçada de administração (ou o contrário); acessibilidade zerada.",
       "Perto do limite (≥ 90%); itens administrativos genéricos (“apoio administrativo”) sem descrição.",
       "Cada item administrativo descrito; percentuais dentro dos limites; acessibilidade prevista e custeada.")}
{radar(3, "Captação",
       "Valor acima do menor entre 10% do valor do projeto e R$ 150.000; pagamento fixo independente do captado; serviço prestado ao incentivador; captador escondido em outra rubrica.",
       "Contrato de captação ainda sem cláusula de proporcionalidade; captador também é fornecedor de outros itens.",
       "Dentro do menor limite, pago proporcionalmente, serviço ao proponente, contrato claro.")}
<p class="tiny muted">Fonte: {FONTE_IN}.</p>
"""))

add(P(M5, f"""
<div class="kicker">Radar · riscos 4 e 5</div>
{radar(4, "Fornecedores",
       "Um mesmo fornecedor recebe mais de 20% do VALOR CAPTADO (somando todas as linhas dele) sem exceção aplicável; fornecedor fracionado em nomes/CNPJs diferentes para fugir do limite.",
       "Fornecedor entre 18% e 20% do captado; ou dentro do limite só se captar 100%.",
       "Nenhum fornecedor acima do limite no cenário de captação planejado; exceções confirmadas no texto oficial.",
       FONTE_IN + " — há exceções, como intervenções de conservação e restauro de bens culturais.")}
{box("do", "Como detectar automaticamente na planilha", "<p>Na aba ORÇAMENTO, a coluna <b>P</b> soma tudo o que um mesmo fornecedor recebe (fórmula SUMIFS pelo nome digitado na coluna I) e divide pelo <b>VALOR CAPTADO</b> do cenário. A coluna Q mostra 🔴 acima de 20% e 🟡 a partir de 18%. Digite o nome do fornecedor <b>sempre igual</b> (mesma grafia) para a soma funcionar.</p>")}
<h2>5. Cachês</h2>
{table(["Função", "Limite com recurso incentivado", "Base"], [
    ["Artista solo", "R$ 25.000", "por apresentação"], ["Grupo / coletivo", "R$ 50.000", "por apresentação"],
    ["Músico de orquestra", "R$ 5.000", "por apresentação"], ["Maestro / regente", "R$ 25.000", "por apresentação"],
    ["Palestrante / conferencista", "R$ 5.000", "por participação"],
], "compact")}
{radar(5, "Cachês",
       "Cachê acima do limite pago com incentivo sem aprovação da CNIC; cachê “por temporada” escondendo valor por apresentação acima do limite.",
       "Cachê próximo do limite; valores acima pretendidos com outras fontes (confirme e documente) ou pedido à CNIC.",
       "Unidade = apresentação; valor unitário dentro do limite; excedente, se houver, com fonte clara.",
       FONTE_IN + " (dispositivo sobre limites de cachê; valores superiores dependem de outras fontes ou de apreciação da CNIC)")}
"""))

add(P(M5, f"""
<div class="kicker">Radar · riscos 6 a 9</div>
{radar(6, "Divulgação",
       "Divulgação/comunicação acima de 20% do VALOR DO PROJETO; divulgação sem relação com o público do projeto; material sem as marcas obrigatórias.",
       "Perto do limite; impulsionamento sem segmentação; peças não previstas para aprovação do MinC.",
       "Plano de divulgação coerente com público e território, dentro do limite, com marcas e prazo para aprovação das peças.",
       FONTE_IN)}
{radar(7, "Administração",
       "Acima de 15% do VALOR DO PROJETO; itens de produção classificados como administração; despesas da instituição que existiriam sem o projeto.",
       "“Apoio administrativo” genérico; valor alto concentrado em um item (permitido em 2026, mas precisa de justificativa).",
       "Contador, tarifas, materiais do projeto — descritos e dentro do limite.",
       FONTE_IN)}
{radar(8, "Acessibilidade",
       "Nenhuma medida prevista; texto genérico; medida prometida sem custo no orçamento.",
       "Só um tipo de medida (ex.: só rampa) quando o produto exige comunicacional também.",
       "Medidas físicas, comunicacionais e atitudinais por produto, com custo e responsável.",
       FONTE_IN + " · notícia oficial do MinC sobre acessibilidade")}
{radar(9, "Democratização do acesso",
       "Faixas promocionais acima de 10% cada; gratuidade social/educativa abaixo de 10%; preço popular abaixo de 20% ou acima de R$ 50 (quando há venda).",
       "Projeto 100% gratuito sem explicar como está registrado no plano de distribuição; preço médio sem conferência.",
       "Faixas conferidas na aba DISTRIBUICAO; medidas descritas com números e locais.",
       FONTE_IN + " (dispositivo do plano de distribuição)")}
"""))

add(P(M5, f"""
<div class="kicker">Radar · riscos 10 a 13</div>
{radar(10, "Outras fontes",
       "Fonte declarada que não existe ou não está comprometida; valores de outras fontes que não aparecem no orçamento.",
       "Fonte em negociação (sem documento).",
       "Carta/contrato; linhas do orçamento com Fonte = “Outras fontes” somam exatamente o valor declarado.")}
<div class="rule" style="font-size:13pt">11. DUPLA COBERTURA<br>“Esta mesma despesa está sendo financiada por outra fonte?”<small>Se a resposta for SIM, a despesa precisa sair de uma das fontes. Coluna O do ORÇAMENTO → 🔴 automático.</small></div>
{radar(11, "Dupla cobertura",
       "Mesma despesa no incentivo e em outra fonte (edital, patrocínio direto, prefeitura).",
       "Despesas parecidas em fontes diferentes sem descrição que diferencie.",
       "Cada despesa tem uma única fonte, descrita de forma inequívoca.")}
{radar(12, "Despesa sem vínculo",
       "Qualquer despesa sem relação direta com o objeto do projeto; coluna M vazia.",
       "Justificativa vaga (“apoio”, “geral”, “diversos”).",
       "Justificativa aponta a etapa da metodologia e o produto.")}
{radar(13, "Preço fora do mercado",
       "Valor unitário muito acima ou abaixo das referências sem explicação.",
       "Sem cotação para itens relevantes; preços de outro ano/cidade.",
       "Cotações ou referências guardadas; coluna N = “Sim”.")}
"""))

add(P(M5, f"""
<div class="kicker">Radar · risco 14</div><h2>14. Inconsistência</h2>
{table(["Alerta", "Pergunta de teste", "Onde verificar"], [
    ["objetivos ≠ metas", "Todo objetivo tem meta com número?", "MATRIZ — Objetivo x Meta"],
    ["metas ≠ produtos", "Toda meta vira produto no plano de distribuição?", "MATRIZ — Meta x Produto"],
    ["produtos ≠ orçamento", "Todo produto tem despesa? Sobrou despesa sem produto?", "MATRIZ — Produto x Orçamento"],
    ["cronograma ≠ atividades", "Toda atividade da metodologia tem data?", "CRONOGRAMA + MATRIZ"],
    ["público ≠ plano de distribuição", "O público descrito bate com as faixas e locais?", "DISTRIBUICAO + MATRIZ"],
    ["orçamento ≠ metodologia", "Toda despesa aponta uma etapa da metodologia?", "ORÇAMENTO coluna M"],
], "compact")}
{radar(14, "Inconsistência",
       "Qualquer linha 🔴 INCONSISTENTE na Matriz (item do orçamento ou atividade que não existe; 3+ campos vazios).",
       "Linhas 🟡 REVISAR (algum campo vazio).",
       "Todas as linhas 🟢 COERENTE e as 6 perguntas respondidas “Sim”.")}
{check("CHECKLIST DE CONSISTÊNCIA", ["Mesmos números de público em resumo, objetivos, metas e distribuição.", "Mesmas datas em período, cronograma e metodologia.", "Mesmos nomes de produtos em objetivos, distribuição e orçamento.", "Nenhuma etapa sem despesa (ou justificativa).", "Nenhuma despesa sem etapa."])}
<h3>Resumo do radar — marque o seu status</h3>
{table(["#", "Risco", "🔴", "🟡", "🟢"], [[str(i), r, "☐", "☐", "☐"] for i, r in enumerate(["Remuneração do proponente", "Custos vinculados", "Captação", "Fornecedores", "Cachês", "Divulgação", "Administração", "Acessibilidade", "Democratização", "Outras fontes", "Dupla cobertura", "Despesa sem vínculo", "Preço fora do mercado", "Inconsistência"], 1)], "compact")}
"""))

# =================================================================== MÓDULO 6
M6 = "Módulo 6 · Acessibilidade e democratização"
add(divider("06", "Acessibilidade e democratização do acesso", "Não é texto burocrático. São medidas concretas, com custo, local e responsável — e a análise vai procurar exatamente isso.", M6))
add(P(M6, f"""
<div class="kicker">Módulo 6 · Capítulo 6.1</div><h2>Acessibilidade</h2>
{chapter(
    f"<p>{NEW} A IN 29/2026 reforça a obrigatoriedade de medidas de acessibilidade <b>física</b> (acesso, circulação, rampas, assentos), <b>comunicacional</b> (Libras, audiodescrição, legendas, materiais acessíveis) e <b>atitudinal</b> (equipe orientada, atendimento, acolhimento). Custos de consultor/coordenador de acessibilidade, equipe treinada e estruturas temporárias (rampas e plataformas removíveis) são admitidos, dentro do limite de 20% do valor do projeto.</p>",
    ul(["Para <b>cada produto</b>, pergunte: quem poderia ficar de fora? Que barreira existe?", "Escolha as medidas que se aplicam ao formato (presencial, digital, publicação, exposição).", "Coloque cada medida no orçamento com unidade e quantidade.", "Diga no Salic: qual medida, em qual produto, em quais sessões/locais.", "Planeje a comprovação (fotos, vídeo com janela de Libras, contratos)."]),
    ul(["Copiar parágrafo genérico sobre “inclusão”.", "Prometer Libras em todas as sessões e orçar para duas.", "Local sem acessibilidade física e sem solução prevista.", "Divulgação sem versão acessível."]),
    ["Cada produto tem medida física, comunicacional e atitudinal (quando aplicável).", "Toda medida tem custo ou justificativa de custo zero.", "Custos dentro de 20% do valor do projeto.", "Texto específico, sem cópia."], "CHECKLIST DE ACESSIBILIDADE"
)}
"""))

add(P(M6, f"""
<div class="kicker">Módulo 6 · Ferramenta</div><h2>Matriz de acessibilidade por produto</h2>
{table(["Produto", "Barreira possível", "Medida física", "Medida comunicacional", "Medida atitudinal", "Custo (linha do orçamento)", "Comprovação"], [
    ["Apresentação ao ar livre", "Terreno irregular; público surdo/cego", "Rampas removíveis, área reservada", "Libras, audiodescrição", "Equipe orientada para receber PcD", "Rampas; Intérprete; Audiodescrição; Consultoria", "Fotos, vídeo, contratos"],
    ["Oficina", "Sala sem acesso; material só visual", "Sala térrea/acessível", "Material em formato acessível", "Inscrição com pergunta sobre necessidades", "Material acessível", "Lista de presença, fotos"],
    ["Livro/publicação", "Leitores com deficiência visual", "—", "Versão acessível (ex.: digital acessível, audiolivro)", "—", "Produção da versão acessível", "Arquivo/entrega"],
    ["Vídeo/conteúdo digital", "Pessoas surdas/cegas", "—", "Legendas, Libras, audiodescrição", "—", "Legendagem; Libras; AD", "Link do conteúdo"],
    ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
], "compact")}
{box("warn", "Como escrever no Salic (modelo)", "<p><i>“Nas 8 apresentações, haverá intérprete de Libras e audiodescrição ao vivo (itens X e Y do orçamento), rampas removíveis e área reservada nas 4 praças (item Z) e equipe orientada por consultoria de acessibilidade (item W), que também revisará as peças de divulgação em formato acessível.”</i> Substitua pelos seus itens reais.</p>")}
"""))

add(P(M6, f"""
<div class="kicker">Módulo 6 · Capítulo 6.2</div><h2>Democratização do acesso e plano de distribuição</h2>
{table(["Faixa (plano de distribuição)", "Limite", "Base"], [
    ["Distribuição gratuita promocional pelo patrocinador", "até 10%", "total de ingressos/produtos"],
    ["Distribuição gratuita promocional pelo proponente (divulgação)", "até 10%", "total de ingressos/produtos"],
    ["Distribuição gratuita com caráter social ou educativo", "mínimo 10%", "total de ingressos/produtos"],
    ["Comercialização a preço popular", "mínimo 20%, a no máximo R$ 50", "total de ingressos/produtos"],
], "compact")}
<p class="tiny muted">Fonte: {FONTE_IN} (dispositivo do plano de distribuição). Algumas fontes citam também teto de preço médio de ingresso — confira o valor no texto oficial; na planilha ele é um parâmetro editável marcado como “CONFIRA”.</p>
{chapter(
    "<p>O plano de distribuição diz <b>quantos</b> ingressos/produtos existem e <b>como</b> chegam ao público: gratuitos, promocionais, a preço popular, comercializados. Democratização é o conjunto de medidas que ampliam o acesso de quem normalmente fica de fora.</p>",
    ul(["Liste cada produto e a quantidade total.", "Distribua por faixa e confira os limites na aba DISTRIBUICAO.", "Diga para quem vai a gratuidade social/educativa (escolas, ONGs, comunidades).", "Se houver venda, defina preço popular e preço médio.", "Descreva medidas adicionais de ampliação de acesso (locais, horários, transporte, ações formativas)."]),
    ul(["Faixas promocionais maiores que o permitido.", "“Gratuito” no texto e venda no plano de distribuição.", "Gratuidade social sem destinatário.", "Público estimado maior que a capacidade dos locais."]),
    ["Faixas dentro dos limites.", "Destinatários da gratuidade identificados.", "Preços conferidos.", "Medidas de democratização com números."], "CHECKLIST DE DEMOCRATIZAÇÃO"
)}
"""))

# =================================================================== MÓDULO 7
M7 = "Módulo 7 · Cronograma"
add(P(M7, f"""
<div class="kicker">Módulo 7</div><h1>Cronograma que o orçamento consegue pagar</h1>
<div class="rule">NÃO PROMETA NO CRONOGRAMA AQUILO QUE O ORÇAMENTO NÃO CONSEGUE EXECUTAR.<small>Na planilha, atividade em etapa sem despesa gera 🟡 “Etapa sem despesa no orçamento: quem paga?”.</small></div>
{chapter(
    f"<p>O cronograma organiza as atividades no tempo, por etapa: <b>pré-produção, produção, pós-produção, divulgação, execução e encerramento</b>. {NEW} Projetos são cadastrados com prazo máximo de <b>36 meses</b> de execução, que deve refletir a realidade; e deixou de existir a exigência de apresentar a proposta com 30 dias de antecedência do início da execução.</p>",
    ul(["Liste atividades da metodologia (verbo + objeto: “Realizar oficinas”).", "Dê início, fim e responsável a cada uma.", "Divulgação começa antes das atividades com público.", "Reserve tempo para encerramento e prestação de contas.", "Considere o tempo de captação: a execução depende de recursos captados."]),
    ul(["Atividade com fim antes do início.", "Tudo concentrado em um mês “para caber”.", "Divulgação depois do evento.", "Esquecer encerramento.", "Cronograma promete 12 oficinas; orçamento paga 4."]),
    ["Todas as atividades têm datas e responsável.", "Nenhum 🔴 na coluna ALERTAS.", "Nenhum 🟡 de etapa sem despesa (ou justificado).", "Encerramento previsto.", "Período total ≤ 36 meses."]
)}
"""))

add(P(M7, f"""
<div class="kicker">Ferramenta · PLANILHA DE CRONOGRAMA (aba CRONOGRAMA)</div><h2>Modelo de preenchimento</h2>
{table(["Atividade", "Etapa", "Início", "Fim", "Duração", "Responsável", "Observações"], [
    ["Mapeamento das praças e autorizações", "Pré-produção", "01/02", "20/02", "20 dias", "Produtora", "Autorização da prefeitura"],
    ["Plano de acessibilidade e treinamento", "Acessibilidade", "10/02", "28/02", "19 dias", "Consultor", "—"],
    ["Campanha de divulgação", "Divulgação", "20/02", "15/06", "116 dias", "Comunicação", "Peças aprovadas pelo MinC"],
    ["Apresentações (8)", "Produção", "06/03", "20/06", "107 dias", "Grupo", "Sábados"],
    ["Oficinas (4)", "Produção", "13/03", "13/06", "93 dias", "Arte-educador", "—"],
    ["Edição do registro", "Pós-produção", "21/06", "15/07", "25 dias", "Audiovisual", "—"],
    ["Relatório e prestação de contas", "Encerramento", "01/07", "31/07", "31 dias", "Proponente", "Contador apoia"],
    ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
], "compact")}
<p class="small"><b>Na planilha:</b> a duração é calculada sozinha, as barras mensais aparecem em laranja e a coluna ALERTAS marca datas invertidas, atividades fora do período e etapas sem despesa.</p>
"""))

# =================================================================== MÓDULO 8
M8 = "Módulo 8 · Documentação"
docs_rows = [
    ["<b>DOCUMENTOS DO PROPONENTE</b>", "", "", "", "", ""],
    ["Cadastro completo no Salic (PF ou PJ)", "Sim", "☐", "☐", "—", "Base de tudo"],
    ["Identificação do proponente/responsável legal", "Conforme Manual", "☐", "☐", "", "Confira o que o Salic pede"],
    ["CNPJ, ato constitutivo/estatuto/contrato social, ata de eleição (PJ)", "Sim p/ PJ", "☐", "☐", "", "Natureza cultural"],
    ["Comprovação de atuação cultural (portfólio no Salic)", "Depende", "☐", "☐", "—", "Dispensa: 1º projeto até R$ 200 mil"],
    ["Procuração", "Eventual", "☐", "☐", "", "Só se houver procurador"],
    ["<b>DOCUMENTOS DO PROJETO</b>", "", "", "", "", ""],
    ["Currículo/portfólio dos principais profissionais", "Conforme Manual", "☐", "☐", "—", ""],
    ["Cartas de anuência dos principais participantes", "Conforme segmento", "☐", "☐", "", "Datadas e assinadas"],
    ["Anuência/autorização do local", "Conforme segmento", "☐", "☐", "", "Local de terceiros"],
    ["<b>DOCUMENTOS ESPECÍFICOS</b>", "", "", "", "", ""],
    ["Documentos exigidos para o segmento (ex.: patrimônio, audiovisual, livro, plano anual)", "Depende do segmento", "☐", "☐", "", "Veja a lista do segmento"],
    ["Autorização de órgão de patrimônio (bens tombados)", "Depende", "☐", "☐", "", "Iphan/estado/município"],
    ["Cessão/autorização de direitos autorais", "Depende", "☐", "☐", "", "Obras de terceiros"],
    ["<b>DOCUMENTOS EVENTUAIS</b>", "", "", "", "", ""],
    ["Comprovantes de outras fontes (cartas de compromisso)", "Eventual", "☐", "☐", "", "Só fonte que existe"],
    ["Cotações/referências de preço", "Recomendado", "☐", "☐", "", "Para diligências"],
    ["Documentos pedidos em diligência", "Eventual", "☐", "☐", "", "Responder no prazo"],
]
add(P(M8, f"""
<div class="kicker">Módulo 8</div><h1>Checklist de documentação da apresentação</h1>
{box("warn", "Importante", f"<p>Este checklist <b>organiza</b>; a lista oficial está no Manual do Proponente e na IN 29/2026 (e anexos), e varia conforme o tipo de proponente e o segmento. Não foram inventados documentos: onde a exigência depende do caso, está marcado “Depende”/“Conforme”. {NEW} Documentos obrigatórios devem ser anexados na apresentação.</p>")}
{table(["DOCUMENTO", "OBRIGATÓRIO?", "APLICÁVEL AO MEU PROJETO?", "JÁ TENHO?", "VALIDADE", "OBSERVAÇÃO"], docs_rows, "compact")}
"""))

add(P(M8, f"""
<div class="kicker">Módulo 8 · Capítulo 8.1</div><h2>Como não perder a proposta por causa de papel</h2>
{chapter(
    "<p>Documentação é a parte “chata” que mais derruba iniciantes: arquivo errado, vencido, ilegível ou esquecido.</p>",
    ul(["Baixe o Manual do Proponente IN 2026 e liste os documentos do seu tipo e segmento na aba CHECKLIST DOCUMENTOS.", "Marque “Aplicável?” e “Já tenho?” para cada um.", "Anote validades — a planilha pinta de amarelo o que vence em 30 dias e de vermelho o que já venceu.", "Padronize nomes de arquivo: <i>NN_Tipo_Nome.pdf</i>.", "Anexe tudo antes de clicar em enviar."]),
    ul(["Carta de anuência sem assinatura ou data.", "Estatuto desatualizado.", "Arquivo corrompido ou em formato não aceito.", "Descobrir o documento específico do segmento na diligência."]),
    ["Lista oficial conferida.", "Todos os aplicáveis = “Já tenho”.", "Nada vencido.", "Arquivos legíveis e nomeados."]
)}
"""))

# =================================================================== MÓDULO 9
M9 = "Módulo 9 · Checklist final"
blocks = []
cur = None
for b, t, onde in ITENS:
    if b != cur:
        blocks.append(f'<div class="fc-h">{b}</div>')
        cur = b
    blocks.append(f'<div class="fc"><span>{ITENS.index((b, t, onde)) + 1}.</span><span>{t}</span><span class="opts">☐ SIM ☐ NÃO ☐ N/A</span></div>')
half = len(blocks) // 2
# divide em 3 páginas aproximadamente iguais sem quebrar cabeçalho de bloco
chunks = [[], [], []]
per = len(ITENS) / 3
count = 0
for html in blocks:
    idx = min(int(count // per), 2) if 'fc-h' not in html else min(int(count // per), 2)
    chunks[idx].append(html)
    if 'class="fc"' in html:
        count += 1
titles = ["CHECKLIST FINAL “ANTES DE CLICAR EM ENVIAR” (1/3)", "CHECKLIST FINAL (2/3)", "CHECKLIST FINAL (3/3)"]
for k, ch in enumerate(chunks):
    extra = ""
    if k == 0:
        extra = '<p class="lead">54 verificações em 14 blocos (A a N). Meta: zero NÃO. Também na aba CHECKLIST FINAL da planilha, com contagem automática.</p>'
    if k == 2:
        extra_end = box("do", "Resultado", "<p><b>Zero NÃO</b> + pendências do Salic zeradas → envie e salve o comprovante. <b>Algum NÃO</b> → volte à aba indicada em “Onde corrigir” na planilha.</p>")
    else:
        extra_end = ""
    add(P(M9, f'<div class="kicker">Módulo 9</div><h1 style="font-size:18pt">{titles[k]}</h1>{extra}{"".join(ch)}{extra_end}'))

# =================================================================== PLANILHAS
MP = "Ferramentas"
add(P(MP, f"""
<div class="kicker">As planilhas</div><h1>7 planilhas + calculadoras: como usar</h1>
{table(["Planilha", "O que você preenche", "O que ela faz sozinha"], [
    ["1 · MAPA DO PROJETO", "Nome, área, segmento, resumo, objetivos, justificativa, metodologia, público, beneficiários, produtos, metas, local, período, etapas, resultados.", "Status 🔴 vazio / 🟡 curto / 🟢 preenchido e contagem de caracteres."],
    ["2 · ORÇAMENTO", "Etapa, item, descrição, unidade, quantidade, valor unitário, fonte, fornecedor, observação + colunas de conferência (categoria, pessoa vinculada, por que existe, preço conferido, outra fonte).", "Valor total, totais por fonte, % por fornecedor sobre o captado e alertas automáticos por linha."],
    ["3 · CRONOGRAMA", "Atividade, etapa, início, fim, responsável, observações.", "Duração, gráfico mensal, alertas de data, período e etapa sem despesa."],
    ["4 · RADAR DE LIMITES", "Tipo de proponente, exceção, cenário de captação, 1º projeto, carteira, beneficiários.", "Calculadoras A–J com base de cálculo correta e status 🟢🟡🔴 + simulação de captação parcial."],
    ["5 · CHECKLIST SALIC", "Preparado? Revisado?", "Contagem do que falta."],
    ["6 · CHECKLIST DOCUMENTOS", "Aplicável? Já tenho? Validade.", "Pendentes e vencimentos em 30 dias."],
    ["7 · MATRIZ CONSISTENCIA", "Objetivo → meta → produto → item do orçamento → atividade → público.", "Confere se item e atividade existem nas outras abas; 🟢 COERENTE / 🟡 REVISAR / 🔴 INCONSISTENTE."],
    ["+ DISTRIBUICAO", "Quantidades por faixa, preços.", "Calculadora F com limites mínimos e máximos."],
    ["+ PARAMETROS", "Nada (só se a norma mudar).", "Guarda todos os limites usados nas fórmulas."],
    ["+ CHECKLIST FINAL / CONTROLE NORMATIVO", "SIM/NÃO/N/A; datas de conferência.", "Resultado “pronto” ou “não envie ainda”."],
], "compact")}
{box("warn", "Base de cálculo nas fórmulas", "<p>Remuneração do proponente e fornecedor usam <b>VALOR CAPTADO</b> (célula RADAR!B12 = valor do projeto × cenário de captação). Administração, divulgação, acessibilidade e captação usam <b>VALOR DO PROJETO</b> (RADAR!B9). Se o Salic exibir um valor do projeto diferente da soma da planilha, digite-o em RADAR!B8 e ele passa a valer.</p>")}
"""))

calc_rows = [
    ["A · Remuneração do proponente", "Soma: categoria “Remuneração do proponente” + linhas com pessoa vinculada = Sim (fonte incentivo)", "VALOR CAPTADO", "30% (PF/MEI) ou 20% (demais)", "=B/Base", "🔴 >limite · 🟡 ≥90% ou exceção declarada · 🟢"],
    ["B · Fornecedor", "Maior soma de um mesmo fornecedor (incentivo)", "VALOR CAPTADO", "20%", "=B/Base", "idem"],
    ["C · Administração", "Soma da categoria", "VALOR DO PROJETO", "15%", "=B/Base", "idem"],
    ["D1 · Acessibilidade/com./div. acessíveis", "Soma da categoria", "VALOR DO PROJETO", "20%", "=B/Base", "idem + 🔴 se zero"],
    ["D2 · Divulgação/comunicação", "Soma da categoria", "VALOR DO PROJETO", "20%", "=B/Base", "idem"],
    ["E · Captação", "Soma da categoria", "VALOR DO PROJETO", "MÍN(10% × base; R$ 150.000)", "=B/Base", "compara em R$"],
    ["F · Distribuição", "Quantidades por faixa", "Total de ingressos/produtos", "máx. 10% / 10%; mín. 10% / 20%; R$ 50", "=faixa/total", "🔴 fora · 🟡 verificar · 🟢"],
    ["G · % por categoria", "Soma de cada categoria", "VALOR DO PROJETO", "conforme rubrica", "=cat/Base", "informativo"],
    ["H · Valor por beneficiário", "Valor total do projeto", "Nº de beneficiários", "sem limite normativo", "=total/benef.", "teste de razoabilidade"],
]
FORMULAS_TBL = table(["Onde", "Fórmula"], [
    ["ORÇAMENTO G (valor total)", "=IF(OR(E8=\"\",F8=\"\"),\"\",E8*F8)"],
    ["ORÇAMENTO P (% fornecedor)", "=SUMIFS(G:G; I:I; I8; H:H; \"Incentivo*\") / VALOR_CAPTADO"],
    ["RADAR B12 (valor captado)", "=VALOR_PROJETO × cenário de captação (B11)"],
    ["RADAR A (limite)", "=IF(OR(tipo=\"Pessoa física\";tipo=\"MEI\"); 30%; 20%)"],
    ["RADAR E (limite captação)", "=MIN(10% × VALOR_PROJETO; 150000)"],
    ["Status padrão", "=IF(pct>lim;\"🔴 ACIMA DO LIMITE\";IF(pct>=lim×0,9;\"🟡 VERIFICAR\";\"🟢 DENTRO DO LIMITE\"))"],
    ["CRONOGRAMA E (duração)", "=D8−C8+1"],
    ["MATRIZ G (item existe?)", "=IF(COUNTIF(ORÇAMENTO!B:B; D5)>0;\"Sim\";\"Não\")"],
], "compact")
add(P(MP, f"""
<div class="kicker">As calculadoras</div><h1>Calculadoras A–H: o que cada coluna mostra</h1>
<p>Toda calculadora exibe: <b>VALOR INFORMADO · BASE DE CÁLCULO · LIMITE APLICÁVEL · PERCENTUAL RESULTANTE · STATUS · OBSERVAÇÃO</b>.</p>
{table(["Calculadora", "Valor informado", "Base de cálculo", "Limite aplicável", "Percentual", "Status"], calc_rows, "compact")}
<h3>Fórmulas principais (Excel / Google Sheets)</h3>
{FORMULAS_TBL}
<p class="tiny muted">Os nomes VALOR_PROJETO, VALOR_CAPTADO, L_ADM etc. são intervalos nomeados definidos na planilha. No Google Sheets, o separador de argumentos pode ser “;” ou “,” conforme a localidade; o arquivo já vem pronto.</p>
"""))

add(P(MP, f"""
<div class="kicker">Demonstração · projeto-exemplo</div><h1>O que o Radar mostrou no exemplo</h1>
{table(["Calculadora", "Valor informado", "Base", "Limite", "Resultado", "Status"], [
    ["A · Remuneração do proponente (PF)", "R$ 24.000", "Captado R$ 184.360", "30%", "13,0%", "🟢 DENTRO DO LIMITE"],
    ["B · Maior fornecedor (grupo teatral)", "R$ 48.000", "Captado R$ 184.360", "20%", "26,0%", "🔴 ACIMA DO LIMITE"],
    ["C · Administração", "R$ 4.560", "Projeto R$ 184.360", "15%", "2,5%", "🟢"],
    ["D1 · Acessibilidade", "R$ 16.200", "Projeto R$ 184.360", "20%", "8,8%", "🟢"],
    ["D2 · Divulgação", "R$ 13.500", "Projeto R$ 184.360", "20%", "7,3%", "🟢"],
    ["E · Captação", "R$ 9.000", "Projeto R$ 184.360", "R$ 18.436", "4,9%", "🟢"],
    ["I · Primeiro projeto", "R$ 185.560", "maior entre projeto e total", "R$ 200.000", "—", "🟢 pode estar dispensado — confira"],
], "compact")}
{box("wrong", "O erro que o Radar pegou", "<p>O cachê do grupo, pago a um único fornecedor, soma 26% do valor captado. Antes de enviar: confirmar se há exceção aplicável; se não houver, reduzir o valor/quantidade ou mover parte para outras fontes confirmadas. Fracionar o fornecedor é irregular.</p>")}
{box("warn", "Os alertas amarelos do exemplo", ul(["Registro audiovisual sem preço de mercado conferido → fazer cotação.", "Lanche das oficinas em outras fontes → anexar carta do apoiador.", "Etapa de encerramento sem despesa → justificar (contador em administração cobre) ou prever custo.", "Plano de distribuição 100% gratuito → confirmar como declarar a faixa de preço popular."]))}
"""))

# =================================================================== 12 ERROS
ME = "Erros concretos"
erros = [
    ("Começar pelo Salic", "Abrir o sistema e “ir escrevendo”. A sessão expira, os números mudam de um campo para outro.", "Mapa do Projeto pronto antes do login."),
    ("Orçamento desconectado da metodologia", "Despesas que nenhuma etapa explica; etapas sem despesa.", "Coluna M + Matriz de consistência."),
    ("Usar regra antiga", "Cachê de R$ 3 mil, 16 projetos para PJ, documento “depois”, 30 dias de antecedência.", "Tabela de regras antigas + PARAMETROS."),
    ("Confundir valor do projeto com valor captado", "Calcular remuneração sobre o valor do projeto e descobrir o estouro quando a captação é parcial.", "RADAR: cenários 75% e 50%."),
    ("Ultrapassar o limite de remuneração", "Somar só o proponente e esquecer cônjuge, coligada, sócio em comum.", "Coluna L (pessoa vinculada) + calculadora A."),
    ("Esconder remuneração em outra rubrica", "“Consultoria” ou “direção” que na verdade é o proponente.", "Classificação pela natureza real do serviço."),
    ("Fornecedor acima do limite", "Um fornecedor com várias linhas que, somadas, passam de 20% do captado.", "Coluna P do ORÇAMENTO + calculadora B."),
    ("Esquecer acessibilidade", "Parágrafo genérico, sem custo, sem medida por produto.", "Matriz de acessibilidade + calculadora D1."),
    ("Esquecer democratização", "Faixas fora dos limites; gratuidade sem destinatário.", "Aba DISTRIBUICAO."),
    ("Despesas sem vínculo", "“Despesas gerais”, “diversos”, bens permanentes sem justificativa.", "Regra de ouro: sem explicação, sem despesa."),
    ("Cronograma incompatível", "Datas invertidas, divulgação depois do evento, 12 oficinas no cronograma e 4 no orçamento.", "Alertas do CRONOGRAMA."),
    ("Documentação inadequada", "Vencida, ilegível, sem assinatura ou deixada para depois.", "CHECKLIST DOCUMENTOS com validade."),
]
add(P(ME, f"""
<div class="kicker">Alto valor percebido</div><h1>12 erros concretos que derrubam iniciantes</h1>
{table(["#", "Erro", "Como ele aparece", "Como o kit evita"], [[str(i), f"<b>{a}</b>", b, c] for i, (a, b, c) in enumerate(erros[:7], 1)])}
"""))
add(P(ME, f"""
<div class="kicker">Alto valor percebido</div><h1>12 erros concretos (continuação)</h1>
{table(["#", "Erro", "Como ele aparece", "Como o kit evita"], [[str(i), f"<b>{a}</b>", b, c] for i, (a, b, c) in enumerate(erros[7:], 8)])}
{box("warn", "Nenhum destes erros tem a ver com talento", "<p>Todos são <b>operacionais</b>: base de cálculo, classificação, coerência e prazo. Por isso dá para reduzi-los com método — e é exatamente isso que o kit faz. O mérito cultural e a decisão continuam sendo da análise oficial.</p>")}
"""))

# =================================================================== 72H
MD = "Desafio de 72 horas"
dias = [
    ("DIA 1 — ESTRUTURE", "Sair com o projeto inteiro escrito fora do Salic.",
     ["Checklist “Posso começar?” (20 min).", "Ler regras antigas × 2026 e os 6 valores (20 min).", "Preencher o Mapa do Projeto inteiro (2–3 h).", "Preencher a Matriz de consistência só com objetivos, metas e produtos (30 min).", "Separar documentos e anotar validades (40 min)."],
     "PDF Módulos 1–2 · abas MAPA DO PROJETO, MATRIZ, CHECKLIST DOCUMENTOS", "Mapa 100% 🟢; lista de documentos com pendências conhecidas."),
    ("DIA 2 — ORÇAMENTO + CRONOGRAMA", "Transformar metodologia em números e datas coerentes.",
     ["Lançar o orçamento etapa por etapa (2–3 h).", "Preencher colunas de conferência K–O (40 min).", "Montar cronograma (1 h).", "Plano de distribuição (30 min).", "Rodar o RADAR em 100%, 75% e 50% de captação e corrigir 🔴 (1 h)."],
     "PDF Módulos 4–7 · abas ORÇAMENTO, CRONOGRAMA, DISTRIBUICAO, RADAR", "Zero 🔴 no Radar; alertas 🟡 justificados."),
    ("DIA 3 — REVISÃO + SALIC", "Preencher, revisar e enviar.",
     ["Checklist final (40 min) — meta: zero NÃO.", "Conferir a norma oficial e anotar no Controle Normativo (15 min).", "Entrar no Salic e preencher seguindo o Mapa do Salic (2–3 h).", "Anexar documentos (30 min).", "Zerar pendências, enviar e salvar comprovante (20 min)."],
     "PDF Módulos 3, 8, 9 · abas CHECKLIST SALIC, CHECKLIST FINAL", "Proposta enviada, com comprovante salvo."),
]
for i, (t, obj, tarefas, ferr, res) in enumerate(dias):
    if i == 0:
        head = '<div class="kicker">Execução rápida</div><h1>Desafio de 72 horas</h1><p class="lead">Três dias de trabalho focado. Pode ser em fins de semana seguidos — o importante é a ordem.</p>'
    else:
        head = ""
    html = head + f'<h2>{t}</h2>' + table(["", ""], [["<b>OBJETIVO</b>", obj], ["<b>TAREFAS</b>", ul(tarefas, True)], ["<b>FERRAMENTA</b>", ferr], ["<b>RESULTADO ESPERADO</b>", res]], "")
    if i == 0:
        PAGES.append(P(MD, html))
    elif i == 1:
        PAGES[-1]["html"] += html
    else:
        add(P(MD, html + box("warn", "Calendário sugerido para 2026", ul(["Até 16/10: Dia 1 concluído.", "Até 23/10: Dia 2 concluído.", "Até 28/10 (quarta-feira): Dia 3 concluído e proposta enviada.", "29 e 30/10: margem para imprevistos. 31/10/2026 é sábado."]))))

# =================================================================== FONTES
MF = "Fontes e controle"
add(P(MF, f"""
<div class="kicker">Fontes oficiais</div><h1>Onde conferir tudo</h1>
{table(["Fonte", "Para que usar", "Link"], [
    ["Instrução Normativa MinC nº 29/2026", "Todas as regras operacionais: limites, prazos, documentos, distribuição.", L_IN29],
    ["Lei nº 8.313/1991", "Base legal do Pronac e do incentivo fiscal.", L_LEI],
    ["Decreto nº 11.453/2023", "Regulamento dos mecanismos de fomento.", L_DEC],
    ["Manual do Proponente — IN 2026", "Passo a passo do Salic.", L_MANUAL],
    ["MinC — Apresente seu projeto", "Orientações oficiais de apresentação.", L_APRESENTE],
    ["MinC — Quem pode participar?", "Quem pode ser proponente.", L_QUEM],
    ["MinC — notícia da nova IN", "Resumo oficial das mudanças de 2026.", L_NOTICIA],
    ["MinC — notícia sobre acessibilidade", "Novas regras de acessibilidade.", L_NOT_ACESS],
    ["Participa + Brasil — consulta pública da IN 2026", "Histórico da construção da norma.", L_CONSULTA],
    ["IN MinC nº 23/2025 (REVOGADA)", "Só para comparar. Não use como regra.", L_IN23],
    ["Salic", "Sistema de apresentação de propostas.", L_SALIC],
], "compact")}
{box("warn", "Nota de verificação", "<p>As regras deste kit foram levantadas a partir de publicações que reproduzem o texto da IN MinC nº 29/2026 e de comunicados oficiais do MinC, com data de verificação de 25/09/2026. Onde a numeração exata do artigo não pôde ser confirmada literalmente, o kit indica “localize o dispositivo no texto oficial” em vez de arriscar um número. Antes de enviar, abra o link oficial e confira os números usados.</p>")}
"""))

add(P(MF, f"""
<div class="kicker">Controle de atualização normativa</div><h1>ÚLTIMA VERIFICAÇÃO NORMATIVA</h1>
{table(["Data", "Norma consultada", "Versão", "Alterações relevantes"], [
    ["25/09/2026", "IN MinC nº 29/2026", "29/01/2026 (DOU 30/01/2026)", "Base do kit. Revoga a IN 23/2025."],
    ["25/09/2026", "Lei 8.313/1991", "compilada", "Sem alteração relevante para este kit."],
    ["25/09/2026", "Decreto 11.453/2023", "vigente", "Sem alteração relevante para este kit."],
    ["25/09/2026", "Manual do Proponente IN 2026", "MinC", "Referência de telas do Salic."],
    ["___/___/___", "", "", ""], ["___/___/___", "", "", ""], ["___/___/___", "", "", ""], ["___/___/___", "", "", ""],
])}
{box("do", "Como atualizar o kit se a norma mudar", ul(["Abra a aba PARAMETROS da planilha.", "Altere o número da regra que mudou (célula amarela).", "Anote na aba CONTROLE NORMATIVO: data, norma, versão, o que mudou.", "Rode de novo o RADAR e o CHECKLIST FINAL."], True))}
"""))

add(P(MF, f"""
<div class="kicker">Aviso legal</div><h1>Disclaimer</h1>
<p>Este material é um <b>kit de organização e conferência</b> para quem vai apresentar uma proposta ao mecanismo de Incentivo a Projetos Culturais do Pronac (Lei Rouanet). Ele foi elaborado com base nas normas vigentes na data de verificação indicada (25/09/2026).</p>
{ul(["<b>Não há garantia de aprovação.</b> A admissão, a análise técnica, o parecer e a decisão sobre qualquer proposta são atribuições exclusivas do Ministério da Cultura e das instâncias previstas na norma (como a CNIC).",
     "<b>Não há garantia de captação.</b> A captação depende de incentivadores e de fatores fora do controle do proponente e deste material.",
     "<b>Não substitui análise profissional individualizada</b> (jurídica, contábil ou de elaboração de projetos) nem a leitura da legislação.",
     "<b>A norma prevalece.</b> Em caso de divergência entre este material e o texto oficial vigente (Lei 8.313/1991, Decreto 11.453/2023, IN MinC nº 29/2026, Manual do Proponente e atos posteriores), vale o texto oficial.",
     "Os sinais 🟢 das planilhas indicam apenas que o número informado está dentro do parâmetro configurado; não representam avaliação do Ministério da Cultura.",
     "O projeto usado como exemplo é fictício; seus valores são ilustrativos e não são referência de preço de mercado.",
     "Este material não tem vínculo com o Ministério da Cultura nem com o Governo Federal."])}
<div class="rule" style="margin-top:8mm">Você não precisa saber tudo sobre a Lei Rouanet.<br>Precisa fazer as coisas certas, na ordem certa, antes do prazo.<small>Volte à página 3 e comece pelo passo 1.</small></div>
"""))
