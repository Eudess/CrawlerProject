from ..constants.extract import *

def extract_header(response):
    classe = response.xpath(HEADER_XPATH["classe"]).get()
    area = response.xpath(HEADER_XPATH["area"]).get()
    assunto = response.xpath(HEADER_XPATH["assunto"]).get()
    data_distribuicao = response.xpath(HEADER_XPATH["data_distribuicao"]).re_first(REGEX["distri"])
    juiz = response.xpath(HEADER_XPATH["juiz"]).re_first(REGEX["juiz"])

    print(classe)