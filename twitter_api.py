import optparse
import sys

import twitter
import util

def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.
    """
    api = twitter.Api()
    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        util.safe_print(tweet.GetText())

def trendingTopics():
    """
    Print the currently trending topics.
    """
    api = twitter.Api()
    trending_topics = api.GetTrendsCurrent()
    for topic in trending_topics:
        util.safe_print(topic.name)

def userTweets(username):
    """
    Print recent tweets by `username`.
    """
    pass

def trendingTweets():
    """
    Print tweets for all the trending topics.
    """
    pass

def main(args):
    parser = optparse.OptionParser("""Usage: %prog [-s <search term> | -t | -u <username>]""")

    parser.add_option("-s", "--search",
                      type="string",
                      action="store",
                      dest="search_term",
                      default=None,
                      help="Display tweets containing a particular string.")
    parser.add_option("-t", "--trending-topics",
                      action="store_true",
                      dest="trending_topics",
                      default=False,
                      help="Display the trending topics.")

    (opts, args) = parser.parse_args(args)

    if opts.search_term:
        search(opts.search_term)
    elif opts.trending_topics:
        trendingTopics()

if __name__ == "__main__":
    main(sys.argv[1:])
