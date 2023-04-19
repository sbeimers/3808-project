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

# Make transparent
held1.set_alpha(0)
held2.set_alpha(0)
held3.set_alpha(0)
held4.set_alpha(0)
held5.set_alpha(0)

credit_label = font.render("Credits: " + str(credits), True, (255, 255, 255))
bet_label = font.render("Bet: " + str(bet), True, (255, 255, 255))

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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hold1.collidepoint(event.pos):
                if game_state == "first_hand":
                    held[0] = 1 if held[0] == 0 else 0   
                    #add the ui the show that its held 
                print("Button 1 clicked")
            elif hold2.collidepoint(event.pos):
                if game_state == "first_hand":
                    held[1] = 1 if held[1] == 0 else 0   
                    #add the ui the show that its held 
                print("Button 2 clicked")
            elif hold3.collidepoint(event.pos):
                if game_state == "first_hand":
                    held[2] = 1 if held[2] == 0 else 0   
                    #add the ui the show that its held 
                print("Button 3 clicked")
            elif hold4.collidepoint(event.pos):
                if game_state == "first_hand":
                    held[3] = 1 if held[3] == 0 else 0   
                    #add the ui the show that its held 
                print("Button 4 clicked")
            elif hold5.collidepoint(event.pos):
                if game_state == "first_hand":
                    held[4] = 1 if held[4] == 0 else 0   
                    #add the ui the show that its held 
                print("Button 5 clicked")
            elif increase_bet.collidepoint(event.pos):
                if game_state == "betting" and bet < 5:
                    bet += 1
                print("Increase bet clicked")
            elif decrease_bet.collidepoint(event.pos):
                if game_state == "betting" and bet > 1:
                    bet -= 1
                print("Decrease bet clicked")
            elif deal.collidepoint(event.pos):
                if game_state == "betting":
                    credits -= bet
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
                    
                    game_state = "first_hand"
                else:
                    # hold cards
                    for i in range(5):
                        if held[i] == 0:
                            hand[i] = deck.pop()
                    print(hand[0])
                    card_image_1 = pygame.transform.scale(pygame.image.load("card_images/" + hand[0].file_name()), (250, 363))
                    card_image_2 = pygame.transform.scale(pygame.image.load("card_images/" + hand[1].file_name()), (250, 363))
                    card_image_3 = pygame.transform.scale(pygame.image.load("card_images/" + hand[2].file_name()), (250, 363))
                    card_image_4 = pygame.transform.scale(pygame.image.load("card_images/" + hand[3].file_name()), (250, 363))
                    card_image_5 = pygame.transform.scale(pygame.image.load("card_images/" + hand[4].file_name()), (250, 363))
                    
                    
                    # calculate hand value
                    value = funcs.check_hand(hand)


                    # check payout table
                    payouthand = [payoutTable[value]]
                    print (hand)
                    print (payouthand)
                    payout = payouthand[0][bet]

                    print("PAYOUTTT:")
                    print(payout)

                    credits += payout
                    game_state = "betting"
                print("Deal clicked")
    # do button clicking until deal button is clicked

    # Clear the screen
    screen.fill((255, 255, 255))

    screen.blit(background_image, (0, 0))

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

    # Draw credit label
    screen.blit(credit_label, (100, 100))

    # Draw bet label
    screen.blit(bet_label, (100, 150))


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


    # uncomment these once loop isn't infinite:
    ############################################### 
    # check payout table
    # payouthand = [payoutTable[value]]
    # print (hand)
    # print (payouthand)
    # payout = payouthand[0][bet]

    # print("PAYOUTTT:")
    # print(payout)
    ############################################### 
