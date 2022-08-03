# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use Mastodon API to post.


import random
from DB_connect import chooseFuctionMastodon, getPhoto, getDesciption
from mastodon import Mastodon
import requests


access_token = 'ULSvKPbAVCbMbI7ECqnMGZWZBimOChwSOrSFdL3I9oY'
api_base_url = 'https://mstdn.social/'

# connect to mastodon API


def login():
    return Mastodon(
        access_token = access_token,
        api_base_url = api_base_url
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
    temp = requests.get(
        'https://mstdn.social/api/v1/directory?limit=40&order=new').json()
    for i in temp:
        usersIDs.append(temp.pop().get('id'))
    return usersIDs


# follow users from Mastodon's directory
def followUsers():
    mastodon = login()
    for i in getUsers():
        mastodon.account_follow(i)


# gets toots from Mastodon's timeline
def getTootsFromPublicTimeline():
    tootsIDs = []
    temp = requests.get('https://mstdn.social/api/v1/timelines/public').json()
    for i in temp:
        tootsIDs.append(temp.pop().get('id'))
    return tootsIDs


# get toots from my timeline
def getTootsFromHomeTimeline():
    tootsIDs = []
    temp = requests.get(f'https://mstdn.social/api/v1/timelines/home?access_token=' + access_token).json()
    for i in temp:
        tootsIDs.append(temp.pop().get('id'))
    return tootsIDs


# retoots a toot from Mastodon's timeline
def retootFromPublicTimeline():
    mastodon = login()
    toots = getTootsFromPublicTimeline()
    randomNuber = random.randint(0, len(toots))
    mastodon.status_reblog(toots[randomNuber])


# retoots a toot from my timeline
def retootFromHomeTimeline():
    mastodon = login()
    toots = getTootsFromHomeTimeline()
    randomNuber = random.randint(0, len(toots))
    mastodon.status_reblog(toots[randomNuber])


# set as favorite a toot from my timeline
def favoriteFromHomeTimeline():
    mastodon = login()
    toots = getTootsFromHomeTimeline()
    randomNuber = random.randint(0, len(toots))
    mastodon.status_favourite(toots[randomNuber])


#set as favorite a toot from Mastodon's timeline
def favoriteFromPublicTimeline():
    mastodon = login()
    toots = getTootsFromPublicTimeline()
    randomNuber = random.randint(0, len(toots))
    mastodon.status_favourite(toots[randomNuber])