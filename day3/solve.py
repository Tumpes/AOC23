#!usr/bin/python

import string

def checksquares(index, data):

	squares = set()

	if index != 0:
		squares.add(data[i - 1])

	if index != data_length:
		squares.add(data[index + 1])

	if index - line_length + 1 > 0:
		squares.add(data[index - line_length + 1])

	if index - line_length > 0:
		squares.add(data[index - line_length])

	if index - line_length - 1 > 0:
		squares.add(data[index - line_length - 1])

	if index + line_length + 1 < data_length:
		squares.add(data[index + line_length + 1])

	if index + line_length < data_length:
		squares.add(data[index + line_length])

	if index + line_length - 1 < data_length:
		squares.add(data[index + line_length - 1])

	return squares

# -1, +1, +9, +10, +11, -9, -10, -11

file = open("input.txt")
data = file.read()
file.close()

symbols = string.punctuation.replace(".", "")
digits = string.digits

line_length = len(data.split("\n")[1]) # + 1 for newline character

data = data.replace("\n", "")

__sum = 0

i = 0
data_length = len(data)

while i < data_length:
	char = data[i]

	number = ""
	i_offset = 0

	if not char in digits:
		i += 1
		continue

	number += char

	if data[i + 1] in digits:
		number += data[i + 1]
		i_offset += 1

	if data[i + 2] in digits:
		number += data[i + 2]
		i_offset += 1

	squares = set()

	squares.update((checksquares(i, data)))

	if i_offset != 0:
		squares.update((checksquares(i + i_offset, data)))

	i += i_offset + 1

	# squares = {"." if x == "\n" else x for x in squares} # squares.replace("\n", ".")

	print("squares: ", squares)
	print("number: ", number)

	if squares & set(symbols):
		__sum += int(number)

print(__sum)