import pygame

from card import Card
import funcs as funcs
import random

payouttableDict = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 6, 7: 9, 8: 25, 9: 50, 10: 250}

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1254, 700))
pygame.display.set_caption("Video Poker")

# Load background
background_image = pygame.transform.scale(pygame.image.load("background.png"), (1254, 700))

# Load default images
card_image_1 = pygame.transform.scale(pygame.image.load("card_images/red_joker.png"), (250, 363))
card_image_2 = pygame.transform.scale(pygame.image.load("card_images/red_joker.png"), (250, 363))
card_image_3 = pygame.transform.scale(pygame.image.load("card_images/red_joker.png"), (250, 363))
card_image_4 = pygame.transform.scale(pygame.image.load("card_images/red_joker.png"), (250, 363))
card_image_5 = pygame.transform.scale(pygame.image.load("card_images/red_joker.png"), (250, 363))

# Load font
font = pygame.font.SysFont("Arial", 20)

# Load 5 buttons
hold1 = pygame.Rect(2, 200, 250, 363)
hold2 = pygame.Rect(252, 200, 250, 363)
hold3 = pygame.Rect(502, 200, 250, 363)
hold4 = pygame.Rect(752, 200, 250, 363)
hold5 = pygame.Rect(1002, 200, 250, 363)

increase_bet = pygame.Rect(100, 500, 100, 50)
decrease_bet = pygame.Rect(250, 500, 100, 50)
deal = pygame.Rect(400, 500, 100, 50)

def create_new_deck():
    deck = []
    for suit in ["H", "D", "C", "S"]:
        for value in range(2, 15): #2-14
            deck.append(Card(suit, value))
    return deck

running = True
while (running):
    # create deck
    deck = create_new_deck()

    # shuffle deck
    random.shuffle(deck)

    # deal 5 cards
    hand = []
    for i in range(5):
        hand.append(deck.pop())
    held = [0,0,0,0,0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hold1.collidepoint(event.pos):
                print("Button 1 clicked")
            elif hold2.collidepoint(event.pos):
                print("Button 2 clicked")
            elif hold3.collidepoint(event.pos):
                print("Button 3 clicked")
            elif hold4.collidepoint(event.pos):
                print("Button 4 clicked")
            elif hold5.collidepoint(event.pos):
                print("Button 5 clicked")

    # Clear the screen
    screen.fill((255, 255, 255))

    screen.blit(background_image, (0, 0))

    # Draw buttons
    pygame.draw.rect(screen, (0, 0, 0), hold1)
    pygame.draw.rect(screen, (0, 0, 0), hold2)
    pygame.draw.rect(screen, (0, 0, 0), hold3)
    pygame.draw.rect(screen, (0, 0, 0), hold4)
    pygame.draw.rect(screen, (0, 0, 0), hold5)

    # Draw images
    screen.blit(card_image_1, (2, 200))
    screen.blit(card_image_2, (252, 200))
    screen.blit(card_image_3, (502, 200))
    screen.blit(card_image_4, (752, 200))
    screen.blit(card_image_5, (1002, 200))

    pygame.display.flip()

    # # print hand
    # print(hand)

    # # do button clicking until deal button is clicked

    # # buttons will just change held array to 1 or 0 at index of card


    # # deal new cards
    # for i in range(5):
    #     if held[i] == 0:
    #         hand[i] = deck.pop()

    # # idk ui update based off new chards


    # #calculate hand
    # value = funcs.check_hand(hand)

    # # check payout table
    # payout = payouttableDict[value]
    # print("PAYOUTTT:")
    # print(payout)


    # print(funcs.check_hand(hand))
