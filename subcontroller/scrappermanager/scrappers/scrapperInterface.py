import abc
from typing import Optional
import requests
import random
import ujson
from typing import Optional
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from multiprocessing import Pool
from selenium import webdriver
from icecream import ic


class ScrapperApi(abc):
    @abc.abstractmethod
    def setFilters(self, filters: dict):
        """[summary]
        Abstract method for setting scrapper filters
        Args:
            filters (dict): [description]
        """
        pass

    @abc.abstractmethod
    def getVacancyPack(self, pack_amount: int = 150, vacancy_name: Optional[str] = None):
        """[summary]
        Abstract method for getting vacansys
        Args:
            pack_amount (int, optional): [description]. Defaults to 150.
            vacancy_name (Optional[str], optional): [description]. Defaults to None.
        """
        pass

    @abc.abstractmethod
    def authorize(self, creds: dict):
        """[summary]

        Abstract method for authorize at work website
        Args:
            creds (dict): [description]
        """
        pass

    @abc.abstractmethod
    def setToDefault(self):
        """[summary]
            Abstract method for setting filters to default
        """
        pass
