import scrapy
from scrapy.shell import inspect_response
from crawler.items import *
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

        header_item = HeaderItem()
        header_item['classe'] = classe
        header_item['area'] = area
        header_item['assunto'] = assunto
        header_item['data_distribuicao'] = data_distribuicao
        header_item['juiz'] = juiz

        
        partes_items = list(self.extract_partes(response))
        movimentacoes_items = list(self.extrat_movimentacoes(response))

        processo_item = ProcessoItem()
        processo_item['header'] = header_item
        processo_item['partes'] = partes_items
        processo_item['movimentacoes'] = movimentacoes_items

        yield processo_item

    def extract_partes(self, response):
        partes = response.xpath(PARTES_XPATH["table"])
        for parte in partes:
            papel = parte.xpath(PARTES_XPATH["papel"]).get().strip()
            nome = parte.xpath(PARTES_XPATH["nome"]).get().strip()

            item = PartesItem()
            item['nome'] = nome
            item['papel'] = papel

            yield item

            
    def extrat_movimentacoes(self, response):
        movimentacoes = response.xpath(MOVIMENTACOES_XPATH["table"])
        for movimentacao in movimentacoes:
            data = movimentacao.xpath(MOVIMENTACOES_XPATH["data"]).get().strip()
            texto = movimentacao.xpath(MOVIMENTACOES_XPATH["texto"]).get().strip()

            if texto:
                item = MovimentacoesItem()
                item['data'] = data
                item['texto'] = texto

                yield item
        
    def get_numero_ano_unificado(self, process_number):
        return f"{process_number[:15]}"

    def get_foro_numero_unificado(self, process_number):
        return f"{process_number[21:]}"