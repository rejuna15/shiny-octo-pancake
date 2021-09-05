URL Shortener

The app is written in FLASK and consists of 2 services
Use pip install validators (To install the validators package)
RUN
Use pathtoproject/app.py flask run to run the project

1)ShortUrl
Method: GET
Query Params: url
Example https://hostname.com/ShortUrl?url=https://abcd.com

Service will validate the url first to verify if its a valid url
Then it will check if the URl has already been shortened. If yes it will display the shortened url
Else it will proceed to base 62 encode the url to return a 6 character long shortened url

2)OriginalUrl
Method Get
Query Params: short_url
Example https://hostname.com/OriginalUrl?short_url=aUKYOC

Service will decode the shortened url and get the id of the URL. It will then query the database to return the original URL

Time Taken for Project: ~3.5 hr

