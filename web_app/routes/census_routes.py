
from flask import Blueprint, request, render_template

census_routes = Blueprint("census_routes", __name__)

#Industry Analysis Page
@census_routes.route("/IndustryAnalysis")
def IndustryAnalysis():
    return render_template("CensusDataTableau.html")