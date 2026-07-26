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

    # حذف خبرهای نامرتبط
    for word in NEGATIVE_WORDS:
        if word.lower() in text:
            return False, 0, ""

    # هر عبارت فقط یک بار امتیاز بگیرد
    for phrase, value in POSITIVE_PHRASES.items():
        if phrase.lower() in text:
            score += value

    for dictionary in (
        COUNTRY_SCORES,
        TOPIC_SCORES,
        INDUSTRY_SCORES,
        CHANGE_WORDS,
    ):
        for word, value in dictionary.items():
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
