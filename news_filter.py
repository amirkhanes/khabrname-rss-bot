from scoring import score_news
from impact_detector import has_impact


def filter_news(item, source):

    title = item.get("title", "")
    summary = item.get("summary", "")
    link = item.get("link", "")

    text = f"{title}\n{summary}"

    # اگر هیچ اثر اقتصادی نداشت، رد شود
    if not has_impact(text):
        return None

    send, score, level = score_news(
        title=title,
        summary=summary,
        source=source
    )

    if not send:
        return None

    return {
        "title": title,
        "summary": summary,
        "link": link,
        "score": score,
        "level": level
    }
