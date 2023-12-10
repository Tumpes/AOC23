#!usr/bin/python

cards = ["J", "2", "3", "4", "5", "6", "7","8", "9", "T", "Q", "K", "A"]

class levelledHand:
	def __init__(self, hand, level, bid):
		self.hand = hand
		self.level = level
		self.bid = bid

def levelHand(hand):
	level = 0

	count = 0     
	countcard = ""

	jokerCount = hand.count("J")
	fullHouseJokerCount = hand.count("J")

	for card in cards:
		if hand.count(card) == 2 and card != "J" or hand.count(card) == 3 and card != "J":
			count = hand.count(card)
			countcard = card

	for card in cards:
		if card == "J":
			newCardCount = jokerCount
		else:
			newCardCount = hand.count(card) + jokerCount

		# if(hand == "Q2KJJ"):
		# 	# print(card, count * (hand.count(card) + fullHouseJokerCount), countcard)
		# 	print(countcard)

		if newCardCount > 3:
			level = max(newCardCount + 1, level)    # 5 and 4 of a kind; 5 and 6

		if count * (hand.count(card) + fullHouseJokerCount) == 6 and countcard != card:   # Full house
			level = max(4, level)     
			fullHouseJokerCount = 0

		if newCardCount == 3:
			level = max(3, level)        # 3 of a kind

		if count * newCardCount == 4 and card != countcard:   # Two pair
			level = max(2, level)

		if newCardCount == 2:           # One pair
			level = max(1, level)

	if(hand == "Q2KJJ"):
		print(level)

	return level

def isStronger(hand1, hand2):

	# if(hand1.hand == "Q2KJJ"):
	# 	print(hand1.level, hand2.level, hand2.hand)

	if hand1.level < hand2.level:
		return 0

	if hand1.level > hand2.level:
		return 1	

	i = 0
	while i < 6:

		# if(hand1.hand == "Q2KJJ"):
		# 	print(cards.index(hand1.hand[0]))

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
	# print(hand.hand, hand.bid, hand.level)
	total += hand.bid * (len(hands) - hands.index(hand))

print(total)