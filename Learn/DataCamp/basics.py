""" code snippets and notes from foundation courses """

import glob
import json
import os
import re

import tweepy

# --------------------------------------------------------
# OS
# --------------------------------------------------------

# list files in the working directory


def list_files_in_wd():
    """ list all files in the working directory """
    print(os.listdir(os.getcwd()))


# Globbing = pattern matching for file names
#            wildcards allowed e.g. *.csv

csv_files = glob.glob('*.csv')

# RegEx
# 17 = \d   
# $17 = \$\d*  $17.00 = \$\d*\.\d*  or \$\d*\.\{2}d*

pattern1 = re.compile('\$\d*\.\d{2}')
result = pattern1.match('$17.89')
print(bool(result))

# find the numeric values: matches
pattern2 = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
print(pattern2)

pattern3 = bool(re.match(pattern='[A-Z\w*]', string='Australia'))
print(pattern3)

# --------------------------------------------------------
# List comprehensions
# --------------------------------------------------------

num_list = [num ** 2 for num in range(1000) if num % 2 == 0]
print(num_list)

# --------------------------------------------------------
# Twitter WebAPI
# --------------------------------------------------------

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet_list = []
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        tweet_list.append(status)
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

# NEED REAL ACCOUNT !!!
# OAuth authentication credentials in relevant variables
#access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
#access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
#consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
#consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

# Initialize Stream listener
#l = MyStreamListener()

# Create your Stream object with authentication
#stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
#stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])
