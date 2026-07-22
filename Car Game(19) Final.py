import pygame
import random

import pygame.freetype

#Initializtion Of Pygame
pygame.init()

Quit_Game = False
FONT_SIZE = 12

#Initialize Screen Width And Height
FRAME_WIDTH = 1000
FRAME_HEIGHT = 500

Instructions = True


#Initialize Colors 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#Initialize Window And Title
WINDOW = pygame.display.set_mode((FRAME_WIDTH, FRAME_HEIGHT))
pygame.display.set_caption("Street Racer")


#Background Tile Variables
tiles = []

#Initialize The Player's car variables
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 10

Player_X = FRAME_WIDTH / 2
Player_Y = FRAME_HEIGHT / 2
Player_Speed = 2

PLAYER_SPRITE = pygame.image.load("Sprites & Tiles/Blue Car Updated(1).png").convert_alpha()
Player_rect = pygame.Rect(Player_X, Player_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
Player_isalive = True

PLAYER_ANGLE = 10

PLAYER_TURN_LEFT = pygame.transform.rotate(PLAYER_SPRITE, PLAYER_ANGLE)
PLAYER_TURN_RIGHT = pygame.transform.rotate(PLAYER_SPRITE, -(PLAYER_ANGLE))

points = 0

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

OBSTACLE_CAR_SPRITE = pygame.image.load("Sprites & Tiles/Red car Updated(1).png").convert_alpha()
Obstacle_car_speed = random.randint(1, 5)

MAX_NUM_OBSTACLE_CARS = 120
TOTAL_NUM_OBSTACLE_CARS = 0
obstacle_cars = []

SPAWN_TIME = 5
SpawnTick = 0


#Initialize Background Variables
ROAD_TILE = pygame.image.load("Sprites & Tiles/Road.png").convert_alpha()
ROAD_WIDTH = ROAD_TILE.get_width()
ROAD_HEIGHT = ROAD_TILE.get_height()


#Setting The Game's Clock & FPS
clock = pygame.time.Clock()
FPS = 60
FrameTick = 0

#Loads, compares and updates the current high score 
def Load_High_Score():
    try:
        high_score_file = open("score", "r")
        if points >= int(high_score_file.read()):
            high_score_file = open("score", "w")
            high_score_file.write(str(points))
    except:
        high_score_file = open("score", "w")
        high_score_file.write("0")
        
    high_score_file = open("score", "r")
    value = high_score_file.read()
    high_score_file.close()

    return value

#Function for displaying text
def Render_Box(Text, Primary_Color, Background_Color, PositionX, PositionY):
    font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
    Display = font.render(Text, True, Primary_Color, Background_Color)
    Text_Box = Display.get_rect(center = (PositionX, PositionY))
    WINDOW.blit(Display, Text_Box)

#Background Tile Class - creates one instance of a background tile if called
class Background_Tile:
    def __init__(self, x, y, speed, size, image):

        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.image = image

    def Go(self):
        self.x -= self.speed
        WINDOW.blit(self.image, (self.x, self.y))

        #Check if this current tile exceeds the left side of the screen, if so, then return to the far right of the screen
        #This creates the illusion that the road is infinite
        if self.x <= -(ROAD_WIDTH):
            self.x = FRAME_WIDTH


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
        
        # checks if the current car is still "alive", will continue to do as intended if so, will get "disabled" if not 
        if self.isAlive == True:
            WINDOW.blit(OBSTACLE_CAR_SPRITE, (self.Obstacle_car_X, self.Obstacle_car_Y))
            self.rect = pygame.Rect(self.Obstacle_car_X, self.Obstacle_car_Y, self.Obstacle_car_WIDTH, self.Obstacle_car_HEIGHT)
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)

    #function that iterates through the entire collection of obstacle cars, and checks if this car's bounding box collides with any of them.
    def Check_Collision(self):
        for i in range(0, len(obstacle_cars)):
            if obstacle_cars[i].ID != self.ID:
                if self.rect.colliderect(obstacle_cars[i].rect):
                    self.isAlive = False


#Create Multiple Instances Of Background Tiles using a for loop, assigning the desired x and y locations for each tile 
for x in range(0, round(FRAME_WIDTH / ROAD_WIDTH) + ROAD_WIDTH):
    for y in range(0, round(FRAME_HEIGHT / ROAD_HEIGHT)):
        tile = Background_Tile(x * ROAD_WIDTH, y * ROAD_HEIGHT, 10, ROAD_WIDTH, ROAD_TILE)
        tiles.append(tile)


#Create Multiple Instances Of The Obstacle Car using a for loop 
for i in range(0, TOTAL_NUM_OBSTACLE_CARS):
    obstacle_car = Obstacle_Car(BLUE, random.randrange(1, 5), random.randrange(FRAME_WIDTH, FRAME_WIDTH * 2), random.randrange(0, FRAME_HEIGHT), OBSTACLE_CAR_WIDTH, OBSTACLE_CAR_HEIGHT, i)
    obstacle_cars.append(obstacle_car)


#Main Game Loop
while not Quit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit_Game = True

    #Calls method 'Load_High_Score'
    high_score = Load_High_Score()

    #Setting The Screen To Black Before Drawing The Cars Or Background Again
    WINDOW.fill(BLACK)

    #Calling every background tile to move 
    for i in range(0, len(tiles)):
        tiles[i].Go()
    
    #The code below handles user inputs, especially the arrow keys. this controls player movement
    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            Player_Up = True
        if event.key == pygame.K_DOWN:
            Player_Down = True
        if event.key == pygame.K_LEFT:
            Player_Left = True
        if event.key == pygame.K_RIGHT:
            Player_Right = True
        #Removes Instructions Text Once The First Key Is Pressed
        if Instructions == True:
            Instructions = False
        
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            Player_Up = False
        if event.key == pygame.K_DOWN:
            Player_Down = False
        if event.key == pygame.K_LEFT:
            Player_Left = False
        if event.key == pygame.K_RIGHT:
            Player_Right = False

    #Checks if each key of movement (Arrow keys) are active or not. This prevents issues caused by pressing or releasing two or more keys at the same time.
    if Player_Up == True:
        if not keys[pygame.K_UP]:
           Player_Up = False
        else:
           if Player_Y >= 0:
              Player_Y -= Player_Speed
    if Player_Down == True:
        if not keys[pygame.K_DOWN]:
            Player_Down = False
        else:
           if Player_Y + PLAYER_HEIGHT <= FRAME_HEIGHT:
              Player_Y += Player_Speed
    if Player_Left == True:
        if not keys[pygame.K_LEFT]:
            Player_Left = False
        else:
           if Player_X >= 0:
              Player_X -= Player_Speed
    if Player_Right == True:
        if not keys[pygame.K_RIGHT]:
            Player_Right = False
        else:
           if Player_X + PLAYER_WIDTH <= FRAME_WIDTH:
              Player_X += Player_Speed

    #executes the code under the if statement, if, the player has not crashed into other cars.
    if Player_isalive == True:

       #update the player's 'rectangle' that detects collision
       Player_rect = pygame.Rect(Player_X, Player_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
 
       #draw the player's car
       if Player_Up == True:
           WINDOW.blit(PLAYER_TURN_LEFT, (Player_X, Player_Y))
       elif Player_Down == True:
           WINDOW.blit(PLAYER_TURN_RIGHT, (Player_X, Player_Y))
       else:
           WINDOW.blit(PLAYER_SPRITE, (Player_X, Player_Y))

       for i in range(0, len(obstacle_cars)):
           if Player_rect.colliderect(obstacle_cars[i]):
              Player_isalive = False
    else:
        Player_rect = pygame.Rect(0, 0, 0, 0)

    
    #Call all the instances of the obstacle cars to move
    for i in range(0, len(obstacle_cars)):
        obstacle_cars[i].Go()
        obstacle_cars[i].Check_Collision()
    
    #if the player hasn't crashed yet, check if the clock has reached a full second to update player points
    if(Player_isalive) and  not Instructions:
        FrameTick += 1
        if FrameTick >= FPS:
            points += 10
            FrameTick = 0
            """Variable 'SpawnTick' increases by 1 if 1 second has passed, if this variable is greater than or equates to 10, or 10 seconds
            , another obstacle car will be added to the game, essentially, another obstacle car gets added every 10 seconds"""
            SpawnTick += 1
            if SpawnTick >= SPAWN_TIME:
                SpawnTick = 0
                #If the current number of obstacle cars is less than the total (100), add another obstacle car in the game.
                if (len(obstacle_cars) >= TOTAL_NUM_OBSTACLE_CARS):
                    obstacle_cars.append(Obstacle_Car(BLUE, random.randrange(1, 5), random.randrange(FRAME_WIDTH, FRAME_WIDTH * 2), random.randrange(0, FRAME_HEIGHT), OBSTACLE_CAR_WIDTH, OBSTACLE_CAR_HEIGHT, i))

        #Display Score
        Render_Box(("Player Points "+ str(points) + ",  High Score "+ str(high_score)), WHITE, BLACK, 110, 10)

    elif not Player_isalive:
        #Display Game Over Text
        Render_Box(("Game Over! Your Points: "+str(points)+",  High Score: "+str(high_score)), WHITE, BLACK, FRAME_WIDTH / 2, FRAME_HEIGHT / 2)

    if Instructions == True:
        #Display Instructions
        Render_Box("Arrow Keys To Move!", WHITE, BLACK, FRAME_WIDTH / 2, FRAME_HEIGHT / 2)
       
    #refresh the screen at a set frame rate
    clock.tick(FPS)

    #refreshes the screen 
    pygame.display.flip()


pygame.quit()
quit()