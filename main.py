#!/usr/bin/python -tt
import numpy
import pygame
import sys
import os
from char import character
from menus import InstMenu
from pygame.locals import *




fpsClock = pygame.time.Clock()

windowWi = 860+67
windowHi = 500

mapWi = 43 
mapHi = 25

screen = pygame.display.set_mode((windowWi, windowHi))
pygame.display.set_caption("Game Sampling!")

# ----- project path ------------------------------

mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))

# ----- image dictonaries ------------------------------

tile_dict = {
			 1 : pygame.image.load(mainPath + "\\gfx\\grass.png"),
            }

#-------------------------------------------------------

gameRunning = True
menuIsActive = [False]
thisMenu = [None]

groundArray = numpy.ones((mapWi,mapHi))

def getInputSetValues():
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit(); sys.exit();
    if menuIsActive[0] == True:
     	nextAction = str(thisMenu[0].useMenu(CUR, event))
     	print nextAction
      	if nextAction == "Move":
            CUR.setSprite("cursorMV")
            CUR.setLocation(charPlayer.getX(), charPlayer.getY(), "map")
        elif nextAction == "end" or nextAction == "Wait":
            menuIsActive[0] = False
            CUR.setSprite("cursor")
            CUR.setLocation(charPlayer.getX(), charPlayer.getY(),"map")
    else:
        getMapInput(event)


def getMapInput(event):
    if event.type == KEYDOWN and event.key == K_UP:
       	CUR.setLocation(CUR.getX(), CUR.getY() - 1, "map")
    elif event.type == KEYDOWN and event.key == K_DOWN:
       	CUR.setLocation(CUR.getX(), CUR.getY() + 1, "map")
    elif event.type == KEYDOWN and event.key == K_LEFT:
       	CUR.setLocation(CUR.getX() - 1, CUR.getY(), "map")
    elif event.type == KEYDOWN and event.key == K_RIGHT:
       	CUR.setLocation(CUR.getX() + 1, CUR.getY(), "map")
    elif event.type == KEYDOWN and event.key == K_z:
       	if CUR.getLocation() == charPlayer.getLocation():
        	menuIsActive[0] = True
        	thisMenu[0] = InstMenu(charPlayer, "baseMenu", mapWi, mapHi)
    		CUR.setSprite("menuItemSelect")
    		CUR.setLocation(mapWi, 0,"map")

        	

def updateDisplay():
	drawMapArray(groundArray)
	if thisMenu[0] != None:
		thisMenu[0].printMenu()
	screen.blit(charPlayer.getSprite(),charPlayer.getLocation())
	screen.blit(CUR.getSprite(),CUR.getLocation())
	return

def drawMapArray(maparray):
    for x in xrange(0, mapWi):
        for y in xrange(0, mapHi):
            # Determines tile type.
            current_tile = tile_dict[maparray[x, y]]
            screen.blit(current_tile, (x*20, y*20))
    return

drawMapArray(groundArray)

charPlayer = character("player")
charPlayer.setLocation((mapWi) - 1 , (mapHi) - 1, "map")
screen.blit(charPlayer.getSprite(),charPlayer.getLocation())
CUR = character("cursor")
CUR.setLocation((mapWi) - 1 , (mapHi) - 1, "map")
screen.blit(CUR.getSprite(),CUR.getLocation())

while gameRunning:
	getInputSetValues()
	updateDisplay()
	#Updates display and then sets FPS to 30 FPS. 
	pygame.display.update()
	fpsClock.tick(30)

pygame.quit()



