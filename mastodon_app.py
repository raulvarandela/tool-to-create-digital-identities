# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use Mastodon API to post.

# import libraries
from datetime import datetime
import random
from urllib import request
from DB_connect import getFilosofyPhase, getPhase, getDesciption, getReply, getSetPhase, getSimpleReply, getLastDate, addDate, addUser
from mastodon import Mastodon
import requests
from Unsplash_module import getPhoto, deletePhoto
from datetime import datetime
from bs4 import BeautifulSoup
import string


access_token = 'kN9d8jvJ6VTfc0lBn5d8kXguuHSnyG8rLbTX0mEapYo'
api_base_url = 'https://mstdn.social/'


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



# connect to mastodon API and login
def login():
    return Mastodon(
        access_token = access_token,
        api_base_url = api_base_url
    )


# toot something on mastodon
def publishText():
    mastodon = login()
    mastodon.toot(chooseFuctionMastodon())


# choose a ramdom function to use
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
def publishPhoto():
    mastodon = login()
    photo = getPhoto("mastodon")
    media = mastodon.media_post(photo)
    try:
        mastodon.status_post(
        f"{getDesciption()}\n\n\n\n#skate #skateboarding #skater #sk8 #SkateAndDestroy #skatevibes #skatelifestyle ", media_ids=media)
    except mastodon.Mastodon.MastodonAPIError as e:
        print(e)
    finally:
        deletePhoto(photo)


# choose a function to favorite
def boost():
    mastodon = login()
    toots = searchToots().statuses
    randomNuber = random.randint(0, len(toots)-1)
    condiction = True
    while condiction:
        if toots[randomNuber].account.username != 'RogerEGonzales1':
            mastodon.status_reblog(toots[randomNuber].id)
            condiction = False
        else:
            randomNuber = random.randint(0, len(toots)-1)

# reply to a comment
def replyComments():
    mastodon = login()
    userID = me().get('id')
    toots = getTootsFromUser(userID)
    date = getLastDate('mastodon')
    for toot in toots:
        if toot.get('replies_count') != 0 and toot.get('in_reply_to_id') is None and compareDates(date, toot.get('created_at')):
            replies = getTootsReplys(toot.get('id'))
            for reply in replies.values():
                for i in reply:
                    if i['in_reply_to_id'] == toot.get('id'):
                        mastodon.status_post(f"@{i['account']['acct']} {getReply()}",i['id'])
    addDate(str(datetime.utcnow())[:-3],'mastodon')


# format mastodon's date
def formatMastodonDate(date):
    return date.replace('T', ' ').replace('Z', '')


# format dates
def formatDate(date):
    date = date.replace('-', ' ').replace(':', ' ').replace('.', ' ').split(' ')
    return datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5]))

   
# compare two dates
def compareDates(date1, date2):
    if formatDate(date1) < formatDate(formatMastodonDate(date2)):
        return True
    else:
        return False


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


# publish a comment
def publishComment():
    mastodon = login()
    toots = searchToots().statuses
    randomNuber = random.randint(0, len(toots)-1)
    if toots[randomNuber].account.username != 'RogerEGonzales1':
        mastodon.status_post(f"@{toots[randomNuber].account.username} {getSimpleReply()}",toots[randomNuber].id)


# set as favorite a toot
def like():
    mastodon = login()
    toots = searchToots().statuses
    randomNuber = random.randint(0, len(toots)-1)
    if toots[randomNuber].account.username != 'RogerEGonzales1':
        mastodon.status_favourite(toots[randomNuber].id)

    
# search toots
def searchToots():
    mastodon = login()
    return mastodon.search_v2('skate')

# follow users from Mastodon's directory
def followUsers():
    mastodon = login()
    for i in getUsers():
        mastodon.account_follow(i)

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


#follow back users
def followBack():
    mastodon = login()
    followers = mastodon.account_followers(me().get('id'))
    following = mastodon.account_following(me().get('id'))
    for follower in followers:
        if follower not in following:
            mastodon.account_follow(follower.get('id'))


# create a new account
def createAccount():
    access_token = '3uOnpf7O274Qd56uhRcJKOb0fWaD4tJdwz6ZGLi2gbQ'
    api_base_url = 'https://norden.social/'
    username = username_gen()
    password = password_gen()
    email = getFakeMail(username,password)
    account = requests.post(f'{api_base_url}api/v1/accounts?access_token={access_token}&username={username}&password={password}&email={str(email["address"])}&agreement=true&locale=en').json()
    addUser(username,email['address'],password)
    print(account)


# generate a random username
def username_gen(length=24, chars= string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))  


# generate a random password  
def password_gen(length=16, chars= string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length)) 


# get fake email
def getFakeMail(username, password):
    domain = 'bukhariansiddur.com'
    url = "https://api.mail.gw/accounts"
    payload = { "address": f"{username}@{domain}", "password": password }
    headers = { 'Content-Type': 'application/json' }
    data = requests.post(url, headers=headers, json=payload).json()
    return data