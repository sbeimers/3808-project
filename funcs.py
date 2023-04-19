import random
from collections import defaultdict
from card import Card

#given 5 card class objects, determine the best hand
def check_hand(hand):
    # sorts from Ace to 2
    hand.sort()
    if check_royal_flush(hand):
        return 10
    if check_straight_flush(hand):
        return 9
    if check_four_of_a_kind(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pair(hand):
        return 3
    if check_pair(hand):
        return 2
    return 1

def convertNumberToWinner(x):
    if x == 1:
        return "Lose"
    if x == 2:
        return "Win: Pair"
    if x == 3:
        return "Win: Two Pair"
    if x == 4:
        return "Win: 3 of a Kind"
    if x == 5:
        return "Win: Straight"
    if x == 6:
        return "Win: Flush"
    if x == 7:
        return "Win: Full House"
    if x == 8:
        return "Win: 4 of a Kind"
    if x == 9:
        return "Win: Straight Flush"
    if x == 10:
        return "Win: Royal Flush"



# given a hand of 5 cards, determine if it is a royal flush
def check_royal_flush (hand):
    return check_flush(hand) and check_straight(hand) and hand[0].value == 14


# given a hand of 5 cards, determine if it is a straight flush
def check_straight_flush (hand):
    return check_flush(hand) and check_straight(hand)

def check_four_of_a_kind(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_flush(hand):
    return hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit

def check_straight(hand):
    values = [i.value for i in hand]
    if values[0] != 14:
        return values[1] == values[0]-1 and values[2] == values[1]-1 and values[3] == values[2]-1 and values[4] == values[3]-1
    else:
        return (values[1] == 2 and values[2] == 3 and values[3] == 4 and values[4]) == 5 or (values[1] == 13 and values[2] == 12 and values[3] == 11 and values[4] == 10)

def check_three_of_a_kind(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    return set(value_counts.values()) == set([3,1])

def check_two_pair(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    return sorted(value_counts.values())==[1,2,2]

def check_pair(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    # print (value_counts)
    return ((value_counts[11] == 2 or value_counts[12] == 2 or value_counts[13] == 2 or value_counts[14] == 2))

