
from app.yelp_data import yelpAPIfunction

import os
from dotenv import load_dotenv
import pandas as pd

def test_yelp_API():

    YELP_API_KEY = os.getenv("YELP_API_KEY")
    filename, df1, df2 = yelpAPIfunction(YELP_API_KEY, "Coffee", "Santa Monica")

    assert filename == "Yelp Data, Santa Monica, Coffee.xlsx"
    assert len(df1) == 50
    assert "zip_cod" in df1.columns
    assert "Categories" in df2.columns

    
