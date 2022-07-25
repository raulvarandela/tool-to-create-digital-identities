# Author: Raul Varandela
# Date: 22/07/22
# Description: Main file for the project.

from twitter import tweet
import time
import schedule

schedule.every(20).minutes.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)

