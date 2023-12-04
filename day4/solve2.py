#!usr/bin/python

def getWinning(card):

    winning = []

    for number in card:
        if number == "|":
            break
        else:
            winning.append(number)

    return winning

def getInventory(card):

    inventory = []

    passed = 0

    for number in card:
        if number == "|":
            passed = 1
        if passed:
            inventory.append(number)

    return inventory

def getCommonItems(list1, list2):
    result = []

    for item in list1:
        if item in list2:
            result.append(item)

    return result

def getCard(index):

    card = data[index]
    card = card.split()

    card.pop(0)   # remove "card n:""
    card.pop(0)

    return card

def checkCard(index):

    global cardAmount

    if index > lines - 1:
        return

    card = getCard(index)

    winning = []
    inventory = []

    winning = getWinning(card)
    inventory = getInventory(card)



    winningNumbers = getCommonItems(winning, inventory)

    j = 1

    if(len(winningNumbers) == 0):
        cardAmount += 1
        return

    # print("index:", index, len(winningNumbers))
    while j <= len(winningNumbers):
        checkCard(index + j)
        j += 1

    cardAmount += 1

file = open("input.txt")
data = file.read()
file.close()

data = data.splitlines()
lines = len(data)

cardAmount = 0

i = 0

while i < len(data):

    checkCard(i)
    i += 1

print(cardAmount)