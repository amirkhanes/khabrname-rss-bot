from keywords import (
    SOURCE_SCORE,
    MIN_SCORE,
    COUNTRY_SCORES,
    TOPIC_SCORES,
    CHANGE_WORDS,
    NEGATIVE_WORDS,
)


def score_news(title, summary="", source=""):

    text = (title + " " + summary).lower()

    score = 0

    if source:
        score += SOURCE_SCORE

    # حذف خبرهای نامرتبط
    for word in NEGATIVE_WORDS:
        if word.lower() in text:
            return False, 0, ""

    # هر کلمه فقط یکبار امتیاز می‌گیرد
    for word, value in COUNTRY_SCORES.items():
        if word.lower() in text:
            score += value

    for word, value in TOPIC_SCORES.items():
        if word.lower() in text:
            score += value

    for word, value in CHANGE_WORDS.items():
        if word.lower() in text:
            score += value

    if score > 100:
        score = 100

    if score < MIN_SCORE:
        return False, score, ""

    if score >= 95:
        level = "🚨🔥🔥🔥"
    elif score >= 80:
        level = "🔥🔥"
    else:
        level = "🔥"

    return True, score, level
