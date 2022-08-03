# Author: Raul Varandela
# Date: 20/07/22
# Description: file that use Twitter API to tweet.

import tweepy
from DB_connect import chooseFuctionTwitter, getPhoto, getDesciption


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


# tweet a photo
def tweetPhoto():
    api = login()
    media = api.media_upload(getPhoto())
    tweet = f"{getDesciption()}\n\n\n\n#skate #skateboarding #skater #sk8 #SkateAndDestroy #skatevibes #skatelifestyle "
    api.update_status(status=tweet, media_ids=[media.media_id])
