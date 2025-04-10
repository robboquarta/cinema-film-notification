I NEED TO BE THE FIRST TO PRE-ORDER TICKETS OF MI... Sooo I made this simple script on AWS Cloud

This python script running on AWS Cloud Lambda is made to check for every time rate (I decided 6 hours) if the film Mission Impossible - Final Reckoning is out at Cinema. If out will send a notification Email and SMS.
The function is written in Python 3.x, deployed with AWS Lambda + EventBridge and the AWS Simple Notification Service.

The library bs4 BeautifulSoup of python helps me scrape the Cinema site and with a simple text check in a html tag of listed films I can determine if is available to pre-order tickets for the film.
