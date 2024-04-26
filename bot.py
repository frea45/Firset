from pyrogram import Client, filters
import logging
import config
import os
import traceback
#import API_ID, API_HASH, BOT_TOKEN 
from pyrogram.handlers import MessageHandler
#from pyrogram.errors import BadRequest, Forbidden, ...

api_id = 3335796
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0"


app = Client("uploader",api_id=api_id, api_hash=api_hash, bot_token=bot_token )


#@app.on_message(filters.text & filters.private)
#async def echo(client, message):
  #  await message.reply(message.text)
    

f = filters.command("start")

@app.on_message(f)
@app.on_edited_message(f)
async def new_and_edited(c, m):
    print("new and edited")


#logging.basicConfig(
#format = '%(asctime)s – %(name)s – %(levelname)s – %(message)s', 
#level = logging.INFO
#)
#LOGGER = logging.getLoggor(__name__)


app.run()
