from rssfilter import FeedFilter
from parser import basic_parser
from filter import basic_text_filter
from functools import partial

if __name__ == '__main__':

    f = FeedFilter(feed_filter=partial(basic_text_filter, filter_words=['corona', 'Corona', 'Coronavirus', 'Wuhan', 'Coronaepidemie', 'Corona-Epidemie']), news_callback=print)
    f.register_feed("http://www.tagesschau.de/xml/rss2", basic_parser)
    f.reload_feeds()