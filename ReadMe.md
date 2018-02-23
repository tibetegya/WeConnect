# WeConnect 
![banner](./UI/css/Images/banner.png)

This repository contains the Andela Challenge Project


**travis-ci** [![Build Status](https://travis-ci.org/tibetegya/WeConnect.svg?branch=business-api)](https://travis-ci.org/tibetegya/WeConnect)       
 **code-climate** [![Test Coverage](https://api.codeclimate.com/v1/badges/3dbd33931a68c9f94865/test_coverage)](https://codeclimate.com/github/tibetegya/WeConnect/test_coverage)

## Description

WeConnect is a web application that has a Restful backend api that feeds a Reactjs front-end app

## Front End Designs

The front ent version of the application is currently made with Bootstrap it is stored in the 
UI folder which includes the templates of that capture the following.<br>
    User registration,User login, A page where an authenticated user can register his/her business.
    A page that shows the profile of a business and shows the available reviews from users about  that business.
    A page  where a user updates his/her business profile.
    A page  where a user updates his/her business profile.
- UI Designs for the front-end application are hosted on [Github-Pages](http://www.tibetegya.com/WeConnect/)

The folder Structure for the UI folder is as follows
```bash
  |-- UI/
  |     |- css/
  |     |   |- fonts/ 
  |     |   |       |-  lineto-circular-black.eot
  |     |   |       |-  lineto-circular-black.svg
  |     |   |       |-  lineto-circular-black.ttf
  |     |   |       |-  lineto-circular-black.woff
  |     |   |
  |     |   |- Images/
  |     |   |         |-  banner.png
  |     |   |         |-  close.png
  |     |   |         |-  favicon.png
  |     |   |         |-  hero.png
  |     |   |         |-  logo.png
  |     |   |         |-  logo.svg
  |     |   |         |-  plus.svg
  |     |   |         |-  search.png
  |     |   |         |-  search.svg
  |     |   |
  |     |   |
  |     |   |-  bootstrap.css
  |     |   |-  gradstrap.css
  |     |   |-  style.css
  |     |   |-  style.css.mao
  |     |   |-  style.sass
  |     |
  |     |-  js/
  |     |      |-  bootstrap.js
  |     |
  |     |-  add-business.html
  |     |-  add-review.html
  |     |-  index.html
  |     |-  login.html
  |     |-  register.html
  |     |-  user-profile.html

```
- WeConnect currently has 4 Branches
  - [master](https://github.com/tibetegya/WeConnect/tree/master)
  - [business-api](https://github.com/tibetegya/WeConnect/tree/business-api)
  - [user-api](https://github.com/tibetegya/WeConnect/tree/feature)
  - [feature](https://github.com/tibetegya/WeConnect/tree/feature)

## API-Application 
The API Back-end is implemented using flask and it is a RestFul API it is also
implemented using unittests (Test Driven Development)
## Dependancies


  - [flask](flask.pocoo.org/)
  - [flask-Restful](https://flask-restful.readthedocs.io/)
  - [pytest](https://pytest.org/)
  - [virtualenv](https://virtualenv.pypa.io/en/stable/)
  - [flask](http://flask-jwt.readthedocs.io/en/latest/)

## Set Up

This is the File Structure for (api-application) is as follows
``` bash
  |- api-application/
  |                 | app/|
  |                 |     |-  __init__.py
  |                 |     |-  business_api.py
  |                 |     |-  test_business_api.py
  |                 |     |-  test_user_api.py
  |                 |     |-  user_api.py
  |                 |
  |                 |
  |                 |-  .gitignore
  |                 |-  config.py
  |                 |-  requirements.txt
  |                 |-  run.py


```


In order to run the API Application 

1. Clone this Repository to your development machine 
    - Start by copying the url to this Repository 
    > https://github.com/tibetegya/WeConnect.git 
    - Run this command in git bash to create the repo locally 
    ` git clone https://github.com/tibetegya/WeConnect.git `

2. Create a virtual environment inside api-appliction folder using in a terminal shell  ` virtualenv  ENV`

3. Activate the virtual environment but running the following command ` ENV\scripts\activate `
2. Install the dependencies by running the following command in a terminal shell  
` pip install requirements.txt `
5. Now set Flask App name by running  ` export FLASK_APP = run.py ` <br>
In case you are on windows use  ` set `  instead of  ~~` export`~~ 

4. Run the application by running commands ` flask run`


## API End points
| EndPoint |Method|
|-------------|-------------|
|` /api/auth/register `| POST  |
|`  /api/auth/login`|  POST |
|`  /api/auth/logout`| POST |
|` /api/auth/reset-password `| POST |
|`   /api/businesses`| POST |
|`/api/businesses/<businessId>`| PUT |
|` /api//businesses/<businessId>`| DELETE |
|`/api/businesses`| GET   |
` /api/businesses/<businessId>`| GET   |
|` /api/businesses/<businessId>/reviews`| POST  |
|`/api/businesses/<businessId>/reviews`|  GET  |


1. Test the endpoints using [Postman](https://www.getpostman.com/) or [Curl](https://curl.haxx.se/)

2. Use Pytest to test the endpoints For example Run ` pytest test_user_api.py`

## Deployment 

The application is deployed on Heroku Server at 
>https://weconnect-tibe.herokuapp.com/

## License
The project is licensed using MIT License therefore you are free to clone the repository and 
modify the code base in any way you would like. 

Copyright 2018 Tibzyart [MIT](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwiTvrzsh9_YAhWC1hQKHekjDHYQFggzMAE&url=https%3A%2F%2Fopensource.org%2Flicenses%2FMIT&usg=AOvVaw1MsEPekvPKCIceu2jiRDy4)




