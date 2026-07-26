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

    matched = set()

    country_found = False
    topic_found = False
    industry_found = False
    change_found = False

    # حذف کامل خبرهای نامرتبط
    for word in NEGATIVE_WORDS:
        if word.lower() in text:
            return False, 0, ""

    # عبارات مهم (فقط یک بار)
    for phrase, value in POSITIVE_PHRASES.items():
        key = phrase.lower()
        if key in text and key not in matched:
            score += value
            matched.add(key)

    # کشورها
    for word, value in COUNTRY_SCORES.items():
        key = word.lower()
        if key in text and key not in matched:
            score += value
            matched.add(key)
            country_found = True

    # موضوعات
    for word, value in TOPIC_SCORES.items():
        key = word.lower()
        if key in text and key not in matched:
            score += value
            matched.add(key)
            topic_found = True

    # صنایع
    for word, value in INDUSTRY_SCORES.items():
        key = word.lower()
        if key in text and key not in matched:
            score += value
            matched.add(key)
            industry_found = True

    # کلمات تغییر
    for word, value in CHANGE_WORDS.items():
        key = word.lower()
        if key in text and key not in matched:
            score += value
            matched.add(key)
            change_found = True

    # امتیاز هوشمند
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
