import tweepy
from tweepy import OAuthHandler

consumer_key = "H4VJP8RGGXge44FhiA0IDbSFc"
consumer_secret = "oasFMmJrmpDGhafqCwz87QA9Y0ZLiX1ZCsDFxEPU1fiupvV1CP"
access_token = "764283896875843585-BCjE7PpBCXP79XErClu9ufuNJzdu1LP"
access_secret = "L8Axk7IfqDt2HfH4E5BCH98S9d1P93z402CZF99fPIPCf"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)