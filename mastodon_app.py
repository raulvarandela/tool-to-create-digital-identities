# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use Mastodon API to post.


from os import access
import random
from DB_connect import getFilosofyPhase, getPhase, getPhoto, getDesciption, getReply, getSetPhase, getSimpleReply
from mastodon import Mastodon
import requests


access_token = 'ULSvKPbAVCbMbI7ECqnMGZWZBimOChwSOrSFdL3I9oY'
api_base_url = 'https://mstdn.social/'


# connect to mastodon API and login
def login():
    return Mastodon(
        access_token = access_token,
        api_base_url = api_base_url
    )


# toot something on mastodon
def toot():
    mastodon = login()
    mastodon.toot(chooseFuctionMastodon())


# choosea ramdom function to use
def chooseFuctionMastodon():
    ramdomNumber = random.randint(1, 3)
    if ramdomNumber == 1:
        return getFilosofyPhase()
    elif ramdomNumber == 2:
        return getPhase()
    elif ramdomNumber == 3:
        return getSetPhase()
    else:
        print("Error")


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


# choose a function to favorite
def retoot():
    ramdomNumber = random.randint(1, 2)
    if ramdomNumber == 1:
        retootFromPublicTimeline()
    else:
        retootFromHomeTimeline()


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


# choose a function to favorite
def favorite():
    ramdomNumber = random.randint(1, 2)
    if ramdomNumber == 1:
        favoriteFromHomeTimeline()
    else:
        favoriteFromPublicTimeline()


# set as favorite a toot from my timeline
def favoriteFromHomeTimeline():
    mastodon = login()
    toots = getTootsFromHomeTimeline()
    randomNuber = random.randint(0, len(toots)-1)
    mastodon.status_favourite(toots[randomNuber])


#set as favorite a toot from Mastodon's timeline
def favoriteFromPublicTimeline():
    mastodon = login()
    toots = getTootsFromPublicTimeline()
    randomNuber = random.randint(0, len(toots)-1)
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


# reply to a comment
def replyToComments():
    mastodon = login()
    userID = me().get('id')
    toots = getTootsFromUser(userID)
    for toot in toots:
        if toot.get('replies_count') != 0:
            replies = getTootsReplys(toot.get('id'))
            for reply in replies.values():
                for i in reply:
                    if i['in_reply_to_id'] == toot.get('id'):
                        mastodon.status_post(f"@{i['account']['acct']} {getReply()}",i['id'])


# choose a function to reply
def replyToToot():
    ramdomNumber = random.randint(1, 2)
    if ramdomNumber == 1:
        replyToPublicToot()
    else:
        replyToTimelineToot()


# reply to a ramdom toot in the public timeline
def replyToPublicToot():
    mastodon = login()
    toots = mastodon.timeline_public()
    randomNuber = random.randint(0, len(toots)-1)
    mastodon.status_post(f"@{toots[randomNuber]['account']['acct']} {getSimpleReply()}",toots[randomNuber]['id'])


# reply to a ramdom toot in the my timeline
def replyToTimelineToot():
    mastodon = login()
    toots = mastodon.timeline_home()
    randomNuber = random.randint(0, len(toots)-1)
    mastodon.status_post(f"@{toots[randomNuber]['account']['acct']} {getSimpleReply()}",toots[randomNuber]['id'])


#follow back users
def followBack():
    mastodon = login()
    followers = mastodon.account_followers(me().get('id'))
    following = mastodon.account_following(me().get('id'))
    for follower in followers:
        if follower not in following:
            mastodon.account_follow(follower.get('id'))
