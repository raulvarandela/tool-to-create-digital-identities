# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use instagram API to post.

from instagrapi import Client
import random
import json
from DB_connect import getReply, getDesciption, getSimpleReply
from Unsplash_module import getPhoto, deletePhoto

# RogerEGonzales1's user and passwd
#username = 'RogerEGonzales1'
#passwd = 'Sqt3cL9tZhV1nSiXr7Ea'

# Armentario's user and passwd
username = 'armentariofigueroacorona'
passwd = 'UPW40NG3GUY10Zyk7UeL'


def login():
    cl = Client()
    cl.login(username, passwd)
    return cl


def persistentLogin():
    cl = Client()
    cl.login(username, passwd)
    json.dump(
        cl.get_settings(),
        open(f'./cookies/{username}_cookie.json', 'w')
    )
    return cl

def loginWithCookie():
    cl = Client(json.load(open(f'./cookies/{username}_cookie.json')))
    return cl

# upload a photo to the feed
def publishPhoto(cl):
    photo = getPhoto('instagram')
    cl.photo_upload(photo, caption=f"{getDesciption()}.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#skateboard #skateboardingisawesomeasfuck #skatevibes #skateboardd #skateparklife #skatebordinglife #skatelifestyle #skateboardwithfriends #skateboardingisfun #skatesyle #skatergirl #skatebaordingsavedmylife #skaterboy #skatebaordheart #skateboardingismylife #skateboardtable #skating #skateboy #skateboardingisawesome #skatepark #skategirls #skateboardingisforever #skateboardlife #skater #skateboards #skatelife #style #skate #skateboardingisnotacrime")
    deletePhoto(photo)


# upload a photo to story
def publishStory(cl):
    photo = getPhoto('instagram')
    story = cl.photo_upload_to_story(photo, caption='photo')
    myUserID = cl.user_id_from_username(username)
    cl.highlight_add_stories(cl.user_highlights(myUserID)[0].pk, [story.id])
    deletePhoto(photo)


# reply to a user that commented on your photo
def replyUsers(cl):
    userID = cl.user_id_from_username(username)
    mediaIDs = cl.user_medias(userID, 3)
    for mediaID in mediaIDs:
        if mediaID.comment_count != 0:
            for coment in getComments(cl, mediaID.id):
                cl.media_comment(mediaID.id, getReply(), coment.pk)


# get the comments of a photo
def getComments(cl, mediaID):
    return cl.media_comments(mediaID, 0)


# get users to follow
def getUsersToFollow(cl):
    users = ['cristiano', 'kyliejenner', 'leomessi', 'arianagrande', 'selenagomez',
             'therock', 'kimkardashian', 'beyonce', 'justinbieber', 'kendalljenner']
    randomNumber = random.randint(0, len(users)-1)
    userID = cl.user_id_from_username(users[randomNumber])
    return list(cl.user_followers(userID, amount=20).keys())


# follow some users
def followUsers(cl):
    usersIDs = getUsersToFollow(cl)
    for user in usersIDs:
        cl.user_follow(int(user))


# like a photo
def likePhoto(cl):
    myUserID = cl.user_id_from_username(username)
    myFollowing = list(cl.user_following(myUserID, 20).keys())
    condiction = False
    while not condiction:
        ramdomNumber = random.randint(0, len(myFollowing)-1)
        media = cl.user_medias(myFollowing[ramdomNumber], 5)
        randomNumber = random.randint(0, 4)
        if len(media):
            condiction = True
            cl.media_like(media[randomNumber].pk)


# follow back users
def followBack(cl):
    myUserID = cl.user_id_from_username(username)
    myFollowers = list(cl.user_followers(myUserID, 20).keys())
    myFollowing = list(cl.user_following(myUserID, 20).keys())
    for user in myFollowers:
        if user not in myFollowing:
            cl.user_follow(int(user))


# comment a photo
def commentPhoto(cl):
    myUserID = cl.user_id_from_username(username)
    myFollowing = list(cl.user_following(myUserID, 20).keys())
    condiction = False
    while not condiction:
        ramdomNumber = random.randint(0, len(myFollowing)-1)
        media = cl.user_medias(myFollowing[ramdomNumber], 5)
        randomNumber = random.randint(0, 4)
        if len(media):
            condiction = True
            cl.media_comment(media[randomNumber].pk, getSimpleReply())
