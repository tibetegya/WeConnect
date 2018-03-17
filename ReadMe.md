# WeConnect

![banner](./UI/css/Images/banner.png)

This repository contains the Andela Challenge Project

[![Build Status](https://travis-ci.org/tibetegya/WeConnect.svg?branch=api-v3)](https://travis-ci.org/tibetegya/WeConnect)
 [![Test Coverage](https://api.codeclimate.com/v1/badges/3dbd33931a68c9f94865/test_coverage)](https://codeclimate.com/github/tibetegya/WeConnect/test_coverage)
 [![Maintainability](https://api.codeclimate.com/v1/badges/3dbd33931a68c9f94865/maintainability)](https://codeclimate.com/github/tibetegya/WeConnect/maintainability)
 [![Coverage Status](https://coveralls.io/repos/github/tibetegya/WeConnect/badge.svg?branch=master)](https://coveralls.io/github/tibetegya/WeConnect?branch=master)

## Description

WeConnect is a web application that has a Restful backend api that feeds a Reactjs front-end app

## Front End Designs

The front ent version of the application is currently made with Bootstrap it is stored in the
UI folder which includes the templates of that capture the following.
    User registration,User login, A page where an authenticated user can register his/her business.
    A page that shows the profile of a business and shows the available reviews from users about  that business.
    A page  where a user updates his/her business profile.
    A page  where a user updates his/her business profile.
- UI Designs for the front-end application are hosted on [Github-Pages](http://www.tibetegya.com/WeConnect/)

## API-Application

The API Back-end is implemented using flask and it is a RestFul API it is also
implemented using unittests (Test Driven Development)

## Dependancies

- [flask](flask.pocoo.org/)
- [flask-Restplus](https://flask-restplus.readthedocs.io/)
- [pytest](https://pytest.org/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)
- [flask](http://flask-jwt.readthedocs.io/en/latest/)
- Pytest

## Set Up

In order to run the API Application

1. Clone this Repository to your development machine
    - Start by copying the url to this Repository
    > https://github.com/tibetegya/WeConnect.git
    - Run this command in git bash to create the repo locally
    `git clone https://github.com/tibetegya/WeConnect.git`

2. Create a virtual environment inside api-appliction folder using in a terminal shell  `virtualenv  ENV`

3. Activate the virtual environment but running the following command `env\scripts\activate`

4. Install the dependencies by running the following command in a terminal shell `pip install requirements.txt`

5. Now set Flask App name by running  `export FLASK_APP = run.py` (for Linux and Mac)
    In case you are on Windows use  `set`  instead of  ~~`export`~~

6. Run the application by running commands `flask run`

## API End points

| EndPoint |Method|
|-------------|-------------|
|`/api/auth/register`| POST  |
|`/api/auth/login`|  POST |
|`/api/auth/logout`| POST |
|`/api/auth/reset-password`| POST |
|`/api/businesses`| POST |
|`/api/businesses/<businessId>`| PUT |
|`/api//businesses/<businessId>`| DELETE |
|`/api/businesses`| GET   |
|`/api/businesses/<businessId>`| GET   |
|`/api/businesses/<businessId>/reviews`| POST  |
|`/api/businesses/<businessId>/reviews`|  GET  |

1. Test the endpoints using [Postman](https://www.getpostman.com/) or [Curl](https://curl.haxx.se/)

2. Use Pytest to test the endpoints For example Run `pytest tests.py`

## Deployment

The application is deployed on Heroku Server at
>https://weconnect-tibe.herokuapp.com/

## License

The project is licensed using MIT License therefore you are free to clone the repository and
modify the code base in any way you would like.

Copyright 2018 Tibetegya [MIT](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwiTvrzsh9_YAhWC1hQKHekjDHYQFggzMAE&url=https%3A%2F%2Fopensource.org%2Flicenses%2FMIT&usg=AOvVaw1MsEPekvPKCIceu2jiRDy4)
