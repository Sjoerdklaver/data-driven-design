friends = [
	["Arjen"],
	["Emiel"],
	["Ayco"]
]

for friend in friends:
	print(friend[0] + " is " + str(len(friend[0])) + " letters lang ")
	snack = input(" What is your favourite snack? ")
	friend.append(snack)

for friend in friends:
	print(friend[0] + " his favourite snack is " + friend[1])

