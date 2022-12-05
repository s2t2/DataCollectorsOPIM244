# InnovoWebTools
This repository fo my final in OPIM 244

https://innovowebapplications.herokuapp.com/home


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

Create a local ".env" file and provide your API keys like this:

```sh

TWITTER_ACCESS_TOKEN="________"
TWITTER_ACCESS_TOKEN_SECRET="________"
TWITTER_API_KEY="________"
TWITTER_API_KEY_SECRET="________"

YELP_API_KEY="________"

NYT_API_KEY="________"

FLASK_APP=web_app
FLASK_PASSWORD="________"
```

## Usage

Run the flask app on your machine:

```sh
flask run
```

Visit the deployed app online:
https://innovowebapplications.herokuapp.com/home