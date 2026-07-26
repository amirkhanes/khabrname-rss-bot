import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = "-1004426971236"

def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:

        requests.post(
            url,
            data={
                "chat_id": CHANNEL_ID,
                "text": text,
                "disable_web_page_preview": False
            },
            timeout=20
        )

    except Exception as e:
        print(e)


def send_warning(source, error):

    text = (
        f"⚠️ RSS ERROR\n\n"
        f"Source : {source}\n\n"
        f"{error}"
    )

    send_message(text)


def send_recovered(source):

    text = (
        f"✅ RSS RECOVERED\n\n"
        f"Source : {source}"
    )

    send_message(text)
