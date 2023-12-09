#!/usr/bin/python

file = open("input.txt")
data = file.read()
file.close()

data = data.split("\n")

instruction = data[0]

network = data
network.pop(0);network.pop(0)

print(network)

