# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use instagram API to post.

from instagrapi import Client

cl = Client()
#instagram account nº 1
#cl.login('antonym4166', 'L6poFDhOS8eBECc9sW5L')
#instagram account nº 2
cl.login('armentariofigueroacorona', 'UPW40NG3GUY10Zyk7UeL')

#upload a photo to the feed
cl.photo_upload('C:\\Users\\Raul\\Pictures\\Saved Pictures\\skylinemadrid.jpg',caption='test2')


#upload a photo to story
cl.photo_upload_to_story('C:\\Users\\Raul\\Pictures\\Saved Pictures\\skylinemadrid.jpg',caption='test2')

#the second user follow the first user
cl.user_follow(cl.user_id_from_username('antonym4166'))

print("Done!")