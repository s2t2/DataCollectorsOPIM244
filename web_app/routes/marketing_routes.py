
from flask import Blueprint, request, render_template, send_file

marketing_routes = Blueprint("marketing_routes", __name__)

#Marketing Tools Page
@marketing_routes.route("/MarketingTools", methods=["Get","Post"])
def marketingTools():

    if request.method == "POST":
        platform = str(request.form["platform"])
    
        if platform == "all":
            return send_file("Social Media Audit.xlsx", as_attachment = True)

        elif platform == "instagram":
            return send_file("Instagram Audit.xlsx", as_attachment = True)
        
        elif platform == "facebook":
            return send_file("Facebook Audit.xlsx", as_attachment = True)
        
        elif platform == "twitter":
            return send_file("Twitter Audit.xlsx", as_attachment = True)
        
        elif platform == "tiktok":
            return send_file("TikTok Audit.xlsx", as_attachment = True)
        
        elif platform == "linkedin":
            return send_file("LinkedIn Audit.xlsx", as_attachment = True)

        elif platform == "pinterest":
            return send_file("Pinterest Audit.xlsx", as_attachment = True)


    return render_template("marketing_tools.html")


#Post Template #1
@marketing_routes.route("/PostTemplate1", methods=["Get","Post"])
def postTemplate1():
    return send_file("Social Media Templates_Part1.pdf", as_attachment = True)
#Post Template #2
@marketing_routes.route("/PostTemplate2", methods=["Get","Post"])
def postTemplate2():
    return send_file("Social Media Templates_Part2.pdf", as_attachment = True)

#Post Template #3
@marketing_routes.route("/PostTemplate3", methods=["Get","Post"])
def postTemplate3():
    return send_file("Social Media Templates_Part3.pdf", as_attachment = True)

#Post Template #4
@marketing_routes.route("/PostTemplate4", methods=["Get","Post"])
def postTemplate4():
    return send_file("Social Media Templates_Part4.pdf", as_attachment = True)

#Post Template #5
@marketing_routes.route("/PostTemplate5", methods=["Get","Post"])
def postTemplate5():
    return send_file("Social Media Templates_Part5.pdf", as_attachment = True)

#Post Template #6
@marketing_routes.route("/PostTemplate6", methods=["Get","Post"])
def postTemplate6():
    return send_file("Social Media Templates_Part6.pdf", as_attachment = True)

#Post Template #7
@marketing_routes.route("/PostTemplate7", methods=["Get","Post"])
def postTemplate7():
    return send_file("Social Media Templates_Part7.pdf", as_attachment = True)