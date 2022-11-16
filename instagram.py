# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use instagram API to post.

from instagrapi import Client
import random
import json
from DB_connect import getReply, getDesciption, getSimpleReply, getLastDate, addDate
from Unsplash_module import getPhoto, deletePhoto
from datetime import datetime
import os

#  user and passwd
username = 'username'
passwd = 'passwd'


# main function
def main(fuction):
    cl = loginWithCookie()
    if fuction == 'publishPhoto':
        publishPhoto(cl)
    elif fuction == 'publishStory':
        publishStory(cl)
    elif fuction == 'replyComments':
        replyComments(cl)
    elif fuction == 'publishComment':
        publishComment(cl)
    elif fuction == 'like':
        like(cl)
    elif fuction == 'followUsers':
        followUsers(cl)
    elif fuction == 'followBack':
        followBack(cl)
    else:
        print('Error: invalid function')


# login to instagram
def login():
    cl = Client()
    cl.login(username, passwd)
    return cl


# login to instagram and save the cookie
def persistentLogin():
    cl = Client()
    cl.login(username, passwd)
    cwd = os.getcwd()
    json.dump(
        cl.get_settings(),
        open(f'{cwd}/cookies/{username}_cookie.json', 'w')
    )
    return cl


# login to instagram with cookie
def loginWithCookie():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    cl = Client(json.load(open(f'{BASE_DIR}/cookies/{username}_cookie.json')))
    return cl


# upload a photo to the feed
def publishPhoto(cl):
    photo = getPhoto('instagram')
    cl.photo_upload(photo, caption=f"{getDesciption()}.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#skateboard #skateboardingisawesomeasfuck #skatevibes #skateboardd #skateparklife #skatebordinglife #skatelifestyle #skateboardwithfriends #skateboardingisfun #skatesyle #skatergirl #skatebaordingsavedmylife #skaterboy #skatebaordheart #skateboardingismylife #skateboardtable #skating #skateboy #skateboardingisawesome #skatepark #skategirls #skateboardingisforever #skateboardlife #skater #skateboards #skatelife #style #skate #skateboardingisnotacrime")
    deletePhoto(photo)


# upload a photo to story
def publishStory(cl):
    photo = getPhoto('instagram_story')
    story = cl.photo_upload_to_story(photo, caption='photo')
    myUserID = cl.user_id_from_username(username)
    cl.highlight_add_stories(cl.user_highlights(myUserID)[0].pk, [story.id])
    deletePhoto(photo)


# reply to a user that commented on your photo
def replyComments(cl):
    userID = cl.user_id_from_username(username)
    mediaIDs = cl.user_medias(userID, 3)
    for mediaID in mediaIDs:
        if mediaID.comment_count != 0 and compareDates(mediaID.taken_at, getLastDate('instagram')):
            for coment in getComments(cl, mediaID.id):
                cl.media_comment(mediaID.id, getReply(), coment.pk)
    addDate(str(datetime.utcnow())[:-3],'instagram')


#format date
def formatDate(date):
    date = date.replace('+',' ').replace(':',' ').replace('-',' ').replace('.',' ').split(' ')
    return datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5]))


#compare dates
def compareDates(date1, date2):
    if formatDate(str(date1)) > formatDate(str(date2)):
        return True
    else:
        return False


# comment a photo
def publishComment(cl):
    photos = searchHashtag(cl)
    randomNumber = random.randint(0, len(photos)-1)
    cl.media_comment(photos[randomNumber].pk, getSimpleReply())


# get the comments of a photo
def getComments(cl, mediaID):
    return cl.media_comments(mediaID, 0)


# like a photo
def like(cl):
    photos = searchHashtag(cl)
    randomNumber = random.randint(0, len(photos)-1)
    cl.media_like(photos[randomNumber].pk)


# search for photos with a hashtag
def searchHashtag(cl):
    tag = ['skate', 'skateboard', 'greenday', 'blink182']
    randomNumber = random.randint(0, len(tag)-1)
    return cl.hashtag_medias_top(tag[randomNumber] , 10)


# follow some users
def followUsers(cl):
    usersIDs = getUsersToFollow(cl)
    for user in usersIDs:
        cl.user_follow(int(user))


# get users to follow
def getUsersToFollow(cl):
    users = ['cristiano', 'kyliejenner', 'leomessi', 'arianagrande', 'selenagomez',
             'therock', 'kimkardashian', 'beyonce', 'justinbieber', 'kendalljenner']
    randomNumber = random.randint(0, len(users)-1)
    userID = cl.user_id_from_username(users[randomNumber])
    return list(cl.user_followers(userID, amount=20).keys())


# follow back users
def followBack(cl):
    myUserID = cl.user_id_from_username(username)
    myFollowers = list(cl.user_followers(myUserID, 20).keys())
    myFollowing = list(cl.user_following(myUserID, 20).keys())
    for user in myFollowers:
        if user not in myFollowing:
            cl.user_follow(int(user))

