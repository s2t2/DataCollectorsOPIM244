
from yelpapi import YelpAPI
from openpyxl import Workbook, load_workbook
import pandas as pd

import datetime


def yelpAPIfunction(YELP_API_KEY_parameter, search_term, location_parameter):

    with YelpAPI(YELP_API_KEY_parameter, timeout_s = 3.0) as yelp_api:
        data = yelp_api.search_query(term=search_term, location=location_parameter, limit=50)

    #Sheet 1 Consolidated Code
    df = pd.DataFrame(data["businesses"])

    df = df.reset_index()

    def city(x):
        city = x["city"]
        return city

    def zip_code(x):
        zip_code = x["zip_code"]
        return zip_code

    df["city"] = df["location"].apply(lambda x: city(x))
    df["zip_code"] = df["location"].apply(lambda x: zip_code(x))

    def lat(x):
        latitude = x["latitude"]
        return latitude

    def long(x):
        longitude = x["longitude"]
        return longitude

    df["latitude"] = df["coordinates"].apply(lambda x: lat(x))
    df["longitude"] = df["coordinates"].apply(lambda x: long(x))

    #Sheet 2 Consolidated Code
    df_sheet2 = df[['index', 'categories']]

    categories_list = []
    for i in range(len(df_sheet2)):
        for x in range(len(df_sheet2['categories'].loc[i])):
            categories = [i, df_sheet2['categories'].loc[i][x]['title']]
            categories_list.append(categories)
            
    df_sheet2 = pd.DataFrame(categories_list)
    df_sheet2 = df_sheet2.rename(columns={0:"Business Id", 1:"Categories"})

    excel_file_name = "Yelp Data" + ", " + location_parameter + ", " + search_term + ".xlsx"
    #to an Excel file!
    with pd.ExcelWriter("web_app/" + excel_file_name) as writer:  
        df.to_excel(writer, sheet_name='Data')
        df_sheet2.to_excel(writer, sheet_name='Categories')

    #ouput the file name
    return excel_file_name, df, df_sheet2