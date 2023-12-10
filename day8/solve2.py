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

network = {}  

for line in network_unparsed:

	line = line.split()

	key = line[0]
	left = line[2].replace(",", "(")
	left = left.replace("(", "")
	right = line[3].replace(")", "")

	network.update({key: [left, right]})

nodes = []

for node in network:
	if node[2] == "A":
		nodes.append(network.get(node))

# node = network.get("AAA")
stepCount = 0
ended = 0
Zcount = 0
currentNode = ""
newNodes = []

while True:
	for instruction in instructions:

		stepCount += 1

		index = 1
		if instruction == "L":
			index = 0

		for i in range(len(nodes)):
			node = nodes[i]

			nextNode = node[index]
			print(nextNode)

			if nextNode[2] == "Z":
				Zcount += 1

			if Zcount == len(nodes):
				ended = 1
				print("voitettu ASDASDASD")
				break

			# print(currentNode)

			currentNode = nextNode

			newNodes.append(network.get(nextNode))

		newNodes.clear()

		if ended:
			break
		Zcount = 0
		nodes = newNodes

	if ended:
		break

print(stepCount)