#!usr/bin/python

def loop_cubes(cubes):

	for cube in cubes:
		amount = int(cube.split()[0])
		color = cube.split()[1][0]

		if(color == "r" and amount > 12 ):
			return 0
		if(color == "g" and amount > 13 ):
			return 0
		if(color == "b" and amount > 14 ):
			return 0

	return 1

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

	if loop_cubes(cubes):
		__sum += game_id
		print("game " + str(game_id))

print(__sum)