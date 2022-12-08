
from app.NYT_data import NYTAPIfunction

import os
from dotenv import load_dotenv
import pandas as pd

def test_NYT_API():

    NYT_API_KEY = os.getenv("NYT_API_KEY")
    filename, df1, df2, df3, df4 = NYTAPIfunction(NYT_API_KEY, "Climate Change", "1 Year")

    assert filename == "Climate Change.xlsx"
    assert "Main Headline" in df1.columns
    assert "Abstract Words" in df2.columns
    assert "Main Headline Words" in df3.columns
    assert "Article Keywords" in df4.columns
    assert "test!" in df4.columns

    assert len(df1) >= 100
