import datetime
from dateutil import tz
import keys
import tweepy


sandwich = keys.sandwich
gnosandwich = keys.gnosandwich

# Authenticate sandwich Account
auth_sandwich = tweepy.OAuthHandler(sandwich["api_key"], sandwich["api_secret"])
auth_sandwich.set_access_token(sandwich["token_key"], sandwich["token_secret"])
api_sandwich = tweepy.API(auth_sandwich)
try:
    api_sandwich.verify_credentials()
    print("Sandwich Authentication OK")
except:
    print("Error during sandwich authentication")


# Authenticate gnosandwich Account
auth_gnosandwich = tweepy.OAuthHandler(gnosandwich["api_key"], gnosandwich["api_secret"])
auth_gnosandwich.set_access_token(gnosandwich["token_key"], gnosandwich["token_secret"])
api_gnosandwich = tweepy.API(auth_gnosandwich)
try:
    api_gnosandwich.verify_credentials()
    print("Sandwich Authentication OK")
except:
    print("Error during sandwich authentication")


# get next national sandwich day
def get_next_date(month, day):
    pacific = tz.gettz("America/Toronto")
    today = datetime.datetime.now(tz=pacific)
    year = today.year
    if today.month < month or (today.month == month and today.day <= day):
        next_date = datetime.datetime(year, month, day, 0, 0, 0, 0, pacific)
    else:
        next_date = datetime.datetime((year+1), month, day, 0, 0, 0, 0, pacific)

    return next_date


def update_sandwich_tweet():
    pacific = tz.gettz("America/Toronto")
    days_to_next_nsd = get_next_date(11, 3) - datetime.datetime.now(tz=pacific)
    if days_to_next_nsd == 0:
        tweet_text = "Eat a sandwich today! TODAY IS NATIONAL SANDWICH DAY!!!!!"
    elif days_to_next_nsd == 1:
        tweet_text = "Stock up on bread and sandwich fixings, because TOMORROW IS NATIONAL SANDWICH DAY!!!!!"
    else:
        tweet_text = "There are " + str(days_to_next_nsd.days) + " days until National Sandwich Day."
    print(datetime.datetime.now(tz=pacific))
    print(tweet_text)
    api_sandwich.update_status(tweet_text)


def update_gnosandwich_tweet():
    pacific = tz.gettz("America/Toronto")
    days_to_next_gnosandwich = get_next_date(5,23) - datetime.datetime.now(tz=pacific)
    if days_to_next_gnosandwich == 0:
        tweet_text = "Eat anything but a sandwich today, because TODAY IS INTERNATIONAL GNOSANDWICH DAY!!!!! #gnosandwich"
    elif days_to_next_gnosandwich == 1:
        tweet_text = "No bread? No problem! TOMORROW IS INTERNATIONAL GNOSANDWICH DAY!!!!! #gnosandwich"
    else:
        tweet_text = "There are " + str(days_to_next_gnosandwich.days) + " days until International Gnosandwich Day. #gnosandwich"
    print(datetime.datetime.now(tz=pacific))
    print(tweet_text)
    api_gnosandwich.update_status(tweet_text)


update_sandwich_tweet()
update_gnosandwich_tweet()





