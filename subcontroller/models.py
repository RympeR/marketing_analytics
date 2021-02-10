from pydantic import BaseModel
from typing import Optional


class Scrapper(BaseModel):
    scrapper_id: int
    name: str
    website_name: str
    website_url: str
    params: dict
    running: bool
    pause: bool
