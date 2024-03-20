import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
PRIVATE_CHANNEL_ID = os.getenv("PRIVATE_CHANNEL_ID")
