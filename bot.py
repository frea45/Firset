from pyrogram import Client, filters
import logging
import config
#import API_ID, API_HASH, BOT_TOKEN 
from pyrogram.handlers import MessageHandler
#from pyrogram.errors import BadRequest, Forbidden, ...

api_id = 3335796
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0"


app = Client("uploader",api_id=api_id, api_hash=api_hash, bot_token=bot_token )


@app.on_message(filters.text & filters.private)
async def echo(client, message):
  #  await message.reply(message.text)
    if message.text :
      if message.text == '/start':
      app.send_message(
        message.chat_id, 'Hiii',
        reply_to_message_id=message.id 
                      )
   elif message.photo :
     pass 
logging.info('startter')


#logging.basicConfig(
#format = '%(asctime)s – %(name)s – %(levelname)s – %(message)s', 
#level = logging.INFO
#)
#LOGGER = logging.getLoggor(__name__)


app.run()
