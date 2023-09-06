# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
        processo = {
            spider.name: {
                "header": {
                    "classe": item.get("header", {}).get("classe"),
                    "area": item.get("header", {}).get("area"),
                    "assunto": item.get("header", {}).get("assunto"),
                    "data_distribuicao": item.get("header", {}).get("data_distribuicao"),
                    "juiz": item.get("header", {}).get("juiz"),
                },
                "partes": [dict(parte) for parte in item.get("partes", [])],
                "movimentacoes": [dict(movimentacao) for movimentacao in item.get("movimentacoes", [])],
            }
        }

        processo_json = json.dumps(processo, ensure_ascii=False)

        with open('processo.json', 'w', encoding='utf-8') as json_file:
            json_file.write(processo_json)

        return item
