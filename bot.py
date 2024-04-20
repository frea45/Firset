from pyrogram import client , filters
from pyrogram.types import Message 

API_ID = "3335796"
API_HASH = "138b992a0e672e8346d8439c3f42ea78"


app = client("bot",
API_ID,
API_HASH,
BOT_TOKEN= "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0")

@app.on.message(filters.text)
def test (c:client = m:message):
  chatid = m.chat.id
  app.send.message(chatid , "یا خدا")
  
  app.run()
