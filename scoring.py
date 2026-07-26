from keywords import (
    SOURCE_SCORE,
    MIN_SCORE,
    COUNTRY_SCORES,
    TOPIC_SCORES,
    CHANGE_WORDS,
    INDUSTRY_SCORES,
    POSITIVE_PHRASES,
    NEGATIVE_WORDS
)


def score_news(title, summary="", source=""):

    text = (title + " " + summary).lower()

    score = SOURCE_SCORE

    country_found = False
    topic_found = False
    industry_found = False
    change_found = False

    # حذف خبرهای نامرتبط
    for word in NEGATIVE_WORDS:
        if word.lower() in text:
            return False, 0, ""

    # عبارات مهم
    for phrase, value in POSITIVE_PHRASES.items():
        if phrase.lower() in text:
            score += value

    # کشورها
    for word, value in COUNTRY_SCORES.items():
        if word.lower() in text:
            score += value
            country_found = True

    # موضوعات
    for word, value in TOPIC_SCORES.items():
        if word.lower() in text:
            score += value
            topic_found = True

    # صنایع
    for word, value in INDUSTRY_SCORES.items():
        if word.lower() in text:
            score += value
            industry_found = True

    # کلمات تغییر
    for word, value in CHANGE_WORDS.items():
        if word.lower() in text:
            score += value
            change_found = True

    # ضریب هوشمند
    if country_found and topic_found:
        score += 10

    if industry_found and change_found:
        score += 10

    if country_found and industry_found and change_found:
        score += 10

    if topic_found and industry_found and change_found:
        score += 10

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
