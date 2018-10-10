import requests
import json

#requesting the article by input and striping it. And replacing the spaces with underscores
article_request = input("What article do you want to know more about? ")
article_request = article_request.strip().replace(" ", "_")

#Adding the article request to the url
url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + article_request


req = requests.get(url)

#Loading the data from the json file and defining the values
data = json.loads(req.text)
title = data["title"]
description = data["description"]
extract = data["extract"]

#checking for the right status code
status = req.status_code
if status != 200:
	print("This subject could not be found. Restart the program")
	quit()

#printing everything
print(f"Title: {title}\nDescription: {description}\nExtract: {extract}")