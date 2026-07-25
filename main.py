import feedparser

from feeds import FEEDS
from duplicate_filter import load_sent, is_duplicate, add_news
from news_filter import filter_news
from message_builder import build_message
from telegram_sender import send_message


sent = load_sent()

for feed in FEEDS:

    data = feedparser.parse(feed)

    for item in reversed(data.entries[:10]):

        link = item.get("link", "")

        if is_duplicate(link, sent):
            continue

        news = filter_news(item, feed)

        if news is None:
            continue

        message = build_message(news)

        send_message(message)

        add_news(link, sent)
