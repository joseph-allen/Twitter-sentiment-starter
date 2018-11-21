import tweepy
from auth import consumer_token,consumer_secret,access_token, access_secret

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get Any New Tweets
    # Calculate their Sentiment
    # Tweet out results


# twts = api.search(q="@pydataMCR") 
# Tweet
api.update_status('Updating using OAuth authentication via Tweepy!')