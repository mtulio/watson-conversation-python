# Simple Watson Conversation Application

This is a simple conversation application using IBM Bluemix Watson Conversation API.

This application is an python version of [Conversation Simple NodeJS Application](https://github.com/watson-developer-cloud/conversation-simple) using `ibm-developer-cloud` Library.

To use it you should have an Bluemix account and an Conversation Application created. You can find more information in the original NodeJS application commendted above

## Environments

To run this application you should create an `.env`. To do this copy the file `.env.example` and change with your values.

`cp .env.example .env `

## Running

* Create Python virtualenv and install dependencies

`make dependencies`

* Run the application

`make run`

## Notes

> In production environment is strongly recommended to use static files in an performatic webserver, like NGINX.
