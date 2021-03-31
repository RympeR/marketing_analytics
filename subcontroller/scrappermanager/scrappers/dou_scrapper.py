from .scrapperInterface import *
from datetime import datetime
from dateutil import parser
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
                self.creds = random.choice(ujson.loads(
                    f.readlines())['creds']['dou.ua'])
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
        self.driver.get('https://jobs.dou.ua/vacancies/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(
            '/div[2]/div[1]/div[2]/div[2]/form/span/input').send_keys(vacancy_name)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath(
            '#container > div.header > div.b-sub-head-n > div.b-jobs-search > form > input'
        ).click()
        hrefs = self.driver.find_element_by_class_name('vt')
        vacany_amount = len(hrefs)
        while vacany_amount < pack_amount:
            self.driver.find_element_by_css_selector(
                '#vacancyListId > div > a').click()
            hrefs = self.driver.find_element_by_class_name('vt')
            vacany_amount = len(hrefs)
        hrefs = [href.get_attribute('href') for href in hrefs]
        data = []
        data_params = {
            'vacancy_name': '',
            'salary': '',
            'city': '',
            'country': '',
            'work_category': '',
            'website_name': 'dou.ua',
            'posted_date': '',
            'effectivness': 0.0,
            'experience': 0.0,
        }
        for ind, href in enumerate(hrefs):
            data.append(data_params)
            self.driver.get(href)
            try:
                elem = self.driver.find_element_by_xpath()

            except Exception:
                pass
            try:
                elem = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[1]/div/div[3]')
                dt = parser.parse(elem.text)
                
            except Exception:
                pass
            try:
                elem = self.driver.find_element_by_xpath()
                        
            except Exception:
                pass
            try:
                elem = self.driver.find_element_by_xpath()
                        
            except Exception:
                pass
            try:
                elem = self.driver.find_element_by_xpath()
                        
            except Exception:
                pass
            try:
                elem = self.driver.find_element_by_xpath()
                        
            except Exception:
                pass

        return data
