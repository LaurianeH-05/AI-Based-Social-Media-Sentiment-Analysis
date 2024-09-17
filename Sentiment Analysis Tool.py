import tweepy
from textblob import TextBlob
import matplotlib as plt

auth = tweepy.OAuth1UserHandler("API_KEY", "API_SECRET_KEY")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
api = tweepy.API(auth)

tweets = api.search(q="your_serach_term", count=100, lang="en" and "fr")
tweet_data = [tweet.text for tweet in tweets]

def sentiment_analysis(text):
    analysis = TextBlob(text)
    if analysis.sentiment.popularity > 0:
        return "Positive"
    elif analysis.sentiment.popularity < 0:
        return "Negative"
    else:
        return "Neutral"
    
sentiments = [sentiment_analysis(tweet) for tweet in tweet_data]

sentiment_count =
pd.Series(sentiments).value_counts()
sentiment_count.plot(kind="bar")
plt.title("Sentiment Dsitribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()