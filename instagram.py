# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use instagram API to post.

from instagrapi import Client
import random
from DB_connect import getPhoto, getReply, getDesciption

# RogerEGonzales1's user and passwd
username = 'RogerEGonzales1'
passwd = 'Sqt3cL9tZhV1nSiXr7Ea'

# Armentario's user and passwd
#username = 'armentariofigueroacorona'
#passwd = 'UPW40NG3GUY10Zyk7UeL'

def login():
    cl = Client()
    cl.login(username, passwd)
    return cl


# upload a photo to the feed
def publishPhoto():
    cl = login()
    cl.photo_upload(getPhoto(), caption= f"{getDesciption()}.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#skateboard #skateboardingisawesomeasfuck #skatevibes #skateboardd #skateparklife #skatebordinglife #skatelifestyle #skateboardwithfriends #skateboardingisfun #skatesyle #skatergirl #skatebaordingsavedmylife #skaterboy #skatebaordheart #skateboardingismylife #skateboardtable #skating #skateboy #skateboardingisawesome #skatepark #skategirls #skateboardingisforever #skateboardlife #skater #skateboards #skatelife #style #skate #skateboardingisnotacrime")


# upload a photo to story
def publishStory():
    cl = login()
    cl.photo_upload_to_story(getPhoto(), caption='photo')


# reply to a user that commented on your photo
def replyUsers():
    cl = login()
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
    users = ['cristiano','kyliejenner','leomessi','arianagrande','selenagomez','therock','kimkardashian','beyonce','justinbieber','kendalljenner']
    randomNumber = random.randint(0, len(users)-1)
    userID = cl.user_id_from_username(users[randomNumber])
    return list(cl.user_followers(userID,amount=20).keys())


# follow some users
def followUsers():
    cl = login()
    usersIDs = getUsersToFollow(cl)
    for user in usersIDs:
        cl.user_follow(int(user))


# like a photo
def likePhoto():
    cl = login()
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