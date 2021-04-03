#!/usr/bin/env python3
import sys
import os

sys.path.append('..')

from typing import Optional, List
import json

from flask import Flask, request, jsonify
app = Flask(__name__)

from scrappermanager.init_file import *

# from models import *



# def location_dict(locations: List[str] = Query(...)):
#     return list(map(json.loads, locations))

# -----------------------GET REQUESTS-----------------------

@app.route("/", methods=['GET'])
def read_root():
    return {"Hello": "You at single parser api"}


@app.route("/status/", methods=['GET'])
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
                    'number of threads':status['filter']['number of threads'],
                    'vacancys in pack':status['filter']['vacancys in pack'],
                }
            }
        }
    except Exception as e:
        print(e)
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'a') as f:
            f.write(f'''\nFailed get status ->
                        reason \n{e}''')
    return data

# -----------------------POST REQUESTS-----------------------

@app.route("/create_scrapper/", methods=['POST'])
def create_scrapper():
    
    return {
        'status': 'success'
    }


@app.route("/set_filters/", methods=['POST'])
def set_filters():
    # try:
    SCRAPPER_CONTROLLER.setFilters(request.json)
    data = {
        'status': 'success'
    }
    # except Exception as e:
    #     print(e)
    #     data = {
    #         'status': 'failure',
    #     }
    #     with open('logs.txt', 'a') as f:
    #         f.write(f'''\nFailed set filters ->
    #                     reason \n{e}''')
    return data

@app.route("/set_setting/", methods=['POST'])
def set_setting():
    try:
        SCRAPPER_CONTROLLER.setSettings(request.json)
        data = {
            'status': 'success'
        }
    except Exception as e:
        print(e)
        data = {
            'status': 'failure',
        }
        with open('logs.txt', 'w') as f:
            f.write(f'''\nFailed set settings ->
                        reason \n{e}''')
    return data
# -----------------------PUT REQUESTS-----------------------


@app.route('/update_filters/', methods=['PUT'])
def update_filters():
    try:
        SCRAPPER_CONTROLLER.setFilters(request.json)
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


@app.route('/run/', methods=['PUT'])
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


@app.route('/stop/', methods=['PUT'])
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


@app.route('/pause/', methods=['PUT'])
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


@app.route('/unpause/', methods=['PUT'])
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


if __name__ == '__main__':
    app.run(host= '127.0.0.1',port='8000', debug=True)