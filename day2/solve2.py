#!usr/bin/python

class Mincolor:
	r = 0
	b = 0
	g = 0

file = open("input.txt", "r")
data = file.read()
file.close()

data = data.split("\n")

__sum = 0

for i in range(len(data)):
	cubes = data[i]
	cubes = cubes.replace(";", ",")
	cubes = cubes.replace(":", ",")
	cubes = cubes.replace(", ", ",")
	cubes = cubes.split(",")
	game_id = int(cubes[0].split()[1])
	cubes.pop(0)

	mincolor = Mincolor()

	for cube in cubes:
		amount = int(cube.split()[0])
		color = cube.split()[1][0]

		if color == "r" and amount > mincolor.r:
			mincolor.r = amount
		if color == "b" and amount > mincolor.b:
			mincolor.b = amount
		if color == "g" and amount > mincolor.g:
			mincolor.g = amount

	power = mincolor.r * mincolor.b * mincolor.g
	__sum += power


print(__sum)