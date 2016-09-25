__author__ = 'Policenaut'

import os
import sys
from random import randint
import pygame


class Character(pygame.sprite.Sprite):

	classes = {
			   1: ["Warrior"],
			   2: ["Paladin"],
			   3: ["Phantom Knight"],
			   4: ["Myrmidon"],
	           5: [""],
	           6: [""],
	           7: ["Sharpshooter"],
	           8: [""],
	           9: [""],
	           10:["Gear Knight"]
			  }

	def setSprite(self, filename):
		self.spriteFileName = "/gfx/" + str(filename) + ".png"
		return

	def __init__(self, sprite, speed = None):
		self.spriteFileName = "/gfx/" + str(sprite) + ".png"
		self.mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))

		self.isActive = True
		self.hp = randint(2, 12)
		self.mp = 0.0
		self.mvt = 5
		self.atk = randint(1, 5)
		self.mgk = 0.0
		self.defense = 0.0
		self.res = 0.0
		if sprite == "cursor":
			self.speed = 0
		else:
			self.speed = randint(3,5)
		self.weapon = "rusty sword"
		self.armor = "cloths"
		self.skills = []
		self.currentActionPoints = 0

		self.currentX = 0
		self.currentY = 0
		return

	def setLocation(self, newX, newY, loc):
		if loc == "map":
			self.currentX = newX * 20
			self.currentY = newY * 20
		elif loc == "menu":
			self.currentY -= newY * 25
		return

	def getLocation(self):
		return self.currentX, self.currentY

	def getX(self):
		return self.currentX / 20

	def getY(self):
		return self.currentY / 20

	def getSprite(self):
		return pygame.image.load(self.mainPath + self.spriteFileName)

