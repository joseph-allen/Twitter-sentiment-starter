# Twitter-sentiment-starter
This project lets you quickstart a Twitter account to respond to all incoming Tweets to your account with the Sentiment of that Tweet.

# Twitter Developer account
As of July 2018 you now have to have a Twitter Developer account. This process is simple.

go to [https://apps.twitter.com/](Link)

On here you have to "Create an App"

Once this is done you can select "Keys and Tokens" to get your:
* API Key
* Secret API Key

at the root of this project create a file called `auth.json` and populate is as follows:

```
consumer_token="YOUR_API_KEY"
consumer_secret="YOUR_SECRET_API_KEY"
```