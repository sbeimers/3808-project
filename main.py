from card import Card
import funcs as funcs
import random


payouttableDict = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 6, 7: 9, 8: 25, 9: 50, 10: 250}


while (1):
    # create deck
    deck = []
    for suit in ["H", "D", "C", "S"]:
        for value in range(2, 15): #2-14
            deck.append(Card(suit, value))
    
    held = [0,0,0,0,0]


    # shuffle deck
    random.shuffle(deck)

    # deal 5 cards
    hand = []
    for i in range(5):
        hand.append(deck.pop())

    # print hand
    print(hand)

    # do button clicking until deal button is clicked

    # buttons will just change held array to 1 or 0 at index of card


    # deal new cards
    for i in range(5):
        if held[i] == 0:
            hand[i] = deck.pop()

    # idk ui update based off new chards


    #calculate hand
    value = funcs.check_hand(hand)

    # check payout table
    payout = payouttableDict[value]
    print("PAYOUTTT:")
    print(payout)


    # print(funcs.check_hand(hand))
