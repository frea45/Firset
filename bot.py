from pyrogram import Client , filters
import logging


api_id = 3335796
api_hash = '138b992a0e672e8346d8439c3f42ea78'
token = '5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0'


app = Client("uploader",api_id=api_id, api_hash=api_hash, bot_token=bot_token )


logging.basicConfig(
format = '%(asctime)s – %(name)s – %(levelname)s – %(message)s', 
level = logging.INFO
)
LOGGER = logging.getLoggor(__name__)


#@app.on.message(filters.private)
# def hello (client, message):
  #   message.replay("hello")



async def main():
    async with app:
        await app.send_message("me", "Hi!")

app.run(main())
