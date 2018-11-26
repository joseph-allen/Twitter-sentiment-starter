from __future__ import absolute_import, print_function
from auth import consumer_key,consumer_secret,access_token, access_token_secret
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
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
        api = tweepy.API(auth)

        # Calculate Sentiment

        # Command Line logs
        pos = 'pos: ' + str(get_polarity('pos',text))
        neg = 'neg: ' + str(get_polarity('neg',text))
        neu = 'neu: ' + str(get_polarity('neu',text))
        compound = 'compound: ' + str(get_polarity('compound',text))
        
        print("Tweeting... " + text)
        # print(pos)
        # print (neg)
        # print (neu)
        # print (compound)

        # Tweet Test
        toTweet = text + '\n' + pos + '\n' +neg + '\n' + neu + '\n' + compound + '\n'
        print('toTweet' + toTweet)

        # Tweet out response
        api.update_status(toTweet)

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