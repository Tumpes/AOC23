#!/usr/bin/python

class node:
	def __init__(key, left, right):
		self.key = key
		self.left = left
		self.right = right

file = open("input.txt")
data = file.read()
file.close()

data = data.split("\n")

instructions = data[0]

network_unparsed = data
network_unparsed.pop(0);network_unparsed.pop(0)

network = {}  # 

for line in network_unparsed:

	line = line.split()

	key = line[0]
	left = line[2].replace(",", "(")
	left = left.replace("(", "")
	right = line[3].replace(")", "")

	network.update({key: [left, right]})

node = network.get("AAA")
stepCount = 0
ended = 0

while True:
	for instruction in instructions:

		index = 1
		if instruction == "L":
			index = 0

		stepCount += 1
		print(node)

		nextNode = node[index]

		print(nextNode)

		if nextNode == "ZZZ":
			ended = 1
			break

		node = network.get(nextNode)

	if ended:
		break

print(stepCount)