import abc
import requests
import json
from typing import Optional
from .scrappers.dou_scrapper import DouScrapper
from .scrappers.hh_scrapper import HHScrapper
from .scrappers.rabota_scrapper import RabotaScrapper
from .scrappers.work_ua_scrapper import WorkUaScrapper
from .psycopg_models import *
from .data_sender import *
import sqlite3
import pandas as pd
from .dirmanager.init_file import *
k = 0


class Datamaster:
    @staticmethod
    def sendVacancys(vacancys, ApiMaster):
        pass

    @staticmethod
    def getVacancysPack(ApiMaster, VacancysInPack=100, vacancy_name: Optional[str] = None, thread_num='_'):
        if vacancy_name:
            data = ApiMaster.getVacancysPack(
                VacancysInPack, vacancy_name)
        else:
            filter_vacancy_name = ApiMaster.filters.get(
                'vacancyName', None)
            if filter_vacancy_name:
                data = ApiMaster.getVacancysPack(
                    VacancysInPack, filter_vacancy_name)
        path = "Loadead/"+thread_num
        try:
            os.makedirs(path)
        except FileExistsError:
            pass
        Datamaster.saveVacansys(data, path, thread_num)

    @staticmethod
    def saveVacansys(vacansys, path, thread_num='_'):
        global k
        df = pd.DataFrame.from_dict(vacansys)
        df.to_csv(f'{path}/{k}_data.csv', encoding='utf-8')
        k += 1

    @staticmethod
    def setFilters(filters, ApiMaster, to_default=False):
        if to_default:
            ApiMaster.setFilters(filters)
        else:
            ApiMaster.setToDefault()
