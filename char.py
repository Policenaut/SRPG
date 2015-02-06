import os
import sys
import pygame

class character:

	mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))
	spriteFileName = ""

	hp = 0.0
	mp = 0.0
	mvt = 0.0
	atk = 0.0
	mgk = 0.0
	defe = 0.0
	res = 0.0
	currentX = 0
	currentY = 0

	'''
	# Keep track of sprite information
	sprite_dict = {
			   		1 : pygame.image.load(mainPath + "\gfx\player.png"),
			   		2 : pygame.image.load(mainPath + "\gfx\cursor.png")
			  	  }
	#
	'''

	def __init__(self, sprite):
		self.spriteFileName = "\\gfx\\"+str(sprite)+".png"
		self.mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))
		return

	def setLocation(self, newX, newY):
		self.currentX = newX*20
		self.currentY = newY*20

	def getLocation(self):
		return (self.currentX, self.currentY)

	def getX(self):
		return self.currentX/20

	def getY(self):
		return self.currentY/20

	def getSprite(self):
		return pygame.image.load(self.mainPath + self.spriteFileName)

