import time
import feedparser

from feeds import FEEDS
from duplicate_filter import load_sent, is_duplicate, add_news
from news_filter import filter_news
from message_builder import build_message
from telegram_sender import (
    send_message,
    send_warning,
    send_recovered
)
from rss_monitor import (
    feed_failed,
    mark_failed,
    mark_ok
)
from config import CHECK_COUNT

sent = load_sent()

while True:

    for source_name, feed in FEEDS.items():

        try:

            data = feedparser.parse(feed)

            if data.bozo:

                if not feed_failed(source_name):
                    send_warning(source_name, "RSS Parse Error")
                    mark_failed(source_name)

                continue

            else:

                if feed_failed(source_name):
                    send_recovered(source_name)
                    mark_ok(source_name)

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

            if not feed_failed(source_name):
                send_warning(source_name, str(e))
                mark_failed(source_name)

    time.sleep(300)
