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

### Usage

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# ensure FLASK_APP=web_app is in the ".env" file

flask run
```

## Testing

Run tests:

```sh
pytest
```

