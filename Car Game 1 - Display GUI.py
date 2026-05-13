import pygame
import time

#Initializtion Of Pygame
pygame.init()

Quit_Game = False

#Initialize Screen Width And Height
FRAME_WIDTH = 1000
FRAME_HEIGHT = 500

#Initialize Window And Title
WINDOW = pygame.display.set_mode((FRAME_WIDTH, FRAME_HEIGHT))
pygame.display.set_caption("Street Racer")

#Main Game Loop
while not Quit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit_Game = True


pygame.quit()
quit()