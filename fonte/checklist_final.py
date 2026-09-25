# -*- coding: utf-8 -*-
"""Checklist final "ANTES DE CLICAR EM ENVIAR" — fonte única usada no PDF e na planilha."""

ITENS = [
    # A. PROPONENTE
    ("A. PROPONENTE", "Meu cadastro no Salic está completo, com e-mail e telefone que eu acompanho.", "Salic – cadastro"),
    ("A. PROPONENTE", "Sei se sou PF, MEI ou demais PJ e conferi o limite de projetos ativos e o teto global do meu tipo.", "RADAR – linha J"),
    ("A. PROPONENTE", "Se sou PJ, a finalidade cultural consta do ato constitutivo / atividade econômica.", "Documentos da PJ"),
    ("A. PROPONENTE", "Comprovação de atuação cultural cadastrada (portfólio) OU confirmei que estou na dispensa de primeiro projeto até R$ 200 mil.", "RADAR – linha I"),
    ("A. PROPONENTE", "Se alguém opera o Salic por mim, a procuração/vinculação está correta.", "Salic – cadastro"),
    # B. PROJETO
    ("B. PROJETO", "Nome do projeto claro e igual em todos os documentos.", "MAPA DO PROJETO"),
    ("B. PROJETO", "Área, segmento e enquadramento conferidos na tela de identificação.", "Salic – identificação"),
    ("B. PROJETO", "Resumo responde O QUÊ, ONDE, QUANDO, PARA QUEM e COMO.", "MAPA DO PROJETO"),
    ("B. PROJETO", "Período de execução dentro do limite de execução da IN 29/2026 (máx. 36 meses).", "CRONOGRAMA"),
    # C. OBJETIVOS
    ("C. OBJETIVOS", "O objetivo geral é uma frase, com verbo no infinitivo.", "MAPA DO PROJETO"),
    ("C. OBJETIVOS", "Cada objetivo específico tem pelo menos uma meta com número.", "MATRIZ – Objetivo x Meta"),
    ("C. OBJETIVOS", "Cada meta corresponde a um produto do plano de distribuição.", "MATRIZ – Meta x Produto"),
    # D. JUSTIFICATIVA
    ("D. JUSTIFICATIVA", "A justificativa fala do MEU território, público e lacuna (sem texto genérico).", "MAPA DO PROJETO"),
    ("D. JUSTIFICATIVA", "Explico por que eu/minha equipe tenho condições de executar.", "MAPA DO PROJETO"),
    ("D. JUSTIFICATIVA", "Relacionei o projeto às finalidades da Lei 8.313/1991.", "MAPA DO PROJETO"),
    # E. METODOLOGIA
    ("E. METODOLOGIA", "Cada etapa da metodologia tem atividade no cronograma.", "MATRIZ – Atividade x Cronograma"),
    ("E. METODOLOGIA", "Cada etapa da metodologia tem despesa no orçamento (ou explico por que não tem custo).", "CRONOGRAMA – alertas"),
    ("E. METODOLOGIA", "Ficou claro quem faz o quê (funções principais).", "MAPA DO PROJETO"),
    # F. PÚBLICO
    ("F. PÚBLICO", "Público-alvo descrito com perfil, território e estimativa numérica.", "MAPA DO PROJETO"),
    ("F. PÚBLICO", "Beneficiários de gratuidade/formação estão identificados.", "MAPA DO PROJETO"),
    ("F. PÚBLICO", "O público bate com as faixas do plano de distribuição.", "MATRIZ – Público x Distribuição"),
    # G. ACESSIBILIDADE
    ("G. ACESSIBILIDADE", "Previ medidas de acessibilidade física adequadas a cada local.", "CHECKLIST DE ACESSIBILIDADE"),
    ("G. ACESSIBILIDADE", "Previ medidas de acessibilidade comunicacional (ex.: Libras, audiodescrição, legendas) por produto.", "CHECKLIST DE ACESSIBILIDADE"),
    ("G. ACESSIBILIDADE", "Previ medidas atitudinais (equipe orientada, atendimento).", "CHECKLIST DE ACESSIBILIDADE"),
    ("G. ACESSIBILIDADE", "Toda medida de acessibilidade prometida tem custo no orçamento (ou explicação de por que não custa).", "ORÇAMENTO"),
    ("G. ACESSIBILIDADE", "Custos de acessibilidade/comunicação/divulgação acessíveis ≤ 20% do VALOR DO PROJETO.", "RADAR – linha D1"),
    # H. DEMOCRATIZAÇÃO
    ("H. DEMOCRATIZAÇÃO", "Faixas promocionais (patrocinador e proponente) dentro dos máximos.", "DISTRIBUICAO"),
    ("H. DEMOCRATIZAÇÃO", "Distribuição gratuita social/educativa e preço popular atingem os mínimos (ou o projeto é gratuito).", "DISTRIBUICAO"),
    ("H. DEMOCRATIZAÇÃO", "Preço popular e preço médio dentro dos tetos da norma vigente.", "DISTRIBUICAO"),
    ("H. DEMOCRATIZAÇÃO", "Descrevi a medida de democratização concreta (onde, para quem, quantos).", "Salic – democratização"),
    # I. CRONOGRAMA
    ("I. CRONOGRAMA", "Nenhuma atividade com fim antes do início ou fora do período do projeto.", "CRONOGRAMA – alertas"),
    ("I. CRONOGRAMA", "Divulgação acontece ANTES das atividades com público.", "CRONOGRAMA"),
    ("I. CRONOGRAMA", "Encerramento/prestação de contas está previsto.", "CRONOGRAMA"),
    ("I. CRONOGRAMA", "Não prometi no cronograma nada que o orçamento não paga.", "MATRIZ"),
    # J. ORÇAMENTO
    ("J. ORÇAMENTO", "Toda linha tem unidade, quantidade e valor unitário.", "ORÇAMENTO – alertas"),
    ("J. ORÇAMENTO", "Toda linha tem 'por que essa despesa existe' preenchido.", "ORÇAMENTO – coluna M"),
    ("J. ORÇAMENTO", "Preços conferidos com mercado (cotações/referências guardadas).", "ORÇAMENTO – coluna N"),
    ("J. ORÇAMENTO", "Remuneração do proponente (incluindo cônjuge/companheiro, coligada, sócio em comum) dentro do limite sobre o VALOR CAPTADO, e só por serviço efetivo.", "RADAR – linha A"),
    ("J. ORÇAMENTO", "Nenhum fornecedor acima do limite sobre o VALOR CAPTADO (ou exceção confirmada).", "RADAR – linha B"),
    ("J. ORÇAMENTO", "Administração ≤ 15% do VALOR DO PROJETO e sem despesa de produção disfarçada.", "RADAR – linha C"),
    ("J. ORÇAMENTO", "Divulgação dentro do limite sobre o VALOR DO PROJETO.", "RADAR – linha D2"),
    ("J. ORÇAMENTO", "Captação ≤ menor valor entre 10% do VALOR DO PROJETO e R$ 150.000.", "RADAR – linha E"),
    ("J. ORÇAMENTO", "Cachês dentro dos limites por apresentação (ou uso de outras fontes/CNIC justificado).", "ORÇAMENTO – alertas"),
    ("J. ORÇAMENTO", "Testei o cenário de captação parcial (75% e 50%).", "RADAR – cenários"),
    # K. FONTES DE RECURSOS
    ("K. FONTES DE RECURSOS", "Só declarei outras fontes que existem e estão comprometidas (carta/contrato).", "CHECKLIST DOCUMENTOS"),
    ("K. FONTES DE RECURSOS", "Nenhuma despesa está coberta por duas fontes (sem dupla cobertura).", "ORÇAMENTO – coluna O"),
    # L. DOCUMENTOS
    ("L. DOCUMENTOS", "Todos os documentos obrigatórios estão anexados ANTES do envio.", "CHECKLIST DOCUMENTOS"),
    ("L. DOCUMENTOS", "Documentos legíveis, dentro da validade e com nome de arquivo claro.", "CHECKLIST DOCUMENTOS"),
    # M. CONFORMIDADE
    ("M. CONFORMIDADE", "Conferi os limites no texto oficial vigente (e não em material de anos anteriores).", "CONTROLE NORMATIVO"),
    ("M. CONFORMIDADE", "Nenhuma remuneração do proponente escondida em outra rubrica.", "ORÇAMENTO – coluna L"),
    ("M. CONFORMIDADE", "Nenhuma despesa sem vínculo direto com o objeto do projeto.", "ORÇAMENTO – alertas"),
    # N. REVISÃO FINAL
    ("N. REVISÃO FINAL", "Li a proposta inteira em voz alta, do começo ao fim, uma vez.", "—"),
    ("N. REVISÃO FINAL", "Números iguais em todos os campos (metas, público, datas, valores).", "MATRIZ"),
    ("N. REVISÃO FINAL", "Lista de pendências do Salic está zerada e salvei comprovante do envio.", "Salic"),
]
