import requests
from icecream import ic
from datetime import datetime
import time
from .dirmanager.init_file import *


def time_format():
    return f'{datetime.now()}|> '


ic.configureOutput(prefix=time_format)

# NEURO_URL = 'https://www.google.com/'


class DataSender:
    def __init__(self, ip, port, filtrSubURL, readySubURL):
        self.ip = ip
        self.port = port
        self.filtrSubURL = filtrSubURL
        self.readySubURL = readySubURL

    def waitWhileBusy(self):
        response_code = 0
        while response_code != 200:
            url = 'http://{}:{}{}'.format(self.ip, self.port, self.readySubURL)
            response_code = requests.get(url).status_code
            ic(f'\nAnswer from API {response_code}\n')
            if response_code != 200:
                time.sleep(1)

    def sendArchive(self, path):
        self.waitWhileBusy()
        url = 'http://{}:{}{}'.format(self.ip, self.port,  self.filtrSubURL)
        files = {'archive': open(path, 'rb')}
        ic('######FILES TO SEND####')
        ic(files)
        ic(f'\n{path}')
        ic('###########')
        response = requests.post(url, files=files)
        ic(response.status_code)
        return response.status_code
