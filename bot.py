form pyrogram import Client, filters
import config
import os

bot = Client(
"test",
api_id = 3335796,
api_hash = "138b992a0e672e8346d8439c3f42ea78",
bot_token = "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0"
)

@bot.on.message(filters.command('start') & filters.private )
def command1(bot, message):
bot.send.message(message.chat.id, "Hello Baby")
print ("i am online")

@bot.on.message(filters.command('help')  )
def command1(bot, message):
message.reply_text("Hello help")
print ("i am helping")

@bot.on_message(filters.text)
 def echobot(client, message): message.reply_text(message.text)
print ("i am testing")

#pyrogram v1.2.9

#GROUP = "test"
#WELCOME_MESSAGE = "Hello welcome"

@bot.on_message(filters.chat(Config.GROUP) & filters.new_members)
def welcome(client, message):
message.reply_text(Config.WELCOME_MESSAGE)
print ("i am testing group")

bot.run()
