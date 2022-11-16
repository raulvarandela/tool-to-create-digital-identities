# Author: Raul Varandela
# Date: 20/07/22
# Description: file that use Twitter API to tweet.

import random
import tweepy
from DB_connect import getDesciption, getSimpleReply, getReply, getSkaterPhase, getPhase, getSetPhase, getFilosofyPhase, getLastDate, addDate
from Unsplash_module import getPhoto, deletePhoto
from datetime import datetime


# main function
def main(fuction):
    if fuction == "publishText":
        publishText()
    elif fuction == "publishPhoto":
        publishPhoto()
    elif fuction == "boost":
        boost()
    elif fuction == "replyComments":
        replyComments()
    elif fuction == "publishComment":
        publishComment()
    elif fuction == "like":
        like()
    elif fuction == "followUsers":
        followUsers()
    elif fuction == "followBack":
        followBack()
    else:
        print('Error: invalid function')


# conect to twitter API
def login():
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'

    key = 'key'
    secret = 'secret'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    return tweepy.API(auth, wait_on_rate_limit=True)


# tweet a phrase
def publishText():
    api = login()
    api.update_status(chooseFuctionTwitter())


# choosea ramdom function to use
def chooseFuctionTwitter():
    ramdomNumber = random.randint(1, 4)
    if ramdomNumber == 1:
        return getSkaterPhase()
    elif ramdomNumber == 2:
        return getPhase()
    elif ramdomNumber == 3:
        return getSetPhase()
    elif ramdomNumber == 4:
        return getFilosofyPhase()
    else:
        print("Error")


# tweet a photo
def publishPhoto():
    api = login()
    photo = getPhoto("twitter")
    media = api.media_upload(photo)
    tweet = f"{getDesciption()}\n\n\n\n#skate #skateboarding #skater #sk8 #SkateAndDestroy #skatevibes #skatelifestyle "
    api.update_status(status=tweet, media_ids=[media.media_id])
    deletePhoto(photo)


# retweet a tweet
def boost():
    api = login()
    try:
        api.retweet(searchTweet().id)
    except tweepy.errors.Forbidden as e:
        print("Error: ", e)


# reply to comments
def replyComments():
    api = login()
    mentions = getMentions()
    tweets = api.user_timeline()
    for tweet in tweets:
        for mention in mentions:
            if tweet.id == mention.in_reply_to_status_id and compareDate(tweet):
                api.update_status(status=f"@{mention.user.screen_name} {getReply()}", in_reply_to_status_id=mention.id)
    addDate(str(datetime.utcnow())[:-3],'twitter')


#formart twitter's date
def formatTwitterDate(date):
    date = date.replace('+',' ').replace(':',' ').replace('-',' ').split(' ')
    if date[1] == "Jan":
        date[1] = "01"
    elif date[1] == "Feb":
        date[1] = "02"
    elif date[1] == "Mar":
        date[1] = "03" 
    elif date[1] == "Apr":
        date[1] = "04"
    elif date[1] == "May":
        date[1] = "05"
    elif date[1] == "Jun":
        date[1] = "06"
    elif date[1] == "Jul":
        date[1] = "07"
    elif date[1] == "Aug":
        date[1] = "08"
    elif date[1] == "Sep":
        date[1] = "09"
    elif date[1] == "Oct":
        date[1] = "10"
    elif date[1] == "Nov":
        date[1] = "11"
    elif date[1] == "Dec":
        date[1] = "12"
    return datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5]))


#compare the date of the tweet with the current date
def compareDate(tweet):
    date = formatTwitterDate(str(tweet.created_at))
    now = formatDate(getLastDate('twitter'))
    if date > now:
        return True
    else:
        return False


# format dates
def formatDate(date):
    date = date.replace('-', ' ').replace(':', ' ').replace('.', ' ').split(' ')
    return datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5]))


# get mentions                
def getMentions():
    api = login()
    tweets = api.mentions_timeline()
    replies = []
    for tweet in tweets:
        replies.append(api.get_status(tweet.id, tweet_mode="extended"))
    return replies


# reply a tweet
def publishComment():
    api = login()
    condiction = True
    while condiction:
        tweet = searchTweet()
        if not isRetweet(tweet):
            api.update_status(status=f"@{tweet.user.screen_name} {getSimpleReply()}", in_reply_to_status_id=tweet.id)
            condiction = False


# check if the tweet is a retweet
def isRetweet(tweet):
    if hasattr(tweet, 'retweeted_status'):
        return True
    else:
        return False


# set favorite a tweet
def like():
    api = login()
    try:
        api.create_favorite(searchTweet().id)
    except tweepy.errors.Forbidden as e:
        print("Error: ", e)


# search a tweet
def searchTweet():
    api = login()
    topic = ['skateboarding', 'Green Day', 'Blink-182', 'X-games']
    randomNumber = random.randint(0, len(topic)-1)
    tweets = api.search_tweets(q=topic[randomNumber], lang="en")
    randomNum = random.randint(0, len(tweets)-1)
    return tweets[randomNum]

# follow some users
def followUsers():
    api = login()
    for user in getUsersToFollow():
        api.create_friendship(screen_name=user.screen_name)


# get a array of users to follow
def getUsersToFollow():
    api = login()
    usernames = ['BarackObama','justinbieber','katyperry','rihanna','elonmusk','Cristiano','taylorswift13','ladygaga','KimKardashian','narendramodi','TheEllenShow','YouTube']
    randomNumber = random.randint(0, len(usernames)-1)
    return api.get_followers(screen_name=usernames[randomNumber])


#follow back users
def followBack():
    api = login()
    followers = api.get_followers()
    following = api.get_friends()
    for follower in followers:
        if follower not in following:
            api.create_friendship(screen_name=follower.screen_name)
