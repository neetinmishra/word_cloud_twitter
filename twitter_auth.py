import tweepy
import os

# API Keys and Tokens
consumer_key = os.environ['API_KEY']
consumer_secret = os.environ['API_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
bearer_token = os.environ['BEARER_TOKEN']
client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=False)
print("Successfully Authenticated")

if __name__ == "__main__":
    file = open('./data.txt', 'w+', encoding="utf-8")
    query = 'from:PMOIndia -is:retweet'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)
    paginator = tweepy.Paginator(
    client.search_recent_tweets,           # The method you want to use
    query=query,                           # Some argument for this method
    max_results=100                        # How many tweets asked per request
    )

    for tweet in paginator.flatten(limit=100000): # Total number of tweets to retrieve
        print(tweet)
    # for tweet in tweets.data:
    #     print(tweet.text)
        file.write(str(tweet.text))
    file.close()
