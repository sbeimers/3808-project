# MATH3808 Final Project - Video Poker
# Authors: Elias Hawa, Sebastian Beimers, Victor Li

from collections import defaultdict

# Given 5 card class objects, determine the best hand
def check_hand(hand):
    # Sorts from Ace to 2
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
    if check_high_pair(hand):
        return 2
    return 1

def convertNumberToWinner(x):
    if x == 1:
        return "Lose"
    if x == 2:
        return "Win: High Pair"
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

# Given a hand of 5 cards, determine if it is a royal flush
def check_royal_flush (hand):
    return check_straight_flush(hand) and hand[0].value == 14 and hand[1].value == 13

# Given a hand of 5 cards, determine if it is a straight flush
def check_straight_flush (hand):
    return check_flush(hand) and check_straight(hand)

# Given a hand of 5 cards, determine if it is a four of a kind
def check_four_of_a_kind(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    # check if there are only two different values, and one of them has a count of 4
    return sorted(value_counts.values()) == [1,4]

# Given a hand of 5 cards, determine if it is a full house
def check_full_house(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    # check if there are only two different values, and they have counts of 2 and 3
    return sorted(value_counts.values()) == [2,3]

# Given a hand of 5 cards, determine if it is a flush
def check_flush(hand):
    # check if all suits are the same
    return hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit

# Given a hand of 5 cards, determine if it is a straight
def check_straight(hand):
    values = [i.value for i in hand]
    # if there is no ace, then the straight is just 5 in a row
    if values[0] != 14:
        return values[1] == values[0]-1 and values[2] == values[1]-1 and values[3] == values[2]-1 and values[4] == values[3]-1
    else: # if there is an ace, then the straight is either 14,5,4,3,2 or 14,13,12,11,10
        return (values[1] == 5 and values[2] == 4 and values[3] == 3 and values[4]) == 2 or (values[1] == 13 and values[2] == 12 and values[3] == 11 and values[4] == 10)

# Given a hand of 5 cards, determine if it is a three of a kind
def check_three_of_a_kind(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    # check if there are exactly three different values, and one of them has a count of 3
    return set(value_counts.values()) == set([3,1])

# Given a hand of 5 cards, determine if it is a two pair
def check_two_pair(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    # check if there are exactly three different values, and two of them have a count of 2
    return sorted(value_counts.values())==[1,2,2]

# Given a hand of 5 cards, determine if it is a pair
def check_high_pair(hand):
    values = [i.value for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    return ((value_counts[11] == 2 or value_counts[12] == 2 or value_counts[13] == 2 or value_counts[14] == 2))

