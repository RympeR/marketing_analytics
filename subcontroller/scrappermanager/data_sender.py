import requests
from icecream import ic
from datetime import datetime
import time


def time_format():
    return f'{datetime.now()}|> '


ic.configureOutput(prefix=time_format)

# NEURO_URL = 'https://www.google.com/'


class DataSender:
    def __init__(self, NEURO_URL):
        self.neuro_url = NEURO_URL

    def send_data(self, data: dict):
        response = 500
        while response != 200:
            response = requests.get(self.neuro_url)
            if response.status_code != 200:
                ic('Failed to get status:-> ', response.status_code)
                time.sleep(5)

        try:
            response = requests.post(self.neuro_url, params=data)
            ic('sended data:->', data)
        except Exception as e:
            with open('info/logs.txt', 'a') as f:
                f.write(ic('Failed data sender'))
                f.write(ic(e))
                f.write('-' * 10)
