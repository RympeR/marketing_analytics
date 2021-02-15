from fastapi import FastAPI, File, UploadFile, Depends, Query
from typing import Optional, List
import pandas as pd
import json

app = FastAPI()

def location_dict(locations: List[str] = Query(...)):
    return list(map(json.loads, locations))

# -----------------------GET REQUESTS-----------------------

@app.get("/")
async def read_root():
    return {"Hello": "You at neuro serve api"}

@app.post('/save-data')
async def recieveData(data: list = Depends(location_dict)):
    df = pd.DataFrame.from_dict(data[0])
    df.to_csv('data.csv',encoding='utf-8')
    return {
        'status':'proccessed',
        'data': data
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    print(dir(file))
    return {"filename": file.filename}

