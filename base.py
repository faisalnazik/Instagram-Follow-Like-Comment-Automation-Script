import os
from time import sleep

from instapy import InstaPy #third party

import environ #import environ

env = environ.Env() # Initialise environment variables
environ.Env.read_env()

username = env('MYUSERNAME')  
password = env('PASSWORD')


#If headless_browser=True This feature allows you to run your bot without the GUI of the browser 
session = InstaPy(username=username, password=password, headless_browser=False)
session.login()
session.like_by_tags(["nature", "politics"], amount=5) #5 means 5 likes 
# session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"]) 

#The bot will keep commenting until it reaches its hourly and daily limits. 
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21) 

#With this, your bot won’t interact with posts by users who have more than 1000 followers.
session.set_relationship_bounds(enabled=True, max_followers=1000)
session.end()