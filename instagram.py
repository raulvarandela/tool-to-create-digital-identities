# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use instagram API to post.

from turtle import delay
from instagrapi import Client
from DB_connect import getPhoto, getReply
import numpy as np

def login():
    cl = Client()
    # instagram account nº 1
    cl.login('rogeregonzales1', 'L6poFDhOS8eBECc9sW5L')
    return cl

# upload a photo to the feed
def publishPhoto():
    cl = login()
    cl.photo_upload(getPhoto(), caption='#skateboard #skateboardingisawesomeasfuck #skatevibes #skateboardd #skateparklife #skatebordinglife #skatelifestyle #skateboardwithfriends #skateboardingisfun #skatesyle #skatergirl #skatebaordingsavedmylife #skaterboy #skatebaordheart #skateboardingismylife #skateboardtable #skating #skateboy #skateboardingisawesome #skatepark #skategirls #skateboardingisforever #skateboardlife #skater #skateboards #skatelife #style #skate #skateboardingisnotacrime')


# upload a photo to story  
def publishStory():
    cl = login()
    cl.photo_upload_to_story(getPhoto(), caption='photo')
    
# reply to a user that commented on your photo
def replyUsers():
    cl = login()
    userID = cl.user_id_from_username('rogeregonzales1') # meter esto como global
    mediaIDs = cl.user_medias(userID, 3) # consigo las tres últimas publicaciones de mi usuario
    for mediaID in mediaIDs:
        print(mediaID.id)
        if mediaID.comment_count != 0:
            for coment in getComments(cl, str(mediaID)):
                    print(coment.pk)
                    cl.media_comment(mediaID.id, getReply(), coment.pk)
        


def getComments(cl ,mediaID):
    print("aaaa")
    a = cl.media_comments(mediaID, 0)
    print("bbbb")
    return a

def prueba():
    cl = login()
    userID = cl.user_id_from_username('rogeregonzales1')
    mediaIDs = cl.user_medias(userID, 3)

    
    for coment in getComments(cl,'2894619286271353249_54294180895'):
                    cl.media_comment('2894619286271353249_54294180895', getReply(), coment.pk)
