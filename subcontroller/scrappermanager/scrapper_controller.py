import selenium
from selenium.webdriver import chrome
import threading
import time
import json
from datetime import datetime
from icecream import ic
from .datamanager import Datamaster, RabotaApiDataMaster, WorkUaApiDataMaster, DouApiDataMaster, HHApiDataMaster
from multiprocessing import Pool


def time_format():
    return f'{datetime.now()}|> '


ic.configureOutput(prefix=time_format)


class ScrapperController:
    """[summary]
    """

    def __init__(self, site_to_parce='work.ua', filterParams=None):
        self.ThreadsList = []
        self.runThreads = False
        self.isPaused = False
        self.filterParams = filterParams
        self.siteToParse = site_to_parce
        # statistic
        self.startTime = None
        self.collectedVacansys = 0
        self.datamasterWorkUa = WorkUaApiDataMaster()
        self.datamasterDou = DouApiDataMaster()
        self.datamasterHH = HHApiDataMaster()
        self.datamasterRabotaUa = RabotaApiDataMaster()

    def toDefaultState(self):
        self.runThreads = False
        self.isPaused = False
        self.startTime = None
        self.collectedVacansys = 0

    def change_website(self):
        pass

    def quitAllThreads(self):
        ic("IdsCollector qiting all threads")
        self.runThreads = False

    def unpause(self):
        self.isPaused = False

    def pause(self):
        self.isPaused = True

    def getStatus(self):
        return {
            "number of threads": len(self.ThreadsList),
            "is active": self.runThreads,
            "is paused": self.isPaused,
            "filter": {} if self.filterParams is None else self.filterParams,
            "start time": self.startTime,
            "collected vacansys": self.collectedVacansys,
            "site to parse": self.siteToParse,
        }

    def setFilter(self, filterParams: dict):
        self.filterParams = filterParams

    def run(self):
        self.startTime = datetime.now()
        self.collectedIds = 0
        self.runThreads = True
        ic('#########################################')
        ic('\n\n\nVacansys collector is fcking running\n\n\n')
        ic('#########################################')
        if self.filterParams is None:
            ic('\n!!!No filter to parse!!!\n')
        else:
            ic("nVacansysCollector.filterParams", self.filterParams)
            keys = self.filterParams.keys()

    def addThread(self, thread):
        self.ThreadsList.append(thread)

    def startThreads(self):
        for i in range(self.settings['number of threads']):
            thr = threading.Thread(
                target=self.vacancyLoop,
                args=(
                    "THR{}".format(i),
                ),
                name="PhotoThread{}".format(i)
            )
            self.addThread(thr)
            thr.start()
            ic("started thread '{}'".format(thr.getName()))
            time.sleep(3)

    def setSettings(self, settings):
        ic("settings: ", settings)
        for key in settings.keys():
            try:
                self.settings[key] = int(settings[key])
            except ValueError as e:
                ic(e)

    def vacancyLoop(self, ThreadNum):
        ic("started vacancyLoop with arguments:\n\tvacancy_in_pack = {}\n\tThreadNum = {}\n\tmemLimit = {}\n\tpackLimit = {}".format(
            self.settings['vacancy in pack'],
            self.settings['vacancy name'],
            ThreadNum,
            self.settings['memory limit'],
            self.settings.get('pack amount', None),
        ))
        pack_amount = self.settings.get('pack amount', None)
        ic(f'\n pack amount \n\t{pack_amount}\n')
        if pack_amount:

            count = 0
            while self.runThreads and count < pack_amount:
                count += 1
                ic(f'\n Iteration photo loop#{count}\n')
                try:
                    self.handleIdsPack(
                        ThreadNum, IdsInPack=self.settings['ids in pack'])
                except Exception as e:
                    self.ambassador.nextConnection()
                    self.handleIdsPack(
                        ThreadNum, IdsInPack=self.settings['ids in pack'])

                time.sleep(0.1)
        else:
            while self.runThreads:
                try:
                    self.handleIdsPack(
                        ThreadNum, IdsInPack=self.settings['ids in pack'])
                except Exception:
                    self.ambassador.nextConnection()
                    self.handleIdsPack(
                        ThreadNum, IdsInPack=self.settings['ids in pack'])

                time.sleep(0.1)
        ic("Quiting thread '{}'".format(ThreadNum))

    def handleVacancyPack(self, vacancyInPack=150, filters=None):
        pass
