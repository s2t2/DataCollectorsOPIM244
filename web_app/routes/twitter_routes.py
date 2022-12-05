
from flask import Blueprint, Flask, render_template, request, flash, url_for, send_file, redirect

import os
from dotenv import load_dotenv
import datetime

from app.twitter_data import twitterAPIfunction


twitter_routes = Blueprint("twitter_routes", __name__)


#Innovo Twitter password page
@twitter_routes.route("/twitterAPI_password", methods=["Get","Post"])
def twitterAPI_Password():
    if request.method == "POST":
        if str(request.form["Innovo Twitter Password"]) == os.environ['INNOVO_PASSWORD']:        
            return redirect("/twitterAPISuperSneaky546627!")
        
        else:
            flash("Please re-enter. The password was incorrect.")
            
    return render_template("twitterAPI_password.html")


#Twitter API
@twitter_routes.route("/twitterAPI", methods=["Get","Post"])
def twitterAPI():
    if request.method == "POST":
        try:
            user_API_type = "account" #str(request.form["user_API_type"])
            user_twitter = str(request.form["user_twitter"])
            TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
            TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
            TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
            TWITTER_API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")

            file = twitterAPIfunction(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_API_KEY, 
                                        TWITTER_API_KEY_SECRET, user_API_type, user_twitter)

            #this was only required for the Twitter file
            file = file[8:]
            
            return send_file(file, as_attachment = True)

        except:
            flash("Please re-enter. There was an error with your inputs.", "danger")


    return render_template("twitter_API.html")