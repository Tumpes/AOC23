#!usr/bin/python

def getWinning(card):

	winning = []

	for number in card:
		if number == "|":
			break
		else:
			winning.append(number)

	return winning

def getInventory(card):

	inventory = []

	passed = 0

	for number in card:
		if number == "|":
			passed = 1
		if passed:
			inventory.append(number)

	return inventory

def getCommonItems(list1, list2):
	result = []

	for item in list1:
		if item in list2:
			result.append(item)

	return result

file = open("input.txt")
data = file.read()
file.close()

data = data.split("\n")

points = 0

for card in data:
	card = card.replace("  ", " ")
	card = card.split(" ")

	card.pop(0)   # remove "card n:""
	card.pop(0)

	print(card)
	winning = []
	inventory = []

	winning = getWinning(card)
	inventory = getInventory(card)

	winningNumbers = getCommonItems(winning, inventory)

	temp_points = 0

	for i in winningNumbers:
		if temp_points == 0:
			temp_points += 1
		else:
			temp_points *= 2

	points += temp_points

print(points)