# MATH3808 Final Project - Video Poker
# Authors: Elias Hawa, Sebastian Beimers, Victor Li

import pygame

from card import Card
import funcs as funcs
import random

payoutTable = { 
    1: 
    {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
    2:
    {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
    3:
    {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
    4:
    {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
    5:
    {1: 4, 2: 8, 3: 12, 4: 16, 5: 20},
    6:
    {1: 6, 2: 12, 3: 18, 4: 24, 5: 30},
    7:
    {1: 9, 2: 18, 3: 27, 4: 36, 5: 45},
    8:
    {1: 25, 2: 50, 3: 75, 4: 100, 5: 125},
    9:
    {1: 50, 2: 100, 3: 150, 4: 200, 5: 250},
    10:
    {1: 250, 2: 500, 3: 750, 4: 1000, 5: 4000}
}

bet = 1 #goes from 1-5
credits = 1000
game_state = "betting"

# game states: betting, first_hand
# betting -> no holding, can bet, can deal
# first_hand -> can hold, cannot bet, can deal

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
font = pygame.font.SysFont("Arial", 40)

# Load 5 buttons
hold1 = pygame.Rect(2, 200, 250, 363)
hold2 = pygame.Rect(252, 200, 250, 363)
hold3 = pygame.Rect(502, 200, 250, 363)
hold4 = pygame.Rect(752, 200, 250, 363)
hold5 = pygame.Rect(1002, 200, 250, 363)

# 5 labels for text
held1 = font.render("HELD", True, (255, 255, 255, 0))
held2 = font.render("HELD", True, (255, 255, 255))
held3 = font.render("HELD", True, (255, 255, 255))
held4 = font.render("HELD", True, (255, 255, 255))
held5 = font.render("HELD", True, (255, 255, 255))

# 2 lables for bet + and bet -
bet_plus = font.render("Bet Up", True, (255, 255, 255))
bet_minus = font.render("Bet Down", True, (255, 255, 255))

# 1 label for deal
deal_label = font.render("Deal", True, (255, 255, 255))

# Make transparent
held1.set_alpha(0)
held2.set_alpha(0)
held3.set_alpha(0)
held4.set_alpha(0)
held5.set_alpha(0)

credit_label = font.render("Credits: " + str(credits), True, (255, 255, 255))
bet_label = font.render("Bet: " + str(bet), True, (255, 255, 255))

increase_bet = pygame.Rect(45, 587, 200, 50)
decrease_bet = pygame.Rect(45, 637, 200, 50)
deal = pygame.Rect(300, 610, 150, 50)
win_label = font.render("Winner Label", True, (255, 255, 255))
win_label.set_alpha(0)

# pygame functions to draw the pay table
def draw_pay_table():
    pygame.draw.rect(screen, (255, 255, 255), (10, 5, 565, 190), 5)
    font = pygame.font.SysFont("Arial", 18)

    # Win types
    screen.blit(font.render("ROYAL FLUSH", True, (255, 255, 255)), (20, 10))
    screen.blit(font.render("STRAIGHT FLUSH", True, (255, 255, 255)), (20, 30))
    screen.blit(font.render("4 OF A KIND", True, (255, 255, 255)), (20, 50))
    screen.blit(font.render("FULL HOUSE", True, (255, 255, 255)), (20, 70))
    screen.blit(font.render("FLUSH", True, (255, 255, 255)), (20, 90))
    screen.blit(font.render("STRAIGHT", True, (255, 255, 255)), (20, 110))
    screen.blit(font.render("3 OF A KIND", True, (255, 255, 255)), (20, 130))
    screen.blit(font.render("TWO PAIR", True, (255, 255, 255)), (20, 150))
    screen.blit(font.render("JACKS OR BETTER", True, (255, 255, 255)), (20, 170))

    pygame.draw.line(screen, (255, 255, 255), (200, 5), (200, 190), 5)

    # Payoff for 1 betting unit
    screen.blit(font.render("250", True, (255, 255, 255)), (244, 10))
    screen.blit(font.render("50", True, (255, 255, 255)), (253, 30))
    screen.blit(font.render("25", True, (255, 255, 255)), (253, 50))
    screen.blit(font.render("9", True, (255, 255, 255)), (260, 70))
    screen.blit(font.render("6", True, (255, 255, 255)), (260, 90))
    screen.blit(font.render("4", True, (255, 255, 255)), (260, 110))
    screen.blit(font.render("3", True, (255, 255, 255)), (260, 130))
    screen.blit(font.render("2", True, (255, 255, 255)), (260, 150))
    screen.blit(font.render("1", True, (255, 255, 255)), (260, 170))
    
    pygame.draw.line(screen, (255, 255, 255), (275, 5), (275, 190), 5)

    # Payoff for 2 betting units
    screen.blit(font.render("500", True, (255, 255, 255)), (319, 10))
    screen.blit(font.render("100", True, (255, 255, 255)), (319, 30))
    screen.blit(font.render("50", True, (255, 255, 255)), (327, 50))
    screen.blit(font.render("18", True, (255, 255, 255)), (327, 70))
    screen.blit(font.render("12", True, (255, 255, 255)), (327, 90))
    screen.blit(font.render("8", True, (255, 255, 255)), (335, 110))
    screen.blit(font.render("6", True, (255, 255, 255)), (335, 130))
    screen.blit(font.render("4", True, (255, 255, 255)), (335, 150))
    screen.blit(font.render("2", True, (255, 255, 255)), (335, 170))

    pygame.draw.line(screen, (255, 255, 255), (350, 5), (350, 190), 5)

    # Payoff for 3 betting units
    screen.blit(font.render("750", True, (255, 255, 255)), (394, 10))
    screen.blit(font.render("150", True, (255, 255, 255)), (394, 30))
    screen.blit(font.render("75", True, (255, 255, 255)), (402, 50))
    screen.blit(font.render("27", True, (255, 255, 255)), (402, 70))
    screen.blit(font.render("18", True, (255, 255, 255)), (402, 90))
    screen.blit(font.render("12", True, (255, 255, 255)), (402, 110))
    screen.blit(font.render("9", True, (255, 255, 255)), (410, 130))
    screen.blit(font.render("6", True, (255, 255, 255)), (410, 150))
    screen.blit(font.render("3", True, (255, 255, 255)), (410, 170))

    pygame.draw.line(screen, (255, 255, 255), (425, 5), (425, 190), 5)

    # Payoff for 4 betting units
    screen.blit(font.render("1000", True, (255, 255, 255)), (461, 10))
    screen.blit(font.render("200", True, (255, 255, 255)), (469, 30))
    screen.blit(font.render("100", True, (255, 255, 255)), (469, 50))
    screen.blit(font.render("36", True, (255, 255, 255)), (477, 70))
    screen.blit(font.render("24", True, (255, 255, 255)), (477, 90))
    screen.blit(font.render("16", True, (255, 255, 255)), (477, 110))
    screen.blit(font.render("12", True, (255, 255, 255)), (477, 130))
    screen.blit(font.render("8", True, (255, 255, 255)), (485, 150))
    screen.blit(font.render("4", True, (255, 255, 255)), (485, 170))

    pygame.draw.line(screen, (255, 255, 255), (500, 5), (500, 190), 5)

    # Payoff for 5 betting units
    screen.blit(font.render("4000", True, (255, 255, 255)), (536, 10))
    screen.blit(font.render("250", True, (255, 255, 255)), (544, 30))
    screen.blit(font.render("125", True, (255, 255, 255)), (544, 50))
    screen.blit(font.render("45", True, (255, 255, 255)), (552, 70))
    screen.blit(font.render("30", True, (255, 255, 255)), (552, 90))
    screen.blit(font.render("20", True, (255, 255, 255)), (552, 110))
    screen.blit(font.render("15", True, (255, 255, 255)), (552, 130))
    screen.blit(font.render("10", True, (255, 255, 255)), (552, 150))
    screen.blit(font.render("5", True, (255, 255, 255)), (560, 170))

def draw_components():
    # Draw buttons
    pygame.draw.rect(screen, (0, 0, 0), hold1)
    pygame.draw.rect(screen, (0, 0, 0), hold2)
    pygame.draw.rect(screen, (0, 0, 0), hold3)
    pygame.draw.rect(screen, (0, 0, 0), hold4)
    pygame.draw.rect(screen, (0, 0, 0), hold5)
    pygame.draw.rect(screen, (0, 255, 0), increase_bet)
    pygame.draw.rect(screen, (255, 0, 0), decrease_bet)
    pygame.draw.rect(screen, (0, 0, 255), deal)

    # Draw images
    screen.blit(card_image_1, (2, 200))
    screen.blit(card_image_2, (252, 200))
    screen.blit(card_image_3, (502, 200))
    screen.blit(card_image_4, (752, 200))
    screen.blit(card_image_5, (1002, 200))

    # Draw labels
    screen.blit(held1, (88, 150))
    screen.blit(held2, (336, 150))
    screen.blit(held3, (584, 150))
    screen.blit(held4, (832, 150))
    screen.blit(held5, (1080, 150))
    screen.blit(bet_plus, (80, 587))
    screen.blit(bet_minus, (55, 637))
    screen.blit(deal_label, (330, 610))
    screen.blit(win_label, (500, 600))

    # Draw credit label
    screen.blit(credit_label, (1000, 587))

    # Draw bet label
    screen.blit(bet_label, (1000, 637))

def create_new_deck():
    deck = []
    for suit in ["H", "D", "C", "S"]:
        for value in range(2, 15): #2-14
            deck.append(Card(suit, value))
    return deck

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hold1.collidepoint(event.pos):
                if game_state == "first_hand":
                    if held[0] == 0:
                        held[0] = 1
                        held1.set_alpha(255)
                    else:
                        held[0] = 0
                        held1.set_alpha(0)
            elif hold2.collidepoint(event.pos):
                if game_state == "first_hand":
                    if held[1] == 0:
                        held[1] = 1
                        held2.set_alpha(255)
                    else:
                        held[1] = 0
                        held2.set_alpha(0) 
            elif hold3.collidepoint(event.pos):
                if game_state == "first_hand":
                    if held[2] == 0:
                        held[2] = 1
                        held3.set_alpha(255)
                    else:
                        held[2] = 0
                        held3.set_alpha(0)
            elif hold4.collidepoint(event.pos):
                if game_state == "first_hand":
                    if held[3] == 0:
                        held[3] = 1
                        held4.set_alpha(255)
                    else:
                        held[3] = 0
                        held4.set_alpha(0) 
            elif hold5.collidepoint(event.pos):
                if game_state == "first_hand":
                    if held[4] == 0:
                        held[4] = 1
                        held5.set_alpha(255)
                    else:
                        held[4] = 0
                        held5.set_alpha(0)
            elif increase_bet.collidepoint(event.pos):
                if game_state == "betting" and bet < 5:
                    bet += 1
                    bet_label = font.render("Bet: " + str(bet), True, (255, 255, 255))
            elif decrease_bet.collidepoint(event.pos):
                if game_state == "betting" and bet > 1:
                    bet -= 1
                    bet_label = font.render("Bet: " + str(bet), True, (255, 255, 255))
            elif deal.collidepoint(event.pos):
                if game_state == "betting":
                    credits -= bet
                    credit_label = font.render("Credits: " + str(credits), True, (255, 255, 255))
                    # create deck
                    deck = create_new_deck()

                    # shuffle deck
                    random.shuffle(deck)

                    # deal 5 cards
                    hand = []
                    for i in range(5):
                        hand.append(deck.pop())
                    held = [0,0,0,0,0]
                    card_image_1 = pygame.transform.scale(pygame.image.load("card_images/" + hand[0].file_name()), (250, 363))
                    card_image_2 = pygame.transform.scale(pygame.image.load("card_images/" + hand[1].file_name()), (250, 363))
                    card_image_3 = pygame.transform.scale(pygame.image.load("card_images/" + hand[2].file_name()), (250, 363))
                    card_image_4 = pygame.transform.scale(pygame.image.load("card_images/" + hand[3].file_name()), (250, 363))
                    card_image_5 = pygame.transform.scale(pygame.image.load("card_images/" + hand[4].file_name()), (250, 363))
                    
                    win_label.set_alpha(0)
                    game_state = "first_hand"
                else:
                    # hold cards
                    for i in range(5):
                        if held[i] == 0:
                            hand[i] = deck.pop()
                    card_image_1 = pygame.transform.scale(pygame.image.load("card_images/" + hand[0].file_name()), (250, 363))
                    card_image_2 = pygame.transform.scale(pygame.image.load("card_images/" + hand[1].file_name()), (250, 363))
                    card_image_3 = pygame.transform.scale(pygame.image.load("card_images/" + hand[2].file_name()), (250, 363))
                    card_image_4 = pygame.transform.scale(pygame.image.load("card_images/" + hand[3].file_name()), (250, 363))
                    card_image_5 = pygame.transform.scale(pygame.image.load("card_images/" + hand[4].file_name()), (250, 363))
                    
                    
                    # calculate hand value
                    value = funcs.check_hand(hand)


                    # check payout table
                    payouthand = [payoutTable[value]]
                    payout = payouthand[0][bet]

                    credits += payout
                    credit_label = font.render("Credits: " + str(credits), True, (255, 255, 255))

                    held1.set_alpha(0)
                    held2.set_alpha(0)
                    held3.set_alpha(0)
                    held4.set_alpha(0)
                    held5.set_alpha(0)

                    win_label.set_alpha(255)
                    win_label = font.render(funcs.convertNumberToWinner(value), True, (255, 255, 255))

                    game_state = "betting"
    # do button clicking until deal button is clicked

    # Clear the screen
    screen.fill((255, 255, 255))

    screen.blit(background_image, (0, 0))

    # Draw pay scale selector
    pygame.draw.rect(screen, (128, 0, 32), pygame.Rect(125 + (75 * bet), 5, 75, 190))

    # Draw pay table
    draw_pay_table()

    # Draw buttons, images and labels
    draw_components()

    pygame.display.flip()