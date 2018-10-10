#import the needed requests
import requests

#Ask for and strip the URL the user wants to check
user_url = input("What URL do you want to check?")
user_url = user_url.strip()

#defining req and status
req = requests.get(user_url)
status = req.status_code

#Displaying an Error if the status code is anything but 200
if status != 200:
	print("Error")

else:
	print(status)

#Getting the headers from the URL and printing them
headers = req.headers

for key, val in headers.items():
	print(f"{key} : {val}")
