import os
from dotenv import load_dotenv

load_dotenv()

STATE_FILE = "state.json"

CHECK_INTERVAL = 600

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")