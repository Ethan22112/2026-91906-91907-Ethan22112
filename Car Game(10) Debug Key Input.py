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
Player_Speed = 2

PLAYER_COLOR = RED


#Instead of putting code directly under when a specific key is pressed, booleans will be used for more control
Player_Up = False
Player_Down = False
Player_Left = False
Player_Right = False


#Initialize The Obstacle Car's Variables
OBSTACLE_CAR_WIDTH = 20
OBSTACLE_CAR_HEIGHT = 10

Obstacle_car_X = FRAME_WIDTH - OBSTACLE_CAR_WIDTH
Obstacle_car_Y = random.randint(0, FRAME_HEIGHT)

OBSTACLE_CAR_COLOR = BLUE
Obstacle_car_speed = random.randint(1, 5)

TOTAL_NUM_OBSTACLE_CARS = 10
obstacle_cars = []


#Setting The Game's Clock & FPS
clock = pygame.time.Clock()
FPS = 60


#Obstacle Car Class - creates one instance of an obstacle car if called
class Obstacle_Car:
    def __init__(self, color, speed, x, y, width, height, ID):

        #sets/instances the current car's variables
        self.Obstacle_car_speed = speed
        self.Obstacle_car_WIDTH = width
        self.Obstacle_car_HEIGHT = height
        self.Obstacle_car_X = x
        self.Obstacle_car_Y = y
        self.Obstacle_car_COLOR = color
        self.ID = ID
        self.rect = pygame.Rect(self.Obstacle_car_X, self.Obstacle_car_Y, self.Obstacle_car_WIDTH, self.Obstacle_car_HEIGHT)
        self.isAlive = True

    #function that controls the movement of the car where if called, the car will move 
    def Go(self):
       self.Obstacle_car_X -= self.Obstacle_car_speed

       if (self.Obstacle_car_X + self.Obstacle_car_WIDTH) < 0:
            self.Obstacle_car_X = FRAME_WIDTH
            self.Obstacle_car_Y = random.randint(0, FRAME_HEIGHT)
            self.Obstacle_car_speed = random.randint(1, 5)
            self.isAlive = True
        
       if self.isAlive == True:
            pygame.draw.rect(WINDOW, self.Obstacle_car_COLOR, (self.Obstacle_car_X, self.Obstacle_car_Y, self.Obstacle_car_WIDTH, self.Obstacle_car_HEIGHT))
            self.rect = pygame.Rect(self.Obstacle_car_X, self.Obstacle_car_Y, self.Obstacle_car_WIDTH, self.Obstacle_car_HEIGHT)
       else:
            self.rect = pygame.Rect(0, 0, 0, 0)

    #function that checks if this car collides with another car(not the player)
    def Check_Collision(self):
        for i in range(0, TOTAL_NUM_OBSTACLE_CARS):
            if obstacle_cars[i].ID != self.ID:
                if self.rect.colliderect(obstacle_cars[i].rect):
                    self.isAlive = False


#Create Multiple Instances Of The Obstacle Car 
for i in range(0, TOTAL_NUM_OBSTACLE_CARS):
    obstacle_car = Obstacle_Car(BLUE, random.randrange(1, 5), random.randrange(FRAME_WIDTH, FRAME_WIDTH * 2), random.randrange(0, FRAME_HEIGHT), OBSTACLE_CAR_WIDTH, OBSTACLE_CAR_HEIGHT, i)
    obstacle_cars.append(obstacle_car)


#Main Game Loop
while not Quit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit_Game = True

    #Setting The Screen To Black Before Drawing The Cars Or Backdrop Again
    WINDOW.fill(BLACK)

    #The code below handles user inputs especially the arrow keys, this controls player movement

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            Player_Up = True
        if event.key == pygame.K_DOWN:
            Player_Down = True
        if event.key == pygame.K_LEFT:
            Player_Left = True
        if event.key == pygame.K_RIGHT:
            Player_Right = True
        
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            Player_Up = False
        if event.key == pygame.K_DOWN:
            Player_Down = False
        if event.key == pygame.K_LEFT:
            Player_Left = False
        if event.key == pygame.K_RIGHT:
            Player_Right = False

    if Player_Up == True:
        if Player_Y >= 0:
           Player_Y -= Player_Speed
        else:
           Player_Y += Player_Speed
           print('crossing top boundary...')
    if Player_Down == True:
        if Player_Y + PLAYER_HEIGHT <= FRAME_HEIGHT:
           Player_Y += Player_Speed
        else:
           Player_Y -= Player_Speed
           print('crossing bottom boundary...')
    if Player_Left == True:
        if Player_X >= 0:
           Player_X -= Player_Speed
        else:
           Player_X += Player_Speed
           print('crossing left boundary...')
    if Player_Right == True:
        if Player_X + PLAYER_WIDTH <= FRAME_WIDTH:
           Player_X += Player_Speed
        else:
           Player_X -= Player_Speed
           print('crossing right boundary...')
 
    #draw a filled rectangle in the screen with the player's specifications
    pygame.draw.rect(WINDOW, PLAYER_COLOR, (Player_X, Player_Y, PLAYER_WIDTH, PLAYER_HEIGHT))

    
    #Call all the instances of the obstacle cars to move
    for i in range(0, TOTAL_NUM_OBSTACLE_CARS):
        obstacle_cars[i].Go()
        obstacle_cars[i].Check_Collision()
   
    #refreshes the screen at a set frame rate
    clock.tick(FPS)

    #refreshes the screen 
    pygame.display.flip()


pygame.quit()
quit()