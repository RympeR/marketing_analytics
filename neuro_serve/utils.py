import pandas as pd

class TgUtils:
    def __init__(self):
        pass
    
class GuiStatsUtils:
    def __init__(self):
        pass

class DataUtils:
    def __init__(self):
        pass

    def read_data(self, data_file):
        df = pd.read_csv('data.csv',sep='\n', delimiter=',', header=0,encoding='utf-8')
        print(df)
        print(isinstance(df, pd.DataFrame))