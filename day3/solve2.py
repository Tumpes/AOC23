#!usr/bin/python

import string

def FindNumbers(index):

	numbers = []

	if index != 0 and data[index - 1] in digits:
		numbers.append(index - 1)

	if index != data_length and data[index + 1] in digits:
		numbers.append(index + 1)

	a = 0
	if index - line_length > 0 and data[index - line_length] in digits:
		numbers.append(index - line_length)
		a = 1

	if index - line_length + 1 > 0 and data[index - line_length + 1] in digits and a != 1:
		numbers.append(index - line_length + 1)

	if index - line_length - 1 > 0 and data[index - line_length - 1] in digits and a != 1:
		numbers.append(index - line_length - 1)

	b = 0
	if index + line_length < data_length and data[index + line_length] in digits:
		numbers.append(index + line_length)
		b = 1

	if index + line_length + 1 < data_length and data[index + line_length + 1] in digits and b != 1:
		numbers.append(index + line_length + 1)

	if index + line_length - 1 < data_length and data[index + line_length - 1] in digits and b != 1:
		numbers.append(index + line_length - 1)

	return numbers

def getFullNumber(index):

	number = ""
	number += data[index]

	if data[index + 1] in digits:
		number += data[index + 1]

		if data[index + 2] in digits:
			number += data[index + 2]

	if data[index - 1] in digits:
		number = data[index - 1] + number

		if data[index - 2] in digits:
			number = data[index - 2] + number

	return number


file = open("input.txt")
data = file.read()
file.close()

symbols = string.punctuation.replace(".", "")
digits = string.digits

line_length = len(data.split("\n")[1])

data = data.replace("\n", "")

__sum = 0

i = 0
data_length = len(data)

while i < data_length:
	char = data[i]
	number = ""
	i_offset = 0

	if char == "*":
		numbers = []
		for numberindex in FindNumbers(i):
			numbers.append(getFullNumber(numberindex))
			print(numbers)
		if len(numbers) == 2:
			__sum += int(numbers[0]) * int(numbers[1])

	i += 1

print(__sum)

# paska implementaatio mut toimii :D:D