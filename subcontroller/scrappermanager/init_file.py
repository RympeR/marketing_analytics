from .scrapper_controller import *
from .data_sender import *

SCRAPPER_CONTROLLER = ScrapperController()
DATA_SENDER = DataSender(
    '127.0.0.1',
    '7999',
    '/',
    '/uploadfile/'
)
