
from flask import Blueprint, request, render_template, send_file

finance_routes = Blueprint("finance_routes", __name__)

#Financial Statements Page
@finance_routes.route("/FinancialStatements", methods=["Get","Post"])
def financialStatements():
    if request.method == "POST":
        return send_file("Innovo Financial Statements.xlsx", as_attachment = True)
   
    return render_template("financial_statements.html")