import os
import feedparser
import requests
import json
import time

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = "-1004426971236"

FEEDS = [
    "http://feeds.reuters.com/reuters/topNews",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://oilprice.com/rss/main",
    "https://www.tasnimnews.com/fa/rss",
    "https://www.mehrnews.com/rss"
]

sent_file = "sent.json"

if os.path.exists(sent_file):
    with open(sent_file, "r") as f:
        sent = json.load(f)
else:
    sent = []

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(
        url,
        data={
            "chat_id": CHANNEL_ID,
            "text": text,
            "disable_web_page_preview": False
        }
    )

while True:
    for feed in FEEDS:
        data = feedparser.parse(feed)

        for item in reversed(data.entries[:5]):
            link = item.get("link")

            if link not in sent:
                title = item.get("title", "")
                msg = f"📰 {title}\n\n🔗 {link}"

                send_message(msg)
                sent.append(link)

                with open(sent_file, "w") as f:
                    json.dump(sent[-200:], f)

    time.sleep(300)
