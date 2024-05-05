form pyrogram import Client, __version__ , filters
from pyrogram.raw.all import layerfilters
import config
import sc.py
import os
import logging 
LOGGER = logging.getLoggor(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)


api_id = 3335796,
api_hash = "138b992a0e672e8346d8439c3f42ea78",
bot_token = "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0"

fars = Client("test",
api_id = api_id,
api_hash = api_hash,
bot_token = bot_token
)


#GROUP = "test"
#WELCOME_MESSAGE = "Hello welcome"


def welcome(client, message):
message.reply_text(Config.IMDB_TEMPLATE_TXT)
print ("i am testing group")


fars.run()
