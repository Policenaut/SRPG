import os
import sys
import pygame
from pygame import sprite

class character():

	'''
	# 
	hp = 0.0
	mp = 0.0
	mvt = 3
	atk = 0.0
	mgk = 0.0
	defe = 0.0
	res = 0.0
	currentX = 0
	currentY = 0
	select = False
	#
	'''
	def setSprite(self, filename):
		self.spriteFileName = "\\gfx\\"+str(filename)+".png"
		return

	def __init__(self, sprite):
		self.spriteFileName = "\\gfx\\"+str(sprite)+".png"
		self.mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))
		return

	def setLocation(self, newX, newY, loc):
		if loc == "map":
			self.currentX = newX*20
			self.currentY = newY*20
		elif loc == "menu":
			self.currentY -= newY*25

	def getLocation(self):
		return (self.currentX, self.currentY)

	def getX(self):
		return self.currentX/20

	def getY(self):
		return self.currentY/20

	def getSprite(self):
		return pygame.image.load(self.mainPath + self.spriteFileName)

