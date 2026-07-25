from boards.kgeu import BOARD
from modules.crawler import get_latest_post
from modules.notifier import send_notification
from modules.storage import load_last_post_id, save_last_post_id
from modules.logger import Logger


def main():
    Logger.banner()

    Logger.info(f"게시판 : {BOARD['display_name']}")

    post = get_latest_post()

    Logger.success("게시판 접속 성공")

    Logger.info(f"최신 게시글 : {post['id']}")

    last_post = load_last_post_id(BOARD["name"])

    Logger.info(f"저장된 게시글 : {last_post}")

    if last_post is None:
        Logger.warning("첫 실행입니다.")
        save_last_post_id(BOARD["name"], post["id"])
        return

    if last_post == post["id"]:
        Logger.info("새 게시글이 없습니다.")
        return

    Logger.success("새 게시글 발견!")

    send_notification(post)

    save_last_post_id(BOARD["name"], post["id"])

    Logger.success("상태 저장 완료")


if __name__ == "__main__":
    main()