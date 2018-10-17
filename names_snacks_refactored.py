friends = ["Arjen ", "Emiel ", "Ayco ", "Piet ", "Jan "]
snacks = []

index2 = 0
for name in friends:
	name = friends[index2]
	index2 = index2 + 1
	snacks.append(input(name +", What is your favourite snack?"))
		
index = 0		
for name in friends:
	snack = snacks[index]	
	index = index + 1
	print(name + "likes " + snack)	