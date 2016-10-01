""" Streaming twitter API example """

from __future__ import print_function
import sys
import tweepy
from ConfigParser import ConfigParser

class TwitterListener(tweepy.StreamListener):
    """ Twitter stream listener. """
    def on_status(self, tweet):
        print(tweet.text)

    def on_error(self, msg):
        print('Error: %s', msg)

    def on_timeout(self):
        print('timeout : wait for next poll')
        sleep(10)

def get_config():
    """ Get the configuration """
    conf = ConfigParser()
    conf.read('../cfg/sample.cfg')
    return conf

def get_stream():
    config = get_config()
    auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'),
                               config.get('twitter', 'consumer_secret'))

    auth.set_access_token(config.get('twitter', 'access_token'),
                          config.get('twitter', 'access_token_secret'))

    listener = TwitterListener()
    stream = tweepy.Stream(auth=auth, listener=listener)
    return stream

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % (sys.argv[0]))
    else:
        word = sys.argv[1]
        stream = get_stream()
        print("Listening to '%s' and '%s' ..." %('#' + word, word))
        stream.filter(track=['#' + word, word])
