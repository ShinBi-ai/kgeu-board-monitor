import requests
from bs4 import BeautifulSoup

from boards.kgeu import BOARD


def get_latest_post():
    response = requests.get(
        BOARD["url"],
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    posts = soup.select("li.board__li__data")

    if not posts:
        raise Exception("게시글을 찾을 수 없습니다.")

    latest = None

    for post in posts:
        if "board__li__notice" in post.get("class", []):
            continue

        latest = post
        break

    if latest is None:
        raise Exception("일반 게시글이 없습니다.")

    title_tag = latest.select_one("p.board__title a")

    return {
        "id": title_tag["href"].split("/")[-1].split("?")[0],
        "title": title_tag.get_text(strip=True),
        "url": BOARD["base_url"] + title_tag["href"],
        "number": latest.select_one("p.board__no").get_text(strip=True),
        "date": latest.select_one("p.board__date").get_text(strip=True),
        "writer": latest.select_one("p.board__name").get_text(strip=True),
        "views": latest.select_one("p.board__hit").get_text(strip=True),
    }