import optparse
import sys

import twitter_functions

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
    parser.add_option("-u", "--user-tweets",
                      type="string",
                      action="store",
                      dest="user_tweets",
                      default=False,
                      help="Display a user's tweets.")
    parser.add_option("-w", "--trending-tweets",
                      action="store_true",
                      dest="trending_tweets",
                      default=False,
                      help="Display tweets from all of the trending topics.")

    (opts, args) = parser.parse_args(args)

    if opts.search_term:
        twitter_functions.search(opts.search_term)
    elif opts.trending_topics:
        twitter_functions.trendingTopics()
    elif opts.user_tweets:
        twitter_functions.userTweets(opts.user_tweets)
    elif opts.trending_tweets:
        twitter_functions.trendingTweets()

if __name__ == "__main__":
    main(sys.argv[1:])
