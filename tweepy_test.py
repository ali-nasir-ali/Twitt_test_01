import tweepy   # pip install tweepy
import os
from dotenv import load_dotenv  # pip install python-dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# api.update_status(status="Hello World.")
user = api.get_user('Lenniesaurus')
print(user.screen_name)
#print(user.friends(*, user_id, screen_name, cursor, count, skip_status, include_user_entities))
"""
user = api.get_user('NasirTheRoman')
print(user.screen_name)
print(user.followers_count)
"""