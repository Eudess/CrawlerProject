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
    pass
