
# this is the "web_app/__init__.py" file...

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.about_routes import about_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.yelp_routes import yelp_routes
from web_app.routes.NYT_routes import NYT_routes


load_dotenv()

SECRET_KEY = os.getenv('FLASK_PASSWORD')


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(about_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(yelp_routes)
    app.register_blueprint(NYT_routes)


    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)