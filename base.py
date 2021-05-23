import os
from time import sleep

from instapy import InstaPy #third party

import environ #import environ

env = environ.Env() # Initialise environment variables
environ.Env.read_env()

username = env('MYUSERNAME')  
password = env('PASSWORD')

#If headless_browser=True This feature allows you to run your bot without the GUI of the browser
session = InstaPy(username=username, password=password, headless_browser=True)
session.login()

session.end()