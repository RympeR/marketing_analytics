import abc
import requests
import json
from scrappers.dou_scrapper import DouScrapper
from scrappers.hh_scrapper import HHScrapper
from scrappers.rabota_scrapper import RabotaScrapper
from scrappers.work_ua_scrapper import WorkUaScrapper


class Datamaster(abc):
    @abc.abstractmethod
    def sendVacancys(self, vacancys):
        pass

    @abc.abstractmethod
    def getVacancysPack(self, VacancysInPack=100):
        pass

    @abc.abstractmethod
    def saveVacansys(self, vacansys):
        pass


class RabotaApiDataMaster(Datamaster):
    def __init__(self):
        self.rabotaApiMaster = RabotaScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100):
        pass

    def saveVacansys(self, vacansys):
        pass


class WorkUaApiDataMaster(Datamaster):
    def __init__(self):
        self.workUaApiMaster = WorkUaScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100):
        pass

    def saveVacansys(self, vacansys):
        pass


class HHApiDataMaster(Datamaster):
    def __init__(self):
        self.hhApiMaster = HHScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100):
        pass

    def saveVacansys(self, vacansys):
        pass


class DouApiDataMaster(Datamaster):
    def __init__(self):
        self.douApiMaster = DouScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100):
        pass

    def saveVacansys(self, vacansys):
        pass
