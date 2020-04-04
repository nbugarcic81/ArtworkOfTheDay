import tweepy

CONSUMER_KEY = '*******'
CONSUMER_SECRET = '*******'
ACCESS_TOKEN = '*******'
ACCESS_TOKEN_SECRET = '*******'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def twitter_post(tweet_text, image_path):
	api.update_with_media(image_path, tweet_text)

