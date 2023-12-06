#!usr/bin/python

import math

file = open("input.txt")
data = file.read()
file.close()

data = data.splitlines()

times = data[0].split()
distances = data[1].split()

times.pop(0); distances.pop(0) # remove "time:" and "distance:" text

i = 0

waysToBeat = []

while i < len(times):
	time = int(times[i])
	recordDistance = int(distances[i])

	solutions = 0

	for holdtime in range(1, time , 1):    # this treats the time as an open interval, so 7 would loop values 1 - 6.

		distance = holdtime * (time - holdtime)
		if distance > recordDistance:
			solutions += 1

	waysToBeat.append(solutions)

	i += 1

print(waysToBeat)

result = math.prod(waysToBeat) # multiply all numbers together

print(result)
