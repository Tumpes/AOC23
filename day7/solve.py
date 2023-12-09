#!usr/bin/python

cards = ["2", "3", "4", "5", "6", "7","8", "9", "T", "J", "Q", "K", "A"]

class levelledHand:
	def __init__(self, hand, level, bid):
		self.hand = hand
		self.level = level
		self.bid = bid

def levelHand(hand):
	level = 0

	count = 0     
	countcard = ""

	for card in cards:
		if hand.count(card) == 2 or hand.count(card) == 3:
			count = hand.count(card)
			countcard = card

	for card in cards:

		if hand.count(card) > 3:
			level = max(hand.count(card) + 1, level)    # 5 and 4 of a kind; 5 and 6


		if count * hand.count(card) == 6:   # Full house
			level = max(4, level)

		if hand.count(card) == 3:
			level = max(3, level)                       # 3 of a kind

		if count * hand.count(card) == 4 and card != countcard:   # Two pair
			level = max(2, level)

		if hand.count(card) == 2:           # One pair
			level = max(1, level)

	return level

def isStronger(hand1, hand2):

	if hand1.level < hand2.level:
		return 0

	if hand1.level > hand2.level:
		return 1	

	i = 0
	while i < 6:

		if(cards.index(hand1.hand[i]) > cards.index(hand2.hand[i])):
			return 1

		if(cards.index(hand1.hand[i]) < cards.index(hand2.hand[i])):
			return 0

		i += 1

def PlaceHandInList(hand, list):

	for i in range(len(list)):
		if isStronger(hand, list[i]):
			list.insert(i, hand)
			return list

	list.insert(len(list), hand)

	return list

 # main:

file = open("input.txt")
data = file.read()
file.close()

data = data.split("\n")

hands = []

for item in data:	
	hand = item.split()[0]
	bid = int(item.split()[1])
	hand = levelledHand(hand, levelHand(hand), bid)
	
	PlaceHandInList(hand, hands)

total = 0

for hand in hands:
	total += hand.bid * (len(hands) - hands.index(hand))

print(total)