import numpy
import pygame
import sys
import os
#import char
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

windowWi = 860
windowHi = 500

mapWi = 43 
mapHi = 25

# ----- project path ------------------------------

mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))

# ----- image dictonaries ------------------------------

tile_dict = {
			 1 : pygame.image.load(mainPath + "\\gfx\\grass.png"),
            }

sprite_dict = {
			   1 : pygame.image.load(mainPath + "\\gfx\\player.png")
			  }


#-------------------------------------------------------
screen = pygame.display.set_mode((windowWi, windowHi))
pygame.display.set_caption("Game Sampling!")

gameRunning = True

groundArray = numpy.ones((mapWi,mapHi))

def drawMapArray(maparray):
    for x in xrange(0, mapWi):
        for y in xrange(0, mapHi):
            # Determines tile type.
            current_tile = tile_dict[maparray[x, y]]
            screen.blit(current_tile, (x*20, y*20))
    return

def drawSpritesInit():
	screen.blit(sprite_dict[1], ((mapWi * 20) - 20, (mapHi * 20) - 20))
	return

def moveSprite():
	return

def moveSprite(x1,y1,mvx,mvy):
	return

drawMapArray(groundArray)
drawSpritesInit()

while gameRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
            break

    #Updates display and then sets FPS to 30 FPS. 
    pygame.display.update()
    fpsClock.tick(30)

pygame.quit()



