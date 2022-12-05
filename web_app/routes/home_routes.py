# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

#home page
@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("index.html")

#tableau examples page
@home_routes.route("/tableau")
def tableau():
    return render_template("tableau_examples.html")

#about page
@home_routes.route("/about")
def about():
    return render_template("about.html")

#privacy policy page
@home_routes.route("/privacypolicy")
def privacy_policy():
    return render_template("privacyPolicy.html")
