import os
import zipfile
import shutil
from icecream import ic
import pandas as pd
k = 0


class ZipArchiver:
    @staticmethod
    def zipdir(path):
        ic('###zipdir method####')
        ic(path)
        ic(os.listdir(path))
        ic('#####################')
        ziph = zipfile.ZipFile(path+'.zip', mode='w')
        for dir_path in os.listdir(path):
            if os.path.isdir(path+'/'+dir_path):
                for file_path in os.listdir(path+'/'+dir_path):
                    if os.path.isfile(path+'/'+dir_path+'/'+file_path):
                        ziph.write(path+'/'+dir_path+'/'+file_path,
                                   dir_path+'/'+file_path)
        ziph.close()
        return ziph.filename

    @staticmethod
    def cleandir(path):
        ic('###cleandir method####')
        ic(path)
        ic(os.listdir(path))
        ic('#####################')
        # logFile = open("Logs/PyClearLog.txt","a")
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                # logFile.write('Failed to delete %s. Reason: %s\n\n' % (file_path, e))
                # logFile.close()
                ic(e)

    @staticmethod
    def saveFiles(data, path):
        global k
        df = pd.DataFrame.from_dict(data)
        df.to_csv(path + '/' + str(k) + '.csv', encoding='utf-8')
        k += 1
