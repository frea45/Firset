from pyrogram import Client , filters



api_id = 3335796
api_hash = '138b992a0e672e8346d8439c3f42ea78'
token = '5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0'

app = Client(
  "uploader",
api_id = api_id,
api_hash = api_hash,
bot_token = token
)

import logging
logging.basicConfig(
format = '%(asctime)s – %(name)s – %(levelname)s – %(message)s', 
level = logging.INFO
)
LOGGER = logging.getLoggor(__name__)


@app.on.message(filters.private)
 def hello (client, message):
     message.replay("hello")
     
     
  app.run()
