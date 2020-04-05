import time

from twitterbot import TwitterBot

import config

def tweet():
	bot = TwitterBot(
		twitter_consumer_key = config.twitter_consumer_key
		,twitter_consumer_secret = config.twitter_consumer_secret
		,twitter_access_key = config.twitter_access_key
		,twitter_access_secret = config.twitter_access_secret
		# ,search_terms = ['lockdown','COVID-19']
		,search_on='twitter'
		# ,search_on='news'
		,bitly_access_token = config.bitly_access_token
		,news_api_key = config.news_api_key
	)

	# Configure tweet and create lists for tweets based on search_on parameter
	bot.configure_tweet(status_type= 'rt')
	# bot.configure_tweet(status= 'Latest News')
	bot.create_list()

	# Look at created list
	bot.list

	# Send tweets using created list
	bot.sendTweets()

	# sleep for 60 sec, i.e 1 min
	time.sleep(1800)

while True:
	tweet()