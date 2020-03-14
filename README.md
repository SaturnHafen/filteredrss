# filteredrss
A python rss-feed parser which supports filtering.

## API
`rssfilter.FeedFilter(self, feed_filter, news_callback=print, feeds=None, cache_feeds=True, cache_len=100)`
Initializes the FeedFilter.
`feed_filter`: is the filter function to apply to all messages from the feeds.
`news_callback`: will be called on every message that is not filtered by `feed_filter`.
`feeds`: The dict with the initial feeds (`{ url: parser }`).
`cache_feeds`: Should the feeds be cached (+: faster parse times, -: memory consumption).
`cache_len`: Maximum size of the cache.

`rssfilter.FeedFilter.reload_feeds(self) -> None`
Reloads and reparses every feed.

`rssfilter.FeedFilter.register_feed(self, url, parser=basic_parser) -> None`
Adds a new feed to the FeedFilter.
`url`: The url to the rss-feed.
`parser`: The parser-function which should be used when a feed-message is recieved.

`parser.basic_parser(feed_entry) -> tuple`
An example parser for a feed-entry. If you use it, check that all the fields mach up.
`feed_entry`: A feed entry dict (with probably much more information than needed).
return: `(title, url, content)`.

`filter.basic_text_filter(feed_entry: tuple, filter_words) -> bool`
A basic filter which looks at in content of the rss-message for the specified words
`feed_entry` The parsed feedEntry `(title, url, content)`.
`filter_words` A list with all words to filter (case sensitive!).
return: `True` matches filter, `False` does not match filter

### parser-api-contract
arguments: type `dict`, pattern depends on feed
return: type `tuple`, pattern `(title: str, url: str, content: str)`

### filter-api-contract
arguments: type `tuple`, pattern `(title: str, url: str, content: str)`
return: type `bool`, `True` -> matches filter
