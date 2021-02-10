import abc
from typing import Optional


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
