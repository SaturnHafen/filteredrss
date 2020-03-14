
def basic_text_filter(feed_entry, filter_words):
    for filter_word in filter_words:
        if feed_entry[2].find(filter_word) > -1:
            return True
    return False