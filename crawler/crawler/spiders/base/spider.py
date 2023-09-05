import scrapy
from scrapy.shell import inspect_response
from crawler.items import HeaderItem
from .constants.constants import *
from .constants.extract import *

class SpiderBase(scrapy.Spider):
    name = "spider_base_esaj"
    

    def __init__(self, *args, **kwargs):
        super(SpiderBase, self).__init__(*args, **kwargs)
        self.process_number = kwargs.get('numero_processo')

    
    def parse(self, response):
        formdata = FORMDATA.copy()
        formdata.update(
            {
                "numeroDigitoAnoUnificado": self.get_numero_ano_unificado(self.process_number),
                "foroNumeroUnificado": self.get_foro_numero_unificado(self.process_number),
                "dadosConsulta.valorConsultaNuUnificado": self.process_number,
            }
        ) 

        yield scrapy.FormRequest.from_response(response, 
                                                   formdata=formdata,
                                                   headers=USER_AGENT,
                                                   callback=self.extract_header,
            )


    def extract_header(self, response):
        classe = response.xpath(HEADER_XPATH["classe"]).get()
        area = response.xpath(HEADER_XPATH["area"]).get()
        assunto = response.xpath(HEADER_XPATH["assunto"]).get()
        data_distribuicao = response.xpath(HEADER_XPATH["data_distribuicao"]).re_first(REGEX["distri"])
        juiz = response.xpath(HEADER_XPATH["juiz"]).re_first(REGEX["juiz"])

        yield self.extract_partes
        yield self.extrat_andamentos
        yield HeaderItem(classe=classe, area=area, assunto=assunto, data_distribuicao=data_distribuicao, juiz=juiz)

    def extract_partes(self, response):
        pass

    def extrat_andamentos(self, response):
        pass

        
    def get_numero_ano_unificado(self, process_number):
        return f"{process_number[:15]}"

    def get_foro_numero_unificado(self, process_number):
        return f"{process_number[21:]}"