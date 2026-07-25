import os

from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 저장 파일
STATE_FILE = "state.json"

# 게시판 확인 주기(초)
CHECK_INTERVAL = 600

# Discord Webhook
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# HTTP 요청
REQUEST_TIMEOUT = 10

# User-Agent
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/138.0 Safari/537.36"
)