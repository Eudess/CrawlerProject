GET_PROCESS_XPATH = "//div[contains(@class, 'header')]/input[contains(@id, 'processoSelecionado')]/@value"

HEADER_XPATH = {
    "general": "//div[contains(@id, '{}')]/span/text()",
    "classe": "//div[contains(@id, 'classeProcesso')]/span/text()",
    "area": "//div[contains(@id, 'areaProcesso')]/span/text()",
    "assunto": "//div[contains(@id, 'assuntoProcesso')]/span/text()",
    "juiz": "//table[3]//tbody//tr[contains(@class, 'fundoClaro')]/td[4]"
}

PARTES_XPATH = {
    "table": "//table[contains(@id, 'tableTodasPartes') or contains(@id, 'tablePartesPrincipais')]//tr",
    "papel": "./td/span[contains(@class, 'tipoDePartici')]/text()",
    "nome": "./td[contains(@class, 'nomeParteEAdvogado')]/text()"
}

MOVIMENTACOES_XPATH = {
    "table": "//tbody[contains(@id, 'tabelaTodasMovimentacoes')]//tr",
    "data": "./td[contains(@class, 'dataMovimentacao')]/text()",
    "texto": "./td[contains(@class, 'descricaoMovimentacao')]//text()"
}