import json
import os

from config import STATE_FILE
from modules.logger import Logger


def _create_default_state():
    return {
        "boards": {}
    }


def load_state():
    if not os.path.exists(STATE_FILE):
        Logger.warning("state.json이 없어 새로 생성합니다.")
        return _create_default_state()

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)

        if "boards" not in state:
            state["boards"] = {}

        return state

    except Exception as e:
        Logger.error(f"state.json 읽기 실패: {e}")
        return _create_default_state()


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=4)


def load_last_post_id(board_name):
    state = load_state()

    board = state["boards"].get(board_name)

    if board is None:
        return None

    return board.get("last_post_id")


def save_last_post_id(board_name, post_id):
    state = load_state()

    if board_name not in state["boards"]:
        state["boards"][board_name] = {}

    state["boards"][board_name]["last_post_id"] = str(post_id)

    save_state(state)

    Logger.success(
        f"{board_name} 게시판 마지막 게시글 ID 저장 완료 ({post_id})"
    )