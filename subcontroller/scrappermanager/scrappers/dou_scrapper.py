from .scrapperInterface import *

options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
PATH = "D:\develop\pypr\marketing_analytics\subcontroller\scrappermanager\scrappers\chromedriver.exe"


class DouScrapper(ScrapperApi):
    def __init__(self, filters: Optional[dict] = None, need_authorization=False):
        if filters:
            self.filters = filters
        else:
            self.filters = {
                'vacancyInPack': 150,
                'vacancyName': 'it'
            }

        self.need_authorization = need_authorization

    def initialize_drive(self):
        self.driver = webdriver.Chrome(
            PATH,
            options=options
        )
        if self.need_authorization:
            with open('creads.json', 'r', encoding='utf-8') as f:
                self.creds = random.choice(ujson.loads(f.readlines())['creds'])
            self.authorize(self.creds)

    def setFilters(self, filters: dict):
        self.filters = filters

    def setToDefault(self):
        self.filters['vacancyInPack'] = 150
        self.filters['vacancyName'] = 'it'

    def authorize(self, creds: dict):
        self.driver.get('https://dou.ua')
        self.cookies = self.driver.get_cookies()

    def getVacancyPack(self, pack_amount: int = 150, vacancy_name: Optional[str] = None):
        data = {}
        return data
