from pyrogram import client , filters
from pyrogram.types import Message 
import asyncio


API_ID = "3335796"
API_HASH = "138b992a0e672e8346d8439c3f42ea78"


app = client("bot",
API_ID,
API_HASH,
BOT_TOKEN= "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0")


@app.on_message(filters.command(["reset"]) & filters.private)
async def reset(bot, update):
        await db.delete_user(update.from_user.id)
        await db.add_user(update.from_user.id)
        await update.reply_text("Settings reseted successfully"
    
 
  
  app.run()
