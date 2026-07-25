from config import MESSAGE_TITLE


def build_message(news):

    return f"""🟦 {MESSAGE_TITLE}

{news["level"]} امتیاز خبر: {news["score"]}/100

📰 {news["title"]}

🔗 {news["link"]}"""
