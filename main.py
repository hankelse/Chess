import pygame, sys, random
from pygame.locals import *
import game_objects as gobs
import peices
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Pygame Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

#Game Setup
board = gobs.Grid()
peice = peices.Peice("8")

 

def main () :

    running = True


    while running :
        WINDOW.fill(BACKGROUND)
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
     
    
        pygame.display.update()
        fpsClock.tick(FPS)
#  main()

board.console_display()
board.add(3, "A", peice)
print(" ")
board.console_display()

board.move(3, "A")
print(" ")
board.console_display()