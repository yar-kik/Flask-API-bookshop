# Bookshop with Flask and React
[![Coverage Status](https://coveralls.io/repos/github/yar-kik/botforqueue/badge.svg?branch=master)](https://coveralls.io/github/yar-kik/botforqueue?branch=master)
[![Build Status](https://travis-ci.com/yar-kik/botforqueue.svg?branch=master)](https://travis-ci.com/yar-kik/botforqueue)

## Technologies
Project use such technologies:
* Flask Rest-API as backend
* React as frontend
* PostgreSQL as database
* Docker for containerizing

## Requirements
You should have already installed Docker. 

## Usage
With `git clone https://github.com/yar-kik/botforqueue.git` get local copy of project.

Run `docker-compose build` to build a local development environment according to our specifications in docker-compose.yml. 

After the containers have been built (this may take a few minutes), run 

`docker-compose up` 

This one command boots up a local server for Flask (on port 5000) and React (on port 3000). Head over to

`http://localhost:3000/` 

to view an React webpage with ... empty main page. 
