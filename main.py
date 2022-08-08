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
schedule.every(1).hour.do(mastodon_app.followBack)
schedule.every(10).day.do(mastodon_app.retoot)
schedule.every(20).day.do(mastodon_app.favorite)
schedule.every(10).minutes.do(mastodon_app.replyToComments)
schedule.every(4).hours.do(mastodon_app.replyToToot)

#Instagram schedule
schedule.every(1).days.do(instagram.publishPhoto)
schedule.every(2).days.do(instagram.publishStory)
schedule.every(2).hours.do(instagram.replyUsers)
schedule.every(2).week.do(instagram.followUsers)

#Twitter schedule
schedule.every(randomNuber).minutes.do(twitter.tweet)
schedule.every(1).week.do(twitter.tweetPhoto)
schedule.every(5).week.do(twitter.followUsers)
schedule.every(1).hours.do(twitter.replyComments)
schedule.every(10).day.do(twitter.retweet)
schedule.every(20).day.do(twitter.setFavorite)
schedule.every(1).day.do(twitter.replyComments)

while True:
    schedule.run_pending()
    time.sleep(1)

