from config import MESSAGE_TITLE


def build_message(news):

    score = news["score"]
    level = news["level"]

    if score >= 95:
        priority = "اولویت بسیار بالا"
    elif score >= 80:
        priority = "اولویت بالا"
    else:
        priority = "اولویت متوسط"

    return f"""🟦 {MESSAGE_TITLE}

{level} {priority}

📊 امتیاز: {score}/100

📰 {news["title"]}

🔗 {news["link"]}"""
