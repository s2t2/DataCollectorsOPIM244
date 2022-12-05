
from flask import Blueprint, Flask, render_template, request, flash, url_for, send_file, redirect

import os
from dotenv import load_dotenv
import datetime

from app.yelp_data import yelpAPIfunction


yelp_routes = Blueprint("yelp_routes", __name__)

#Yelp API
@yelp_routes.route("/yelpAPI", methods=["Get","Post"])
def yelpAPI():
    if request.method == "POST":
        try:
            user_business = str(request.form["user_business"])
            user_location = str(request.form["user_location"])
            YELP_API_KEY = os.getenv("YELP_API_KEY")

            file = yelpAPIfunction(YELP_API_KEY, user_business, user_location)
            return send_file(file, as_attachment = True)

        except:
            flash("Please re-enter. There was an error with your inputs.", "danger")


    return render_template("yelp_API.html")