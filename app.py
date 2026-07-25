from boards.kgeu import BOARD
from modules.crawler import get_latest_post
from modules.notifier import send_notification
from modules.storage import load_last_post_id, save_last_post_id


def main():
    post = get_latest_post()

    last_id = load_last_post_id(BOARD["name"])

    if last_id is None:
        print("첫 실행입니다.")
        save_last_post_id(BOARD["name"], post["id"])
        return

    if last_id == post["id"]:
        print("새 게시글이 없습니다.")
        return

    print("새 게시글 발견!")
    send_notification(post)
    save_last_post_id(BOARD["name"], post["id"])


if __name__ == "__main__":
    main()