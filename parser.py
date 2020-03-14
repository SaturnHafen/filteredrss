import sys

def basic_parser(feed_entry) -> tuple:
    """
        Parses the url, the title and content of the rss message
        :feed_entry: The feed_entry dict to analyse.
        :return: A tuple (title, link, content)
    """
    return feed_entry.title, feed_entry.links[0].href, feed_entry.content[1].value