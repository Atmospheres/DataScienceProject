import twitter
import TwitterAPI
import tweepy
from TwitterAPI import TwitterAPI
from tweepy import OAuthHandler

consumer_key = 'T7JsF1OhyfFkCEEsBMkQJhYWF'
consumer_secret = 'rQw0Ofglx97yDURi7KzDofqMdAWGYU0XJsnBDzvcxM0POAqYln'
access_token = '167964900-rXIeVLiBCPGeIhntKzIbOXAOfCmq8hlVhoN3yofy'
access_secret = '4Ovozw9rcXEgi9X4pJhPvYP5q8txAU7oAlNJ7fC1PNHV4'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class PresidentialTrends():

   def get_bernie_tweets(self):
      r = api.request('search/tweets', {'q': '#trump2016'})
