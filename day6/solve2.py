#!usr/bin/python

import math

file = open("input.txt")
data = file.read()
file.close()

data = data.splitlines()

times = data[0].split(" ", 1)[1]
recordDistance = data[1].split(" ", 1)[1]

time = int(times.replace(" ", ""))
recordDistance = int(recordDistance.replace(" ", ""))

solutions = 0

for holdtime in range(1, time , 1):    # this treats the time as an open interval, so 7 would loop values 1 - 6.

	distance = holdtime * (time - holdtime)
	if distance > recordDistance:
		solutions += 1


print(solutions)

# better solution for this and part 1 would be to find the first and
# last solution and calculate how many solutions there are between them.