# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use instagram API to post.

from instagrapi import Client
from DB_connect import getPhoto

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
    