# Twitter-sentiment-starter
This project lets you quickstart a Twitter account to respond to all incoming Tweets to your account with the Sentiment of that Tweet.

# Twitter Developer account
As of July 2018 you now have to have a Twitter Developer account. This process is simple.

go to [https://apps.twitter.com/](Link)

On here you have to "Create an App"

Once this is done you can select "Keys and Tokens" to get your:
* API Key
* Secret API Key
* Access Token
* Access Token Secret

at the root of this project create a file called `auth.json` and populate is as follows:

```
consumer_key="YOUR_API_KEY"
consumer_secret="YOUR_SECRET_API_KEY"
access_token="YOUR_ACCESS_TOKEN"
access_token_secret="YOUR_SECRET_ACCESS_TOKEN"
```

# Sentiment Analysis
Run a Python terminal, then run the following:
```
 >>> import nltk
>>> nltk.download('vader_lexicon')
```