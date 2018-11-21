from __future__ import absolute_import, print_function
from auth import consumer_key,consumer_secret,access_token, access_token_secret
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        obj = json.loads(data)
        text = obj['text']
        # TODO: Calculate Sentiment
        # Tweet out response
        api = tweepy.API(auth)
        # api.update_status(text)
        print("Tweeting... " + text)

        return True

    def on_error(self, status):
        print(status)

def setup_auth():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    return auth

if __name__ == '__main__':
    l = StdOutListener()
    auth = setup_auth()

    stream = Stream(auth, l)
    # filter for tweets at a particular user only, in this case realdonaldtrump
    stream.filter(track=['@realdonaldTrump'])