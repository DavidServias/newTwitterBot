import tweepy
import datetime
import time
from dateutil import tz


# Authenticate to Twitter
auth = tweepy.OAuthHandler(# [keys from tweepy]#)
auth.set_access_token(#[token from tweepy]#)
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


#
