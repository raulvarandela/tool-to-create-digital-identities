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

#mastodon schedule
schedule.every(randomNuber).minutes.do(mastodon_app.toot)
schedule.every(2).week.do(mastodon_app.tootPhoto)
schedule.every(1).week.do(mastodon_app.followUsers)
schedule.every(1).day.do(mastodon_app.retootFromHomeTimeline)
schedule.every(1).day.do(mastodon_app.retootFromPublicTimeline)
schedule.every(1).day.do(mastodon_app.favoriteFromHomeTimeline)
schedule.every(1).day.do(mastodon_app.favoriteFromPublicTimeline)
schedule.every(10).minutes.do(mastodon_app.replyToComments)

#Instagram schedule
schedule.every(1).days.do(instagram.publishPhoto)
schedule.every(2).days.do(instagram.publishStory)
schedule.every(2).hours.do(instagram.replyUsers)

#Twitter schedule
schedule.every(randomNuber).minutes.do(twitter.tweet)
schedule.every(1).week.do(twitter.tweetPhoto)

while True:
    schedule.run_pending()
    time.sleep(1)

