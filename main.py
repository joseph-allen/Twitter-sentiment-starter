from __future__ import absolute_import, print_function
from auth import consumer_key,consumer_secret,access_token, access_token_secret
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
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
    stream.filter(track=['basketball'])