from boards.kgeu import BOARD
from modules.crawler import get_latest_post
from modules.notifier import send_notification
from modules.storage import load_last_post_id, save_last_post_id
from modules.logger import Logger


def main():
    Logger.banner()

    Logger.info(f"게시판 : {BOARD['display_name']}")

    try:
        post = get_latest_post()
    except Exception as e:
        Logger.error(f"게시판 조회 실패: {e}")
        raise

    Logger.success("게시판 접속 성공")
    Logger.info(f"최신 게시글 : {post['id']}")

    last_post = load_last_post_id(BOARD["name"])
    Logger.info(f"저장된 게시글 : {last_post}")

    # 첫 실행
    if last_post is None:
        Logger.warning("첫 실행입니다.")
        Logger.info("테스트를 위해 최신 게시글을 Discord로 전송합니다.")

        if send_notification(post):
            save_last_post_id(BOARD["name"], post["id"])

        return

    # 새 글 없음
    if last_post == post["id"]:
        Logger.info("새 게시글이 없습니다.")
        return

    # 새 글 발견
    Logger.success("새 게시글 발견!")

    if send_notification(post):
        save_last_post_id(BOARD["name"], post["id"])
        Logger.success("상태 저장 완료")


if __name__ == "__main__":
    main()