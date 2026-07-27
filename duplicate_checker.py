_seen_titles = []


def normalize(text):

    text = text.lower()

    chars = [
        "،", ",", ".", ":", ";",
        "!", "؟", "(", ")", "[", "]",
        "{", "}", "-", "_", "/", "\\",
        "\"", "'", "«", "»"
    ]

    for c in chars:
        text = text.replace(c, " ")

    text = " ".join(text.split())

    return text


def similarity(a, b):

    a = set(normalize(a).split())
    b = set(normalize(b).split())

    if not a or not b:
        return 0

    return len(a & b) / len(a | b)


def is_duplicate_in_cycle(title, threshold=0.80):

    global _seen_titles

    for old in _seen_titles:

        if similarity(title, old) >= threshold:
            return True

    _seen_titles.append(title)

    return False


def reset_cycle():

    global _seen_titles
    _seen_titles = []
