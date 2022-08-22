import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH" "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", None)
