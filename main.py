# Author: Raul Varandela
# Date: 22/07/22
# Description: Main file for the project.

import twitter 
import mastodon_app 
import instagram
import time
import schedule

schedule.every(20).minutes.do(twitter.tweet)
schedule.every(20).minutes.do(mastodon_app.toot)
schedule.every(1).day.do(instagram.publishPhoto)
schedule.every(2).day.do(instagram.publishStory)

while True:
    schedule.run_pending()
    time.sleep(1)

