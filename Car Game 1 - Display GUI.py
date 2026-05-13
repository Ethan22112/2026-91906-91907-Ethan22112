import pygame
import time

#Initializtion Of Pygame
pygame.init()

Quit_Game = False

#Initialize Screen Width And Height
FRAME_WIDTH = 1000
FRAME_HEIGHT = 500

RED = (255, 0, 0)

#Initialize Window And Title
WINDOW = pygame.display.set_mode((FRAME_WIDTH, FRAME_HEIGHT))
pygame.display.set_caption("Street Racer")


#Initialize The Player's car variables
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 10

Player_X = FRAME_WIDTH / 2
Player_Y = FRAME_HEIGHT / 2

PLAYER_COLOR = RED


#Main Game Loop
while not Quit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit_Game = True
 
        #draw a filled rectangle in the screen with the player's specifications
        pygame.draw.rect(WINDOW, RED, (Player_X, Player_Y, PLAYER_WIDTH, PLAYER_HEIGHT))

        #refreshes the screen 
        pygame.display.flip()


pygame.quit()
quit()