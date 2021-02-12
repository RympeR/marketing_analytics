from fastapi import FastAPI
from typing import Optional
import os
os.sys.path.append('..')

# from dirmanager.init_file import *
# from scrappermanager.init_file import *

# from psycopg_models import *
# from models import *


app = FastAPI()


# -----------------------GET REQUESTS-----------------------

@app.get("/")
def read_root():
    return {"Hello": "You at single parser api"}


@app.get("status/{parser_id}")
def get_status(parser_id: int):
    return {
        "parser_id": parser_id
    }


@app.get("params/{parser_id}")
def get_status(parser_id: int):
    return {
        "parser_id": parser_id
    }


# -----------------------POST REQUESTS-----------------------

@app.post("create_scrapper/")
def create_scrapper():
    return {
        'status': 'success'
    }


@app.post("set_filters/{parser_id}")
def set_filters(parser_id: int, params: Optional[dict]):
    return {
        'status': 'success',
        'params': params
    }

# -----------------------PUT REQUESTS-----------------------


@app.put('update_filters/{parser_id}')
def update_filters(parser_id: int, params: Optional[dict]):
    return {
        'status': 'success',
        'params': params
    }


@app.put('run/{parser_id}')
def run(parser_id: int):
    return {
        'status': 'success'
    }


@app.put('stop/{parser_id}')
def stop(parser_id: int):
    return {
        'status': 'success'
    }


@app.put('pause/{parser_id}')
def pause(parser_id: int):
    return {
        'status': 'success'
    }


@app.put('unpause/{parser_id}')
def unpause(parser_id: int):
    return {
        'status': 'success'
    }
