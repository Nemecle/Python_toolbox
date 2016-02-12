#!/usr/bin/python
# coding: latin-1
"""
based on https://gist.github.com/yanofsky/5436496

"""

import tweepy


def get_all_tweets(screen_name):
    """
    get 3200 last tweets of a given @

    """


    tokens = open("Zoehmacarena.tokens", "r")
    consumer_key = tokens.readline()[:-1]
    consumer_secret = tokens.readline()[:-1]
    access_token = tokens.readline()[:-1]
    access_secret = tokens.readline()[:-1]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)


    alltweets = []

    lasttweets = api.user_timeline(screen_name=screen_name, count=200)

    alltweets.extend(lasttweets)


    oldest = alltweets[-1].id - 1


    while len(lasttweets) > 0:
        # print "getting tweets before %s" % (oldest)


        lasttweets = api.user_timeline(screen_name=screen_name, \
            count=200, max_id=oldest)

        alltweets.extend(lasttweets)

        oldest = alltweets[-1].id - 1

        # print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [tweet.text.encode("utf-8") for tweet in alltweets]

    return outtweets
