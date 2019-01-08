from __future__ import absolute_import, print_function
from auth import consumer_key,consumer_secret,access_token, access_token_secret
from endpoints import good, bad
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import urllib.request
# sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        obj = json.loads(data)
        text = obj['text']

        # Calculate Sentiment
        compound = get_polarity('compound',text)
        
        print("Recieved Tweet: " + text)

        # send a http req to our endpoint
        print('Compound Score : ' + str(compound))
        if(compound > 0):
            print('NURTURE')
            urllib.request.urlopen(good).read()
        if(compound < 0):
            print('DESTROY')
            urllib.request.urlopen(bad).read()

        return True

    def on_error(self, status):
        print('error:' + str(status))

def get_polarity(key, string):
    ss = sid.polarity_scores(string)
    return ss[key] 
    
def setup_auth():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    return auth


if __name__ == '__main__':
    l = StdOutListener()
    auth = setup_auth()
    sid = SentimentIntensityAnalyzer()

    stream = Stream(auth, l)

    # filter for tweets at a particular user only, in this case realdonaldtrump
    stream.filter(track=['@realdonaldTrump'])