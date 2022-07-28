# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use instagram API to post.

from instagrapi import Client
import random
import os

def publish_photo():
    cl = Client()
    # instagram account nº 1
    cl.login('rogeregonzales1', 'L6poFDhOS8eBECc9sW5L')

    # choose a random image from the folder
    path = r"C:\\Users\\Raul\\Pictures\\TFM\\Insta"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    # upload a photo to the feed
    cl.photo_upload(f'C:\\Users\\Raul\\Pictures\\TFM\\Insta\\' +
                    random_filename, caption='test2')


    # upload a photo to story
    cl.photo_upload_to_story(f'C:\\Users\\Raul\\Pictures\\TFM\\Insta\\' +
                            random_filename, caption='test2')