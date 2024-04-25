import re, os

id_pattern = re.compile(r'^.\d+$') 

api_id = os.environ.get("API_ID", "3335796")

api_hash = os.environ.get("API_HASH", "138b992a0e672e8346d8439c3f42ea78")

bot_token = os.environ.get("BOT_TOKEN", "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0") 

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
