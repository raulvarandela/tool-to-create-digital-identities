# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use Mastodon API to post.


import random
from DB_connect import chooseFuctionMastodon, getPhoto, getDesciption, getReply
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
        f"{getDesciption()}\n\n\n\n#skate #skateboarding #skater #sk8 #SkateAndDestroy #skatevibes #skatelifestyle ", media_ids=media)


# get users from Mastodon's diorectory
def getUsers():
    usersIDs = []
    users = requests.get(
        'https://mstdn.social/api/v1/directory?limit=40&order=new').json()
    for user in users:
        usersIDs.append(user.get('id'))
    return usersIDs


# get suggested users
def suggestedUsers():
    mastodon = login()
    return mastodon.suggestions()


# follow users from Mastodon's directory
def followUsers():
    mastodon = login()
    for i in getUsers():
        mastodon.account_follow(i)


# gets toots from Mastodon's timeline
def getTootsFromPublicTimeline():
    tootsIDs = []
    toots = requests.get('https://mstdn.social/api/v1/timelines/public').json()
    for toot in toots:
        tootsIDs.append(toot.get('id'))
    return tootsIDs


# get toots from my timeline
def getTootsFromHomeTimeline():
    tootsIDs = []
    toots = requests.get(f'https://mstdn.social/api/v1/timelines/home?access_token=' + access_token).json()
    for toot in toots:
        tootsIDs.append(toot.get('id'))
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
    try:
        mastodon.status_reblog(toots[randomNuber])
    except:
        print("Error: no hay ningún toot para retootear")


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


# return info about my account
def me():
    mastodon = login()
    return mastodon.account_verify_credentials()


# get toots from a user
def getTootsFromUser(userID):
    return requests.get(f'https://mstdn.social/api/v1/accounts/{userID}/statuses?limit=40').json()


# get replies from a toot
def getTootsReplys(tootID):
    return requests.get(f'https://mstdn.social/api/v1/statuses/{tootID}/context').json()


# reply to a toot
def replyToToots():
    mastodon = login()
    userID = me().get('id')
    toots = getTootsFromUser(userID)
    for toot in toots:
        if toot.get('replies_count') != 0:
            replies = getTootsReplys(toot.get('id'))
            for reply in replies.values():
                for i in reply:
                    if i['in_reply_to_id'] == toot.get('id'):
                        mastodon.status_post(f"@{i['account']['username']} {getReply()}",i['id'])
