from card import Card
import funcs as funcs

# create deck
deck = []
for suit in ["H", "D", "C", "S"]:
    for value in range(2, 15): #2-14
        deck.append(Card(suit, value))

# shuffle deck
import random
random.shuffle(deck)

# deal 5 cards
hand = []
for i in range(5):
    hand.append(deck.pop())

print(hand[0])
print(hand[0].suit)

# print hand

for i in range (1, 5):
    print(i)
print (hand[0].suit)
print (hand[1].suit)
print (hand[2].suit)
print (hand[3].suit)
print (hand[4].suit)

print(hand)
print(funcs.check_hand(hand))
