#!/usr/bin/python

numbers = "123456789"
file = open("input.txt", "r")
calibration_value = file.read()
file.close() 

calibration_value = calibration_value.replace("one", "o1e")
calibration_value = calibration_value.replace("two", "t2o")
calibration_value = calibration_value.replace("three", "t3e")
calibration_value = calibration_value.replace("four", "f4r")
calibration_value = calibration_value.replace("five", "f5e")
calibration_value = calibration_value.replace("six", "s6x")
calibration_value = calibration_value.replace("seven", "s7n")
calibration_value = calibration_value.replace("eight", "e8t")
calibration_value = calibration_value.replace("nine", "n9e")

calibration_value = calibration_value.split("\n")

first = 0
last = 0
__sum = 0

for i in range(len(calibration_value)):

	string = calibration_value[i]

	if len(string) == 0:
		continue

	for char in range(len(string)):
		if string[char] in numbers:
			first = string[char]
			break

	for char in range(len(string)-1, -1, -1): # start, end, increment
		if string[char] in numbers:
			last = string[char]
			break	

	result = int(str(first) + str(last))
	__sum += result

print(__sum)
