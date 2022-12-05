
from pynytimes import NYTAPI
import pandas as pd
import openpyxl

import json
import datetime


def NYTAPIfunction(NYT_API_KEY_parameter, topic_parameter, date_range_parameter):

    def beginning_date(user_date_range_para):
        if user_date_range_para == "1 Week":
            date = datetime.date.today() - datetime.timedelta(days=7)
            return date
        elif user_date_range_para == "1 Month":
            date = datetime.date.today() - datetime.timedelta(days=31)
            return date
        elif user_date_range_para == "6 Months":
            date = datetime.date.today() - datetime.timedelta(days=183)
            return date
        elif user_date_range_para == "1 Year":
            date = datetime.date.today() - datetime.timedelta(days=365)
            return date

    def clean_words(words):
        new_words = ""
        for character in words:
            if character.isalnum() or character == " " or character == "#" or character == "'" or character == "-":
                new_words += character.lower()
        return new_words

    nyt = NYTAPI(NYT_API_KEY_parameter, parse_dates=True)

    beg_date = str(beginning_date(date_range_parameter))
    beg_year = int(beg_date.split("-")[0])
    beg_month = int(beg_date.split("-")[1])
    beg_day = int(beg_date.split("-")[2])

    current_date = str(datetime.date.today())
    end_year = int(current_date.split("-")[0])
    end_month = int(current_date.split("-")[1])
    end_day = int(current_date.split("-")[2])

    articles = nyt.article_search(
        query = topic_parameter,
        results = 100,
        dates = {
            "begin": datetime.datetime(beg_year, beg_month, beg_day),
            "end": datetime.datetime(end_year, end_month, end_day)
        },
        options = {
            "sort": "oldest",
            "sources": [
                "New York Times",
                "AP",
                "Reuters",
                "International Herald Tribune"
            ],
            "type_of_material": [
                "News"
            ]
        }
    )

    articles_JSON = json.dumps(articles, default=str)
    df = pd.read_json(articles_JSON)

    #Sheet 1 - Data
    df = df.reset_index()
    df["Main Headline"] = df["headline"].apply(lambda x: x["main"])
    df["Date"] = df["pub_date"].apply(lambda x: x[:10])
    df["Time"] = df["pub_date"].apply(lambda x: x[10:19])

    #Sheet 2 - Abstract Words
    df_sheet2 = df[["index","abstract"]]

    list_sheet2 = []
    for i in range(len(df_sheet2)):
        words_list = clean_words(df_sheet2["abstract"].loc[i]).split()
            
        for x in range(len(words_list)):
            index_word = [i, words_list[x]]
            list_sheet2.append(index_word)
            
    df_sheet2 = pd.DataFrame(list_sheet2)
    df_sheet2 = df_sheet2.rename(columns={0:"Article Id", 1:"Abstract Words"})

    #Sheet 3 - Headline Words
    df_sheet3 = df[["index","Main Headline"]]

    list_sheet3 = []
    for i in range(len(df_sheet3)):
        words_list = clean_words(df_sheet3["Main Headline"].loc[i]).split()
            
        for x in range(len(words_list)):
            index_word = [i, words_list[x]]
            list_sheet3.append(index_word)
            
    df_sheet3 = pd.DataFrame(list_sheet3)
    df_sheet3 = df_sheet3.rename(columns={0:"Article Id", 1:"Main Headline Words"})

    #Sheet 4 - Article Keywords
    df_sheet4 = df[["index","keywords"]]

    list_sheet4 = []
    for i in range(len(df_sheet4)):
        for x in range(len(df_sheet4["keywords"].loc[i])):
            keyword = df_sheet4["keywords"].loc[i][x]["value"]
            index_word = [i, keyword]
            list_sheet4.append(index_word)

    df_sheet4 = pd.DataFrame(list_sheet4)
    df_sheet4 = df_sheet4.rename(columns={0:"Article Id", 1:"Main Headline Words"})

    #to Excel!
    df = df.rename(columns={"index":"Id"})

    file_name = topic_parameter + ".xlsx"

    with pd.ExcelWriter("web_app/" + file_name) as writer:  
        df.to_excel(writer, sheet_name='Data')
        df_sheet2.to_excel(writer, sheet_name='Abstract Words')
        df_sheet3.to_excel(writer, sheet_name='Headline Words')
        df_sheet4.to_excel(writer, sheet_name='Article Keywords')

    #ouput the file name
    return file_name