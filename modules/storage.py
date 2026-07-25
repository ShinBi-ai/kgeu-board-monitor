import json
import os

from config import STATE_FILE


def _load_state():
    if not os.path.exists(STATE_FILE):
        return {"boards": {}}

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(
            state,
            f,
            ensure_ascii=False,
            indent=4,
        )


def load_last_post_id(board_name):
    state = _load_state()

    return (
        state
        .get("boards", {})
        .get(board_name, {})
        .get("last_post_id")
    )


def save_last_post_id(board_name, post_id):
    state = _load_state()

    state.setdefault("boards", {})
    state["boards"].setdefault(board_name, {})

    state["boards"][board_name]["last_post_id"] = post_id

    _save_state(state)