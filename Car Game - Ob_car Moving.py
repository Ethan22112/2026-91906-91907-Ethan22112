import pygame
import random

#Initializtion Of Pygame
pygame.init()

Quit_Game = False

#Initialize Screen Width And Height
FRAME_WIDTH = 1000
FRAME_HEIGHT = 500


#Initialize Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

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

Obstacle_car_X = FRAME_WIDTH - OBSTACLE_CAR_WIDTH
Obstacle_car_Y = random.randint(0, FRAME_HEIGHT)

OBSTACLE_CAR_COLOR = BLUE
Obstacle_car_speed = random.randint(1, 5)

#Setting The Game's Clock & FPS
clock = pygame.time.Clock()
FPS = 60


#Main Game Loop
while not Quit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit_Game = True

    #Setting The Screen To Black Before Drawing Again
    WINDOW.fill(BLACK)
 
    #draw a filled rectangle in the screen with the player's specifications
    pygame.draw.rect(WINDOW, PLAYER_COLOR, (Player_X, Player_Y, PLAYER_WIDTH, PLAYER_HEIGHT))

    #draw a filled rectangle in the screen with the obstacle car's specifications
    pygame.draw.rect(WINDOW, OBSTACLE_CAR_COLOR, (Obstacle_car_X, Obstacle_car_Y, OBSTACLE_CAR_WIDTH, OBSTACLE_CAR_HEIGHT))
    Obstacle_car_X -= Obstacle_car_speed

    if (Obstacle_car_X + OBSTACLE_CAR_WIDTH) < 0:
        Obstacle_car_X = FRAME_WIDTH
        Obstacle_car_Y = random.randint(0, FRAME_HEIGHT)
        Obstacle_car_speed = random.randint(1, 5)
   
    #refreshes the screen at a set frame rate
    clock.tick(FPS)

    #refreshes the screen 
    pygame.display.flip()


pygame.quit()
quit()