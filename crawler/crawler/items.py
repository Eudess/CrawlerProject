# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeaderItem(scrapy.Item):
    classe = scrapy.Field()
    area = scrapy.Field()
    assunto = scrapy.Field()
    data_distribuicao = scrapy.Field()
    juiz = scrapy.Field()

class PartesItem(scrapy.Item):
    nome = scrapy.Field()
    papel = scrapy.Field()

class MovimentacoesItem(scrapy.Item):
    data = scrapy.Field()
    texto = scrapy.Field()

class ProcessoItem(scrapy.Item):
    header = scrapy.Field()
    partes = scrapy.Field()
    movimentacoes = scrapy.Field()