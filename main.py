from twitter import tweet
import time
import schedule

schedule.every(10).minutes.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)

