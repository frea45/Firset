form pyrogram import Client, filters 
import logging 
LOGGER = logging.getLoggor(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)


api_id = 3335796,
api_hash = "138b992a0e672e8346d8439c3f42ea78",
bot_token = "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0"

fars = Client("test", api_id = api_id, api_hash = api_hash, bot_token = bot_token )



@fars.on_message(filters.command("start"))
  def welcome(client, message):

print ("")


fars.run()
