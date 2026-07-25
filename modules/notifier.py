from datetime import datetime

import requests

from config import DISCORD_WEBHOOK_URL
from boards.kgeu import BOARD
from modules.logger import Logger


def send_notification(post):
    if not DISCORD_WEBHOOK_URL:
        Logger.error("DISCORD_WEBHOOK_URL이 설정되지 않았습니다.")
        return False

    embed = {
        "title": post["title"],
        "url": post["url"],
        "color": 0x2ECC71,
        "timestamp": datetime.utcnow().isoformat(),
        "fields": [
            {
                "name": "게시판",
                "value": BOARD["display_name"],
                "inline": True,
            },
            {
                "name": "글번호",
                "value": post["number"],
                "inline": True,
            },
            {
                "name": "작성자",
                "value": post["writer"],
                "inline": True,
            },
            {
                "name": "작성일",
                "value": post["date"],
                "inline": True,
            },
            {
                "name": "조회수",
                "value": post["views"],
                "inline": True,
            },
        ],
        "footer": {
            "text": "KGEU Board Monitor",
        },
    }

    payload = {
        "content": "📢 **새 게시글이 등록되었습니다.**",
        "embeds": [embed],
    }

    try:
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        Logger.success("Discord 알림 전송 완료")
        return True

    except requests.RequestException as e:
        Logger.error(f"Discord 알림 전송 실패: {e}")
        return False