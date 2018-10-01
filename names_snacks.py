friends = ["Arjen ", "Emiel ", "Ayco "]

print(friends)
print(len(friends[0]))
print(len(friends[1]))
print(len(friends[2]))


snacks = []

snacks.append(input("What is your favourite snack? Arjen? "))
snacks.append(input("What is your favourite snack? Emiel? "))
snacks.append(input("What is your favourite snack? Ayco? "))
		
index = 0		
for name in friends:
	snack = snacks[index]	
	index = index + 1
	print(name + "likes " + snack)	



"""
print(friends[0] + " his favourite snack is " + snacks[0])
print(friends[1] + " his favourite snack is " + snacks[1])
print(friends[2] + " his favourite snack is " + snacks[2])
"""