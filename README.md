# Data Collectors OPIM 244
https://datacollectors.herokuapp.com/

This web application is my final project for Managing Business Application Development in Python (OPIM 244) at Georgetown University. The application is a set of data collectors intended to assist small business and student consultants.

## Setup


Create and activate a virtual environment:

```sh
conda create -n datacollectors-env python=3.8

conda activate datacollectors-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain Twitter API Credentials](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) (i.e. `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`, `TWITTER_API_KEY`, `TWITTER_API_KEY_SECRET`)

[Obtain Yelp API Credentials](https://docs.developer.yelp.com/docs/fusion-intro) (i.e. `YELP_API_KEY`)

[Obtain New York Times API Credentials](https://developer.nytimes.com/) (i.e. `NYT_API_KEY`).


Then create a local ".env" file and provide the keys like this:

```sh
# this is the ".env" file...

TWITTER_ACCESS_TOKEN="_________"
TWITTER_ACCESS_TOKEN_SECRET="_________"
TWITTER_API_KEY="_________"
TWITTER_API_KEY_SECRET="_________"

YELP_API_KEY="_________"

NYT_API_KEY="_________"

FLASK_PASSWORD="_________"
FLASK_APP=web_app
```


## Usage

Run an example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python -m app.unemployment
```

Run stocks report:

```sh
python -m app.stocks
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

### Email Sending

Run the email service to send an example email and see if everything is working:

```sh
python -m app.email_service
```

Send the unemployment report via email:

```sh
python -m app.unemployment_email
```

Send the stocks report via email:

```sh
python -m app.stocks_email

# or in production mode:
APP_ENV="production" DEFAULT_SYMBOL="GOOGL" python -m app.stocks_email
```

## Testing

Run tests:

```sh
pytest
```

