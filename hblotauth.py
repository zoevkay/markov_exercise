#!/usr/bin/env python

import sys
import tweepy

def tweet(the_tweet):

	CONSUMER_KEY = 'fill here'
	CONSUMER_SECRET = 'fill here'
	ACCESS_KEY = 'fill'
	ACCESS_SECRET = 'fill'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status(the_tweet)