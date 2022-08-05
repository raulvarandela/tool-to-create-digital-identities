# Author: Raul Varandela
# Date: 20/07/22
# Description: file that use Twitter API to tweet.

import random
import tweepy
from DB_connect import getPhoto, getDesciption, getSimpleReply, getReply, getSkaterPhase, getPhase, getSetPhase, getFilosofyPhase


# conect to twitter API
def login():
    consumer_key = 'CCZdCZAHh2ESerJW8C9g7mXXW'
    consumer_secret = 'hNWRr0RT4AKE2Ww8Xz3EQeYhZQN3UY8sTKmq7H42WrRHGi3S5y'

    key = '1546791696884813824-vk0GTOOwbgEYClFwEnCHGaMQF3Bjsf'
    secret = 'WCbbDUKqVQDjQR6RVH78f6FFwY6qGD9nfUv3I55KIydlM'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    return tweepy.API(auth, wait_on_rate_limit=True)



# tweet a phrase
def tweet():
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
def tweetPhoto():
    api = login()
    media = api.media_upload(getPhoto())
    tweet = f"{getDesciption()}\n\n\n\n#skate #skateboarding #skater #sk8 #SkateAndDestroy #skatevibes #skatelifestyle "
    api.update_status(status=tweet, media_ids=[media.media_id])


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


# retweet a tweet
def retweet():
    api = login()
    tweets = api.home_timeline()
    ramdinNumber = random.randint(0, len(tweets)-1)
    api.retweet(tweets[ramdinNumber].id)


# set favorite a tweet
def setFavorite():
    api = login()
    tweets = api.home_timeline()
    ramdinNumber = random.randint(0, len(tweets)-1)
    api.create_favorite(tweets[ramdinNumber].id)


# reply a tweet
def replyTweet():
    api = login()
    tweets = api.home_timeline()
    ramdinNumber = random.randint(0, len(tweets)-1)
    api.update_status(status=f"@{tweets[ramdinNumber].user.screen_name} {getSimpleReply()}", in_reply_to_status_id=tweets[ramdinNumber].id)


# reply to comments
def replyComments():
    api = login()
    mentions = getMentions()
    tweets = api.user_timeline()
    for tweet in tweets:
        for mention in mentions:
            if tweet.id == mention.in_reply_to_status_id:
                api.update_status(status=f"@{mention.user.screen_name} {getReply()}", in_reply_to_status_id=mention.id)


# get mentions                
def getMentions():
    api = login()
    tweets = api.mentions_timeline()
    replies = []
    for tweet in tweets:
        replies.append(api.get_status(tweet.id, tweet_mode="extended"))
    return replies

