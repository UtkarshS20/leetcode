import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets["char_count"]= tweets["content"].apply(len)
    tweets_filtered = tweets[tweets["char_count"]>15]
    tweets_filtered.drop(columns=["content", "char_count"], inplace=True)
    return tweets_filtered
    
tweets = pd.DataFrame([[1,"Let us Code"],
[2,"More than fifteen chars are here!"]], columns=["tweet_id","content"])

print(invalid_tweets(tweets))