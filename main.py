import time
import feedparser

from feeds import FEEDS
from duplicate_filter import (
    load_sent,
    is_duplicate,
    add_news
)
from news_filter import filter_news
from message_builder import build_message
from telegram_sender import send_message
from config import CHECK_COUNT

sent = load_sent()

while True:

    for source_name, feed in FEEDS.items():

        try:

            data = feedparser.parse(feed)

            if data.bozo:
                print(f"RSS Error : {source_name}")
                continue

            for item in reversed(data.entries[:CHECK_COUNT]):

                link = item.get("link", "")

                if is_duplicate(link, sent):
                    continue

                news = filter_news(item, source_name)

                if news is None:
                    continue

                message = build_message(news)

                send_message(message)

                add_news(link, sent)

        except Exception as e:
            print(f"{source_name}: {e}")

    time.sleep(300)
