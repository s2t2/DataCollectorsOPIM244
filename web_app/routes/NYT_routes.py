
from flask import Blueprint, Flask, render_template, request, flash, url_for, send_file, redirect

import os
from dotenv import load_dotenv
import datetime

from app.NYT_data import NYTAPIfunction


NYT_routes = Blueprint("NYT_routes", __name__)


#Innovo NYT password page
@NYT_routes.route("/NYTAPI_password", methods=["Get","Post"])
def NYTAPI_Password():
    if request.method == "POST":
        if str(request.form["Innovo NYT Password"]) == os.environ['INNOVO_PASSWORD']:        
            return redirect("/NYTAPISuperSneaky546627!")
        
        else:
            flash("Please re-enter. The password was incorrect.")
            
    return render_template("NYTAPI_password.html")


#NYT API
@NYT_routes.route("/NYTAPI", methods=["Get","Post"])
def NYTAPI():
    if request.method == "POST":
        try:
            user_topic = str(request.form["user_topic"])
            user_date_range = str(request.form["user_date_range"])
            NYT_API_KEY = os.getenv("NYT_API_KEY")

            file = NYTAPIfunction(NYT_API_KEY, user_topic, user_date_range)
            return send_file(file, as_attachment = True)

        except:
            flash("Please re-enter. There was an error with your inputs.", "danger")


    return render_template("NYTAPI.html")