import json
import os

from config import MAX_SENT_NEWS

SENT_FILE = "sent.json"


def load_sent():

    if os.path.exists(SENT_FILE):

        with open(SENT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return []


def save_sent(sent):

    with open(SENT_FILE, "w", encoding="utf-8") as f:
        json.dump(sent[-MAX_SENT_NEWS:], f, ensure_ascii=False)


def is_duplicate(link, sent):

    return link in sent


def add_news(link, sent):

    sent.append(link)

    save_sent(sent)
