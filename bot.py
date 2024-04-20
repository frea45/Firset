from pyrogram import client , filters
from pyrogram.types import Message , ReplyKeyboardMarkup
import asyncio


API_ID = 3335796
API_HASH = "138b992a0e672e8346d8439c3f42ea78"


app = client("bot",
API_ID,
API_HASH,
BOT_TOKEN= "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0")

@app.on.message(filters.private , group=0) 
  async def test (client = message):
  text = message.text
  chat = message.chat.id
  if text == "/start":
    await app.send_message (
      chat , "welcome",
      reply_markup=ReplyKeyboardMarkup(
        [
          ["sallam"]
        ],
        
         resize_keyboard = True 
        
        ) 
      )
    
    
 
  
  app.run()
