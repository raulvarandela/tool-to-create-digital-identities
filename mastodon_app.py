# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use Mastodon API to post.


import json
from DB_connect import chooseFuctionMastodon, getPhoto, getDesciption
from mastodon import Mastodon
import requests


# connect to mastodon API
def login():
    return Mastodon(
        access_token='ULSvKPbAVCbMbI7ECqnMGZWZBimOChwSOrSFdL3I9oY',
        api_base_url='https://mstdn.social/'
    )


# toot something on mastodon
def toot():
    mastodon = login()
    mastodon.toot(chooseFuctionMastodon())


# toot a photo on mastodon
def tootPhoto():
    mastodon = login()
    media = mastodon.media_post(getPhoto())
    mastodon.status_post(
        f"" + getDesciption() + "\n\n\n\n#skate #skateboarding #skater #sk8 #SkateAndDestroy #skatevibes #skatelifestyle ", media_ids=media)


# get users from Mastodon's diorectory
def getUsers():
    usersIDs = []
    temp = requests.get('https://mstdn.social/api/v1/directory?limit=40&order=new').json()
    for i in temp:
        usersIDs.append(temp.pop().get('id'))
    return usersIDs


# follow users from Mastodon's directory
def followUsers():
    mastodon = login()
    for i in getUsers():
            mastodon.account_follow(i)