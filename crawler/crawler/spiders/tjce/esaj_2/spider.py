from .constants.constants import START_URL
from ...base_esaj_2.spider import SpiderBaseEsaj2

class Esaj2Tjce(SpiderBaseEsaj2):
    name = "esaj_tjce-2-grau"
    start_urls = [START_URL]

