import optparse
import sys

import twitter
from util import encode

def printTweet(tweet):
    """
    Format and print `tweet`.
    """
    print "@" + tweet.GetUser().GetScreenName() + ": " + encode(tweet.GetText())

def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.
    """
    api = twitter.Api()
    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        print encode(tweet.GetText())

def trendingTopics():
    """
    Print the currently trending topics.
    """
    api = twitter.Api()
    trending_topics = api.GetTrendsCurrent()
    for topic in trending_topics:
        print encode(topic.name)

def userTweets(username):
    """
    Print recent tweets by `username`.
    """
    api = twitter.Api()
    userTweets = api.GetUserTimeline(screen_name=username)
    for tweet in userTweets:
        printTweet(tweet)

def trendingTweets():
    """
    Print tweets for all the trending topics.
    """
    api = twitter.Api()

    trending_topics = api.GetTrendsCurrent()
    tweets = []
    # To add some variety, let's round-robin through the trending
    # topics, displaying a tweet from each until we run out of tweets.
    for topic in trending_topics:
        tweets.append((topic, api.GetSearch(topic.name)))

    while True:
        for topic, topic_tweets in tweets:
            if topic_tweets:
                printTweet(topic_tweets.pop())
            else:
                return

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
    parser.add_option("-u", "--user",
                      type="string",
                      action="store",
                      dest="username",
                      default=None,
                      help="Display tweets for a particular public user.")
    parser.add_option("-w", "--trending-tweets",
                      action="store_true",
                      dest="trending_tweets",
                      default=None,
                      help="Display the tweets from trending topics.")

    (opts, args) = parser.parse_args(args)

    if opts.search_term:
        search(opts.search_term)
    elif opts.trending_topics:
        trendingTopics()
    elif opts.username:
        userTweets(opts.username)
    elif opts.trending_tweets:
        trendingTweets()
    
if __name__ == "__main__":
    main(sys.argv[1:])
