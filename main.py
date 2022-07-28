# Author: Raul Varandela
# Date: 22/07/22
# Description: Main file for the project.

from twitter import tweet
from mastodon_app import toot
from instagram import publish_photo
import time
import schedule

schedule.every(20).minutes.do(tweet)
schedule.every(20).minutes.do(toot)
schedule.every(1).hour.do(publish_photo)

while True:
    schedule.run_pending()
    time.sleep(1)

