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
