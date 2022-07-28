# Author: Raul Varandela
# Date: 20/07/22
# Description: File that use Mastodon API to post.


import DB_connect
from mastodon import Mastodon


# toot something on mastodon
def toot():
    mastodon = Mastodon(
        access_token='ULSvKPbAVCbMbI7ECqnMGZWZBimOChwSOrSFdL3I9oY',
        api_base_url='https://mstdn.social/'
    )
    mastodon.toot(DB_connect.getFilosofyPhase())