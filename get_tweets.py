import tweepy
import json

#keys_from twitter developers
consumer_key = "LMMPJnWG6XRteQKKxLuSZn8GU"
consumer_secret = "MTW7rK5c3ZJkCaelfnHfCoxwU9J9NF1kawW2VnT3rd5gyCWHoY"
access_key = "74116398-czOwcbPjQzDnFa2ONmKsTM6g0xgoiuHQDh3LxVnRQ"
access_secret = "FO7Svk6RZeDiJHa1fI8QR3PXibXaVRFfa7zEIAD7hWx6n"


# Function to extract tweets
def get_tweets(username,count_req):
    # Authorization &Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Actaul;y calling for tweets
    tweets = api.user_timeline(screen_name=username, count=count_req)
    handle=username
    name=""
    body=""
    for tweet in tweets:
        tweet_info=json.dumps(tweet._json)
        json_tweet=json.loads(tweet_info)
        name=json_tweet["user"]["name"]
        body=body+json_tweet["created_at"]+"\t"+str(json_tweet["text"]).replace("\n"," ")+"\n"

    #printing tweets as text and in file as csv
    outfile="tweets.tsv"
    f=open(outfile,"w")
    f.write("Handle:@"+handle+"\tName:"+name+"\n\n\nPosted On\tTweet\n"+body)
    f.close()



get_tweets("PMOindia",200)