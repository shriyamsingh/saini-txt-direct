#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25900917"))
API_HASH = environ.get("API_HASH", "5a132cf6df4b93cf4f970522a5bda9f7")
BOT_TOKEN = environ.get("BOT_TOKEN", "8109910902:AAF-YNlwwZGq8AeCVEz1J1dhgPbBxyIuoI0")
OWNER = int(environ.get("OWNER", "6084659318"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '6084659318').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
