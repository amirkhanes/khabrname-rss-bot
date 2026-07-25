import requests
from config import BOT_TOKEN, CHANNEL_ID


def send_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHANNEL_ID,
            "text": message,
            "disable_web_page_preview": False
        },
        timeout=30
    )
