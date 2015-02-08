#!/usr/bin/python -t
import sys
import os
import pygame
from char import character
from pygame import display
from pygame.locals import *
import numpy

# ----- project path ------------------------------

class InstMenu():

	pygame.init()

	mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))

	menuCurrentLocation = 0
	menuName = ""
	charName = ""
	mapWi = 0
	mapHi = 0

	baseMenu = [
		"Move",
		"Attack",
		"Wait"
		]

	currentMenu = []

	def __init__(self, charMenu, menuName, mapWi, mapHi):
		
		self.mapWi = mapWi
		self.mapHi = mapHi

		if menuName != "baseMenu":
			print "notDefault"
		else:
		    self.menuName = menuName
		    self.currentMenu = self.baseMenu

		self.printMenu()
		return

	def printMenu(self):

		from pygame import Color, font

		menuBG = pygame.image.load(self.mainPath + "\\gfx\\menuItem.png")

		pygame.init()
		bg_color = Color('grey')
		hi_color = Color(155,155,155)
		text_color = Color('black')
		glint_color = Color(220,220,220)
		shadow_color = Color(105,105,105)
		font = pygame.font.SysFont(None, 25)

		screen = pygame.display.get_surface()

		menuNum = 0
		for menuText in self.currentMenu:
			menuItem = font.render(menuText, True, text_color)
			screen.blit(menuBG, (self.mapWi*20, menuNum))
			screen.blit(menuItem, (self.mapWi*20 + 7, 4 + (menuNum)))
			menuNum += 25

		return

	def useMenu(self, CUR, event):
	    menuCurrentLocation = 0
	    if event.type == KEYDOWN and event.key == K_UP:
	    	if self.menuCurrentLocation - 1 > -1:
	        	CUR.setLocation(CUR.getX(), +1,"menu")
	        	self.menuCurrentLocation -= 1
	    elif event.type == KEYDOWN and event.key == K_DOWN:
	    	if self.menuCurrentLocation + 1 < self.currentMenu.__len__():
	        	CUR.setLocation(CUR.getX(), -1,"menu")
	        	self.menuCurrentLocation += 1
	    elif event.type == KEYDOWN and event.key == K_z:
	        return self.currentMenu[self.menuCurrentLocation]
	    elif event.type == KEYDOWN and event.key == K_x:
	    	return "end"



