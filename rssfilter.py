import feedparser
from parser import basic_parser

class FeedFilter(object):
    """
    """

    def __init__(self, feed_filter, news_callback=print, feeds=None, cache_feeds=True, cache_len=100):
        """
            :param feed_filter: A function which will be called every time when a new feed-message is recieved.
            This function decides, if the message is passed to the news_callback function.
            :param news_callback: A function wich is called whenever a new feed-message is recieved and not filtered.
            :param feeds: The feeds (more feeds can be added later)
            :param cache_feeds: Should the messages from the feeds be cached. '+': Filtering every message is not necessary, '-': requires more memory
        """
        self.feeds = {} if feeds is None else feeds
        self.feed_filter = feed_filter
        self.news_callback = news_callback

        self.cache_feeds = cache_feeds
        self.cache = []
        self.cache_len = cache_len

    def reload_feeds(self):
        """
            Reparses every currently registered feed
        """
        for feed in self.feeds:
            news = feedparser.parse(feed)

            for entry in news.entries:
                data = self.feeds[feed](entry)

                if self.cache_feeds:
                    if data in self.cache:
                        continue

                    self.cache.append(data)

                    if len(self.cache) > self.cache_len:
                        self.cache.pop(0)

                if self.feed_filter(data):
                    self.news_callback(data)


    def register_feed(self, url, parser=basic_parser):
        """
            Registers the feed.
            :param url: The feed-url
            :param parser: The function which is called every time a new message is recieved
        """
        self.feeds[url] = parser