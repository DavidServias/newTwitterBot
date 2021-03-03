import tweepy
import datetime
import time
from dateutil import tz


# Authenticate to Twitter
auth = tweepy.OAuthHandler("8vY1MGJyP5RMt1TIAHaHa0KRU", "oFzAk0JFmDsL2QksP1eORZYPNa13umzbR1SSiUvwkBi3NtjByn")
auth.set_access_token('1131738695055290370-WfBUslKXoOperT0fO16F87Gf2GwxER', 'JQroHGaVHmbyQpS01TkAkqoXk755GrX5pqX7d4MKCuQrH')
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def get_next_isd():
    pacific = tz.gettz("America/Toronto")
    today = datetime.datetime.now(tz=pacific)
    year = today.year
    if today.month <= 11 and today.day <= 3:
        next_isd = datetime.datetime(year, 11, 3, 0, 0, 0, 0, pacific)
    else:
        next_isd = datetime.datetime((year+1), 11, 3, 0, 0, 0, 0, pacific)

    return next_isd


def make_tweet():
    pacific = tz.gettz("America/Toronto")
    while True:
        days_to_next_isd = get_next_isd() - datetime.datetime.now(tz=pacific)
        if days_to_next_isd == 0:
            tweet_text = "Eat a sandwich today! TODAY IS NATIONAL SANDWICH DAY!!!!!"
        elif days_to_next_isd == 1:
            tweet_text = "Stock up on bread and sandwich fixings, because TOMORROW IS NATIONAL SANDWICH DAY!!!!!"
        else:
            tweet_text = "There are " + str(days_to_next_isd.days) + " days until National Sandwich Day."
        print(datetime.datetime.now(tz=pacific))
        print(tweet_text)
        # api.update_status(tweet_text)
        time.sleep(30)


make_tweet()


# api.update_status("I'm making a new twitter bot. There might be some weird test tweets.")


# Bearer Token:
# AAAAAAAAAAAAAAAAAAAAAIcoNQEAAAAAfqfJ325NcKMMDqotMscxmBwtUNs%3DpCdm5Pn1Yj1DngLKi3EZuxbOLljhw0mfowkSSCXwI7juzJp9Uj
