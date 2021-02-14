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

class Datamaster(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sendVacancys(self, vacancys):
        pass

    @abc.abstractmethod
    def getVacancysPack(self, VacancysInPack=100, vacancy_name: Optional[str] = None):
        pass

    @abc.abstractmethod
    def saveVacansys(self, vacansys):
        pass

    @abc.abstractmethod
    def setFilters(self, filters, to_default=False):
        pass


class RabotaApiDataMaster(Datamaster):
    def __init__(self, filters: Optional[dict] = None):
        if filters:
            self.rabotaApiMaster = RabotaScrapper(filters)
        else:
            self.rabotaApiMaster = RabotaScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100, vacancy_name: Optional[str] = None):
        if vacancy_name:
            self.data = self.rabotaApiMaster.getVacancysPack(
                VacancysInPack, vacancy_name)
        else:
            filter_vacancy_name = self.rabotaApiMaster.filters.get(
                'vacancyName', None)
            if filter_vacancy_name:
                self.data = self.rabotaApiMaster.getVacancysPack(
                    VacancysInPack, filter_vacancy_name)
        self.saveVacansys(self.data)

    def saveVacansys(self, vacansys):
        pass

    def setFilters(self, filters, to_default=False, vacancy_name: Optional[str] = None):
        if to_default:
            self.rabotaApiMaster.setFilters(filters)
        else:
            self.rabotaApiMaster.setToDefault()


class WorkUaApiDataMaster(Datamaster):
    def __init__(self, filters: Optional[dict] = None):
        if filters:
            self.workUaApiMaster = WorkUaScrapper(filters)
        else:
            self.workUaApiMaster = WorkUaScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100, vacancy_name: Optional[str] = None):
        if vacancy_name:
            self.data = self.workUaApiMaster.getVacancysPack(
                VacancysInPack, vacancy_name)
        else:
            filter_vacancy_name = self.workUaApiMaster.filters.get(
                'vacancyName', None)
            if filter_vacancy_name:
                self.data = self.workUaApiMaster.getVacancysPack(
                    VacancysInPack, filter_vacancy_name)
        self.saveVacansys(self.data)

    def saveVacansys(self, vacansys):
        pass

    def setFilters(self, filters, to_default=False):
        if to_default:
            self.workUaApiMaster.setFilters(filters)
        else:
            self.workUaApiMaster.setToDefault()


class HHApiDataMaster(Datamaster):
    def __init__(self, filters: Optional[dict] = None):
        if filters:
            self.hhApiMaster = HHScrapper(filters)
        else:
            self.hhApiMaster = HHScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100, vacancy_name: Optional[str] = None):
        if vacancy_name:
            self.data = self.hhApiMaster.getVacancysPack(
                VacancysInPack, vacancy_name)
        else:
            filter_vacancy_name = self.hhApiMaster.filters.get(
                'vacancyName', None)
            if filter_vacancy_name:
                self.data = self.hhApiMaster.getVacancysPack(
                    VacancysInPack, filter_vacancy_name)

        self.saveVacansys(self.data)

    def saveVacansys(self, vacansys):
        pass

    def setFilters(self, filters, to_default=False):
        if to_default:
            self.hhApiMaster.setFilters(filters)
        else:
            self.hhApiMaster.setToDefault()


class DouApiDataMaster(Datamaster):
    def __init__(self, filters: Optional[dict] = None):
        if filters:
            self.douApiMaster = DouScrapper(filters)
        else:
            self.douApiMaster = DouScrapper()

    def sendVacancys(self, vacancys):
        pass

    def getVacancysPack(self, VacancysInPack=100, vacancy_name: Optional[str] = None):
        if vacancy_name:
            self.data = self.douApiMaster.getVacancysPack(
                VacancysInPack, vacancy_name)
        else:
            filter_vacancy_name = self.douApiMaster.filters.get(
                'vacancyName', None)
            if filter_vacancy_name:
                self.data = self.douApiMaster.getVacancysPack(
                    VacancysInPack, filter_vacancy_name)
        self.saveVacansys(self.data)

    def saveVacansys(self, vacansys):
        pass

    def setFilters(self, filters, to_default=False):
        if to_default:
            self.douApiMaster.setFilters(filters)
        else:
            self.douApiMaster.setToDefault()
