from datetime import datetime
from twitter import *
from apscheduler.schedulers.blocking import BlockingScheduler

# Set the values for following variables from your Twitter Account
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# This function will tweet on Twitter
def publish_Status_On_Twitter(Twitter_Status):
    TW = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET))
    TW.statuses.update(status=Twitter_Status)

def tweet_if_internet():
    try:
        publish_Status_On_Twitter("Internet Service is up: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    except:
        pass

# Tweet on script startup
publish_Status_On_Twitter("Internet Service is up: " + datetime.now().strftime("%Y-%m-%d %H:%M"))

scheduler = BlockingScheduler()

# Schedule tweet every 30 minutes
scheduler.add_job(tweet_if_internet, 'interval', hours=0.5)
scheduler.start()
