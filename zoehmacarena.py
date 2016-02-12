#!/usr/bin/python
# coding: latin-1
"""
file used for small tests. don't mind it

"""

import tweepy
from time import sleep
from tweepy import OAuthHandler

import markov_test as mt
import tweet_dumper

def getstatus():
    """
    generate status, remove mentions and reduce to 140 characters

    """
    status = "hmmmm je suis à court d'idée. @Nemecle (Error message)"

    status = mt.get_rand_string(20, "zoepetitchat_tweets.csv")
    status = status.replace('@', '')

    #limit to 140 characters
    status = " ".join(status[:140].split()[:-1])

    return status

def bot_invasion(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    fo = open("Zoehmacarena.tokens", "r")
    consumer_key = fo.readline()[:-1]
    consumer_secret = fo.readline()[:-1]
    access_token = fo.readline()[:-1]
    access_secret = fo.readline()[:-1]

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)


    for x in range(1000):
        status = getstatus()
        api.update_status(status)
        print "I tweeted \"" + status + "\""
        sleep(62)


    pass

def main():

    bot_invasion("nemecle")


    return

if __name__ == '__main__':
    main()

