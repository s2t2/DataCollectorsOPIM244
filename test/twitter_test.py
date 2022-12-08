
from app.twitter_data import twitterAPIfunction

import os
from dotenv import load_dotenv
import pandas as pd

def test_yelp_API():

    
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")

    filename, tweets = twitterAPIfunction(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_API_KEY, 
                                TWITTER_API_KEY_SECRET, "account", "POTUS")

    assert filename == "web_app/POTUS Twitter Data.xlsx"
    assert len(tweets) >= 400


    
