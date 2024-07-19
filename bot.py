form pyrogram import Client, filters 
import logging 
LOGGER = logging.getLoggor(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)


api_id = 3335796,
api_hash = "138b992a0e672e8346d8439c3f42ea78",
bot_token = "7439915063:AAGWKexBKxqCiQXIWSpLmHZTqpG8gQ-1RJA"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@app.on_message()
async def my_handler(client, message):
    await message.forward("me")
    print ("working")


app.run()
