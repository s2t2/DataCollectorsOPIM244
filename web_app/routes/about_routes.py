
from flask import Blueprint, request, render_template

about_routes = Blueprint("about_routes", __name__)

#privacy policy page
@about_routes.route("/privacypolicy")
def privacy_policy():
    return render_template("privacyPolicy.html")