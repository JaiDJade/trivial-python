import random
mylist = []

minimum = input("Smallest number possible: ")
maximum = input("Largest number possible: ")
slot = input("Amount of numbers needed: ")

for i in range(0, int(slot)):
	x = random.randint(int(minimum), int(maximum))
	mylist.append(x)
print(mylist)
