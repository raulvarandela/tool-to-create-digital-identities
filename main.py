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
schedule.every(3).days.do(mastodon_app.tootPhoto)
schedule.every(7).days.do(mastodon_app.followUsers)
schedule.every(1).hour.do(mastodon_app.followBack)
schedule.every(2).hours.do(mastodon_app.retoot)
schedule.every(2).hours.do(mastodon_app.favorite)
schedule.every(10).minutes.do(mastodon_app.replyToComments)
schedule.every(4).hours.do(mastodon_app.replyToToot)

#Instagram schedule
schedule.every(1).days.do(instagram.publishPhoto)
schedule.every(2).days.do(instagram.publishStory)
schedule.every(2).hours.do(instagram.replyUsers)
schedule.every(3).days.do(instagram.followUsers)
schedule.every(3).hours.do(instagram.likePhoto)
schedule.every(1).hour.do(instagram.followBack)
schedule.every(4).hours.do(instagram.commentPhoto)

#Twitter schedule
schedule.every(randomNuber).minutes.do(twitter.tweet)
schedule.every(7).days.do(twitter.tweetPhoto)
schedule.every(5).days.do(twitter.followUsers)
schedule.every(1).hours.do(twitter.replyComments)
schedule.every(5).hours.do(twitter.retweet)
schedule.every(2).hours.do(twitter.setFavorite)
schedule.every(1).day.do(twitter.replyTweet)
schedule.every(1).hour.do(twitter.followBack)

while True:
    schedule.run_pending()
    time.sleep(1)
