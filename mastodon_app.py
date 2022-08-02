# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use Mastodon API to post.


from DB_connect import chooseFuctionMastodon, getPhoto
from mastodon import Mastodon


# connect to mastodon API
def login():
    return Mastodon(
        access_token='ULSvKPbAVCbMbI7ECqnMGZWZBimOChwSOrSFdL3I9oY',
        api_base_url='https://mstdn.social/'
    )


# toot something on mastodon
def toot():
    mastodon = login()
    mastodon.toot(chooseFuctionMastodon())


# toot a photo on mastodon
def tootPhoto():
    mastodon = login()
    media = mastodon.media_post(getPhoto())
    toot = '#skateboard #skateboardingisawesomeasfuck #skatevibes #skateboardd #skateparklife #skatebordinglife #skatelifestyle #skateboardwithfriends #skateboardingisfun #skatesyle #skatergirl #skatebaordingsavedmylife #skaterboy #skatebaordheart #skateboardingismylife #skateboardtable #skating #skateboy #skateboardingisawesome #skatepark #skategirls #skateboardingisforever #skateboardlife #skater #skateboards #skatelife #style #skate #skateboardingisnotacrime'
    mastodon.status_post(toot, media_ids=media)