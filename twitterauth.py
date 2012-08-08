import sys
import tweepy

def tweet(the_tweet):
	CONSUMER_KEY = 'pq5eC6aJKQJQ3wJMO1N17g'
	CONSUMER_SECRET = 'bODGN3Ut8XgXVMpJAkDIfcehyhXQKRYJdwwQS806pI'
	ACCESS_KEY = '744249078-X8saEQi4y81ZfdS5NiA7EIllmasibO1LuFtwVGn8'
	ACCESS_SECRET = '23ufJRXpjwt6BRhOJcJ42pvlvc1ZLpw2Dm4zaLxzrOs'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status(the_tweet)