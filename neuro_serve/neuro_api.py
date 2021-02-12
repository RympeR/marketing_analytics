from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# -----------------------GET REQUESTS-----------------------

@app.get("/")
def read_root():
    return {"Hello": "You at neuro serve api"}

