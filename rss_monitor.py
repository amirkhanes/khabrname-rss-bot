failed_feeds = set()


def feed_failed(name):
    return name in failed_feeds


def mark_failed(name):
    failed_feeds.add(name)


def mark_ok(name):
    failed_feeds.discard(name)
