import re, os
import script from script

id_pattern = re.compile(r'^.\d+$') 

api_id = os.environ.get("api_id", "3335796")

api_hash = os.environ.get("api_hash", "138b992a0e672e8346d8439c3f42ea78")

bot_token = os.environ.get("bot_token", "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0") 

#PORT = os.environ.get('PORT', '8080')
BUN_VERSION = os.environ.get("BUN_VERSION", "1.1.0")

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
