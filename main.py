# Author: Raul Varandela
# Date: 22/07/22
# Description: Main file for the project.

import twitter 
import mastodon_app 
import instagram
import time
import schedule
import random

randomNuber = random.randint(5,120)

schedule.every(randomNuber).minutes.do(twitter.tweet)
schedule.every(randomNuber).minutes.do(mastodon_app.toot)
schedule.every(1).days.do(instagram.publishPhoto)
schedule.every(2).days.do(instagram.publishStory)
schedule.every(2).hours.do(instagram.replyUsers)

while True:
    schedule.run_pending()
    time.sleep(1)

