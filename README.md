# InnovoWebTools
This repository is a web application developed for the student run consulting agency Innovo Consulting, which operates at Georgetown University.

https://innovowebapplications.herokuapp.com/home


## Setup

Create and activate a virtual environment:

```sh
conda create -n innovowebtools-env python=3.8

conda activate innovowebtools-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Create a local ".env" file and provide your API keys like this:

```sh
FLASK_PASSWORD="______________"
FACEBOOK_ACCESS_TOKEN="______________"
INNOVO_PASSWORD="______________"
TWITTER_ACCESS_TOKEN="______________"
TWITTER_ACCESS_TOKEN_SECRET="______________"
TWITTER_API_KEY="______________"
TWITTER_API_KEY_SECRET="______________"
```

## Usage

Run the flask app on your machine:

```sh
flask run
```

Visit the deployed app online:
https://innovowebapplications.herokuapp.com/home