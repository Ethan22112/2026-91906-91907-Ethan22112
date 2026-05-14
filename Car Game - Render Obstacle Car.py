import pygame
import time

#Initializtion Of Pygame
pygame.init()

Quit_Game = False

#Initialize Screen Width And Height
FRAME_WIDTH = 1000
FRAME_HEIGHT = 500


#Initialize Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Initialize Window And Title
WINDOW = pygame.display.set_mode((FRAME_WIDTH, FRAME_HEIGHT))
pygame.display.set_caption("Street Racer")


#Initialize The Player's car variables
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 10

Player_X = FRAME_WIDTH / 2
Player_Y = FRAME_HEIGHT / 2

PLAYER_COLOR = RED


#Initialize The Obstacle Car's Variables
OBSTACLE_CAR_WIDTH = 20
OBSTACLE_CAR_HEIGHT = 10

Obstacle_car_X = 0
Obstacle_car_Y = 0

OBSTACLE_CAR_COLOR = BLUE


#Main Game Loop
while not Quit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit_Game = True
 
        #draw a filled rectangle in the screen with the player's specifications
        pygame.draw.rect(WINDOW, PLAYER_COLOR, (Player_X, Player_Y, PLAYER_WIDTH, PLAYER_HEIGHT))

        #draw a filled rectangle in the screen with the obstacle car's specifications
        pygame.draw.rect(WINDOW, OBSTACLE_CAR_COLOR, (Obstacle_car_X, Obstacle_car_Y, OBSTACLE_CAR_WIDTH, OBSTACLE_CAR_HEIGHT))
       

        #refreshes the screen 
        pygame.display.flip()


pygame.quit()
quit()