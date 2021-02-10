import requests
import ujson
import random
from scrapperinterface import ScrapperApi


class RabotaScrapper(ScrapperApi):
    def __init__(self, filters: Optional[dict] = None):
        if filters:
            self.filters = filters
        else:
            self.filters = {
                'vacancyInPack': 150,
                'vacancyName': 'it'
            }
        with open('creads.json', 'r', encoding='utf-8') as f:
            self.creds = random.choice(ujson.loads(f.readlines())['creds'])
        self.authorize(self.creds)

    def setFilters(self, filters: dict):
        self.filters = filters

    def setToDefault(self):
        self.filters['vacancyInPack'] = 150
        self.filters['vacancyName'] = 'it'

    def authorize(self, creds: dict):
        pass

    def getVacancyPack(self, pack_amount: int = 150, vacancy_name: Optional[str] = None):
        pass
