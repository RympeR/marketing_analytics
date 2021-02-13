from fastapi import FastAPI
from typing import Optional
import os
os.sys.path.append('..')

# from dirmanager.init_file import *
from .scrappermanager.init_file import *

# from psycopg_models import *
# from models import *


app = FastAPI()


# -----------------------GET REQUESTS-----------------------

@app.get("/")
def read_root():
    return {"Hello": "You at single parser api"}


@app.get("status/")
def get_status():
    status = SCRAPPER_CONTROLLER.getStatus()
    try:
        data = {
            'status': 'success',
            'vacancyCollectorStatus':{
                'is active':status['is active'],
                'is paused':status['is paused'],
                'vacancy':status,
                'collected vacancys':status['collected vacansys'],
                'filter' : {} if status is {} else {
                    'website':status['site to parse'],
                    'stage_from':status['filter']['stage_from'],
                    'stage_to':status['filter']['stage_to'],
                    'number of threads':status['filter']['number of threads'],
                    'city_name':status['filter']['city_name'],
                    'vacancys in pack':status['filter']['vacancys in pack'],
                }
            }
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed get status ->
                        reason \n{e}''')
    return data

# -----------------------POST REQUESTS-----------------------

@app.post("create_scrapper/")
def create_scrapper():
    
    return {
        'status': 'success'
    }


@app.post("set_filters/")
def set_filters(params: Optional[dict]):
    try:
        SCRAPPER_CONTROLLER.setFilter(params)
        data = {
            'status': 'success'
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed set filters ->
                        reason \n{e}''')
    return data

@app.post("set_setting/")
def set_setting(params: Optional[dict]):
    try:
        SCRAPPER_CONTROLLER.setFilter(params)
        data = {
            'status': 'success'
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed set settings ->
                        reason \n{e}''')
    return data
# -----------------------PUT REQUESTS-----------------------


@app.put('update_filters/')
def update_filters(params: Optional[dict]):
    try:
        SCRAPPER_CONTROLLER.setFilter(params)
        data = {
            'status': 'success'
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed set filters ->
                        reason \n{e}''')
    return data


@app.put('run/')
def run():
    try:
        SCRAPPER_CONTROLLER.run()
        data = {
            'status': 'success'
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed run scrapper ->
                        reason \n{e}''')
    return data


@app.put('stop/')
def stop():
    try:
        SCRAPPER_CONTROLLER.quitAllThreads()
        data = {
            'status': 'success'
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed run scrapper ->
                        reason \n{e}''')
    return data


@app.put('pause/')
def pause():
    try:
        SCRAPPER_CONTROLLER.pause()
        data = {
            'status': 'success'
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed run scrapper ->
                        reason \n{e}''')
    return data


@app.put('unpause/')
def unpause():
    try:
        SCRAPPER_CONTROLLER.unpause()
        data = {
            'status': 'success'
        }
    except Exception as e:
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed run scrapper ->
                        reason \n{e}''')
    return data
