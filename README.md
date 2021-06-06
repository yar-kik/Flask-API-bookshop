# Bookshop with Flask-RESTful API
[![Coverage Status](https://coveralls.io/repos/github/yar-kik/Flask-API-bookshop/badge.svg?branch=master)](https://coveralls.io/github/yar-kik/Flask-API-bookshop?branch=master)
[![Build Status](https://travis-ci.com/yar-kik/Flask-API-bookshop.svg?branch=master)](https://travis-ci.com/yar-kik/Flask-API-bookshop)
![GitHub](https://img.shields.io/github/license/yar-kik/Flask-API-bookshop)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/yar-kik/Flask-API-bookshop/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/yar-kik/Flask-API-bookshop/?branch=master)
## Technologies
Project uses such technologies:
* Flask Rest-API with JWT-token for auth
* PostgreSQL
* Celery for asynchronous tasks
* Redis for caching
* Docker for containerizing
* Elasticsearch

## Requirements
You should have already installed Docker and Git. 

## Usage
Get local copy of project with: 
```
git clone https://github.com/yar-kik/Flask-API-bookshop.git
``` 

To build a local development environment and start API server run:  
```
docker-compose -f docker-compose-dev.yml up -d 
``` 
Or you can build a production ready environment: 
```
docker-compose -f docker-compose.yml up -d
``` 
This may take a few minutes. Finally, your api will work on `http://localhost:5000/` 
if you start development configuration or on `http://localhost/` if you start production 
configs.

## Functionality
With command line you can create new admin user:
```
docker-compose exec api python3 manage.py create_admin
```
Only admin can create, update and delete book items. 

Application support registration, login and logout. Users can also change password via email.
To make CRUD operation with books, admin should be logged-in and send request 
with headers `{"Content-Type": "application/json", "Authorization": "Bearer <Token>"}` 

To make operation of filtering, sorting, pagination and searching user should use 
query params, for example: 
* For sorting - `GET http://localhost:5000/books?order=desc&sort=price`
* For filtering - `GET http://localhost:5000/books?category=fantasy&language=english`
* For pagination - `GET http://localhost:5000/books?page=2`
* For searching - `GET http://localhost:5000/books?q=harry+potter`

It's possible to combine different query params in one request. 