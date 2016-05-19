import tweepy
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream, api
from twitter.api import TwitterDictResponse


consumer_key = 'T7JsF1OhyfFkCEEsBMkQJhYWF'
consumer_secret = 'rQw0Ofglx97yDURi7KzDofqMdAWGYU0XJsnBDzvcxM0POAqYln'
access_token = '167964900-rXIeVLiBCPGeIhntKzIbOXAOfCmq8hlVhoN3yofy'
access_secret = '4Ovozw9rcXEgi9X4pJhPvYP5q8txAU7oAlNJ7fC1PNHV4'

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track='#bernie2016,#trump2016,#hillary2016')


# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 100
trump_count = 0
hillary_count = 0
bernie_count = 0
for tweet in iterator:
    tweet_count -= 1
    result = TwitterDictResponse.keys(tweet)
    res = TwitterDictResponse.items(tweet)
    if "#bernie2016" in str(tweet).lower():
        bernie_count += 1
    elif "#trump2016" in str(tweet).lower():
        trump_count += 1
    elif "#hillary2016" in str(tweet).lower():
        hillary_count += 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    for key, value in res:
        if 'text' in key:
            print(value)
            print("^This is what we want^")
    print(res)
    print(tweet_count)
    print(type(tweet))

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break

print(bernie_count)
print(hillary_count)
print(trump_count)
