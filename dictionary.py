#Defining the keys and values of the movie within a dictionary
movie = {
	"title" : "Pulp Fiction",
	"year" : "1994",
	"duration" : 154,
	"director" : "Quentin Tarantino"
}

#Defining the actors of the movie within a list
movie["actors"] = ["John Travolta", " Samual L. Jackson", " Bruce Willis" ]

#Looping over the keys in the dictionary. If the key is duration: it adds minutes. 
#If the key is actors. It joins the seperate values to a single string
for key, val in movie.items():
	if key == "duration":
		print(f"{key} : {val} minutes")
	elif key == "actors":
		print(key + " : " + ",".join(val))
	else:
		print(f"{key} : {val}")
