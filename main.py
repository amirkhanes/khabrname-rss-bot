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

    for feed in FEEDS:

        try:
            data = feedparser.parse(feed)

            for item in reversed(data.entries[:CHECK_COUNT]):

                link = item.get("link", "")

                if is_duplicate(link, sent):
                    continue

                news = filter_news(item, feed)

                if news is None:
                    continue

                message = build_message(news)

                send_message(message)

                add_news(link, sent)

        except Exception as e:
            print(e)

    time.sleep(300)
