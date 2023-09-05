HEADER_XPATH = {
    "classe": "//span[contains(@id, 'classeProcesso')]/text()",
    "area": "//div[contains(@id, 'areaProcesso')]/span/text()",
    "assunto": "//span[contains(@id, 'assuntoProcesso')]/text()",
    "data_distribuicao": "//div[contains(@id, 'dataHoraDistribuicaoProcesso')]/text()",
    "juiz": "//td[contains(@class, 'descricaoMovimentacao')]/span[contains(normalize-space(), 'Nome do juiz')][1]/text()"
}

REGEX = {
    "distri": r"\d+\/\d+\/\d+",
    "juiz": r"Nome do juiz\(a\): (.+)\sNome"
}