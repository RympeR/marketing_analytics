from .scrapperInterface import *
from datetime import datetime
from dateutil import parser


options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
PATH = "D:\develop\pypr\marketing_analytics\subcontroller\scrappermanager\scrappers\chromedriver.exe"
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')


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
        self.filters['vacancyName'] = 'Developer'
        self.filters['work_category'] = 'it'

    def authorize(self, creds: dict):
        self.driver.get('https://dou.ua')
        self.cookies = self.driver.get_cookies()

    def getVacancysPack(self, pack_amount: int = 150, vacancy_name: Optional[str] = None):
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
            'vacancy_name': [],
            'salary': [],
            'city': [],
            'country': [],
            'work_category': [],
            'website_name': [],
            'posted_date': [],
            'effectivness': [],
            'experience': [],
        }
        for href in hrefs:
            self.driver.get(href)
            time.sleep(2)
            data_params['effectivness'].append(0.0)
            data_params['website_name'].append('dou.ua')
            data_params['experience'].append(1.0)
            data_params['work_category'].append('IT')
            data_params['country'].append('Ukraine')

            try:
                name_vacansion = self.driver.find_element_by_class_name('g-h2')
                data_params['vacancy_name'].append(name_vacansion.text)
            except NoSuchElementException:
                data_params['vacancy_name'].append('')

            try:
                salary = self.driver.find_element_by_class_name('salary')
                data_params['salary'].append(salary.text)
            except NoSuchElementException:
                data_params['salary'].append('')

            try:
                city = self.driver.find_element_by_class_name('place')
                data_params['city'].append(city.text)
            except NoSuchElementException:
                data_params['city'].append('')

            try:
                posted_date = self.driver.find_element_by_class_name('date')
                posted_date = posted_date.text.split(' ')
                for month in data['months'].keys():
                    if fuzz.ratio(month, posted_date[1]) >= 40:
                        posted_date[1] = data['months'][month]
                        if len(posted_date[0]) < 2:
                            posted_date[0] = '0' + posted_date[0]
                        year, month, day = list(
                            map(int, '-'.join(reversed(posted_date)).split('-')))
                        dt = datetime(year, month, day)
                        timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
                        data_params['posted_date'].append(timestamp)
                        break
                else:
                    data_params['posted_date'].append(
                        datetime.today().strftime('%Y-%m-%d'))

            except NoSuchElementException as e:
                print(e)
                data_params['posted_date'].append(
                    datetime.today().timestamp())

        return data_params
