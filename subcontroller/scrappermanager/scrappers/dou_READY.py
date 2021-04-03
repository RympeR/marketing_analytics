from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import info_search
import re
import json
from fuzzywuzzy import fuzz
from pprint import pprint
from datetime import datetime
from datetime import timezone
import csv

with open('city.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
# options
options = webdriver.ChromeOptions()

# change useragent

options.add_argument(
    'user-agent=Mozilla/5.0 (x11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0')

options.add_argument('--disable-blink-features=AutomationControlled')

# user-agent
PATH = "D:\develop\pypr\marketing_analytics\subcontroller\scrappermanager\scrappers\chromedriver.exe"

driver = webdriver.Chrome(
    executable_path=PATH, options=options)

try:
    with open('dou.csv', 'w', newline='', encoding="UTF-8") as f:
        fieldnames = ['vacancy_name', 'salary', 'city', 'country', 'work_category',
                      'website_name', 'posted_date', 'effectivness', 'experience']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()

    driver.get('https://jobs.dou.ua')
    time.sleep(2)

    search = driver.find_element_by_class_name('job')
    search.clear()
    search.send_keys(info_search[0])
    time.sleep(2)

    search.send_keys(Keys.ENTER)
    time.sleep(2)

    items = driver.find_elements_by_class_name("vt")
    hrefs = [href.get_attribute('href') for href in items]
    print(hrefs)
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
        driver.get(href)
        time.sleep(2)
        data_params['effectivness'].append(0.0)
        data_params['website_name'].append('dou.ua')
        data_params['experience'].append(1.0)
        data_params['work_category'].append('IT')
        data_params['country'].append('Ukraine')

        try:
            name_vacansion = driver.find_element_by_class_name('g-h2')
            # print(f'Vacansion name:\n\t {name_vacansion.text}')
            data_params['vacancy_name'].append(name_vacansion.text)
        except Exception:
            data_params['vacancy_name'].append('')

        try:
            salary = driver.find_element_by_class_name('salary')
            # print(f'Salary:\n\t {salary.text}')
            data_params['salary'].append(salary.text)
        except Exception:
            data_params['salary'].append('')

        try:
            city = driver.find_element_by_class_name('place')
            # print(f'City:\n\t {city.text}')
            data_params['city'].append(city.text)
        except Exception:
            data_params['city'].append('')

        try:
            posted_date = driver.find_element_by_class_name('date')
            posted_date = posted_date.text.split(' ')
            # print(f'Date post:\n\t {posted_date}')

            # data_params['posted_date'].append(posted_date.text)
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
                    # dt = datetime(','.join(reversed(posted_date)))
                    # timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
                    break
            else:
                data_params['posted_date'].append(
                    datetime.today().strftime('%Y-%m-%d'))

        except Exception as e:
            print(e)
            data_params['posted_date'].append(
                datetime.today().timestamp())

    with open('dou.csv', 'a', newline='', encoding="UTF-8") as f:
        fieldnames = ['vacancy_name', 'salary', 'city', 'country', 'work_category',
                      'website_name', 'posted_date', 'effectivness', 'experience']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        for vacancy in zip(*data_params.values()):
            thewriter.writerow({'vacancy_name': vacancy[0], 'salary': vacancy[1], 'city': vacancy[2], 'country': vacancy[3], 'work_category': vacancy[4],
                                'website_name': vacancy[5], 'posted_date': vacancy[6], 'effectivness': vacancy[7], 'experience': vacancy[8]})
        print('-------------------------------------------')
        pprint(data_params)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
