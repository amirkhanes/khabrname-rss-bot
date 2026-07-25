from scoring import score_news


def filter_news(item, source):

    title = item.get("title", "")
    summary = item.get("summary", "")
    link = item.get("link", "")

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
