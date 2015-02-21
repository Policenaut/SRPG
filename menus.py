__author__ = 'Policenaut'

# !/usr/bin/python -t
import constants
import pygame
from pygame.locals import *
#from maps import Tile


class InstMenu():

	pygame.init()

	menuCurrentLocation = 0
	menuName = ""
	charName = ""

	baseMenu = [
				"Move",
				"Attack",
				"Wait"
			   ]

	currentMenu = []

	def __init__(self, charMenu, menuName, mapWi, mapHi, initFrom, type = "Battle"):

		self.mapWi = mapWi
		self.mapHi = mapHi
		self.menuForChar = charMenu
		self.getMapInput = False
		self.getMapInputRange = 0
		self.actOnCoords = set()
		self.didMove = False
		self.curBattle = initFrom

		self.screen = pygame.display.get_surface()

		if menuName != "baseMenu":
			print "notDefault"
		else:
			self.menuName = menuName
			self.currentMenu = self.baseMenu

		self.printMenu()
		return

	def printMenu(self):
		menuBG = pygame.image.load(constants.mainPath + "\\gfx\\menuItem.png").convert()

		pygame.init()
		text_color = pygame.Color('black')
		font = pygame.font.SysFont(None, 25)

		menuNum = 0
		for menuText in self.currentMenu:
			menuItem = font.render(menuText, True, text_color)
			self.screen.blit(menuBG, (self.mapWi * 20, menuNum))
			self.screen.blit(menuItem, (self.mapWi * 20 + 7, 4 + menuNum))
			menuNum += 25
		return

	def useMenu(self, CUR, event):
		if event.type == KEYDOWN and event.key == K_UP:
			if self.menuCurrentLocation - 1 > -1:
				CUR.setLocation(CUR.getX(), +1,"menu")
				self.menuCurrentLocation -= 1
		elif event.type == KEYDOWN and event.key == K_DOWN:
			if self.menuCurrentLocation + 1 < self.currentMenu.__len__():
				CUR.setLocation(CUR.getX(), -1,"menu")
				self.menuCurrentLocation += 1
		elif event.type == KEYDOWN and event.key == K_z:
			self.currentAction = self.currentMenu[self.menuCurrentLocation]
			return self.actFromMenu(self.currentMenu[self.menuCurrentLocation])
		elif event.type == KEYDOWN and event.key == K_x:
			return "end"
		return

	def actFromMenu(self, action):
		if action == "Attack":
			self.displayRangeForAction("Attack")
		elif action == "Move" and not self.didMove:
			self.displayRangeForAction("Move")
		return action

	def displayRangeForAction(self, action):
		if action == "Attack":
			self.getMapInput = True
			self.getMapInputRange = 10
			self.generateRangeSet(self.getMapInputRange, self.menuForChar.getX(), self.menuForChar.getY())
		elif action == "Move":
			self.getMapInput = True
			self.getMapInputRange = self.menuForChar.mvt
			self.generateRangeSet(self.getMapInputRange, self.menuForChar.getX(), self.menuForChar.getY())
		return

	def generateRangeSet(self, rangeNum, originX, originY):
		charPositions = set()

		for char in self.curBattle.currentChars:
			charPositions.add((char.currentX, char.currentY))

		startVert = Tile(originX, originY)
		self.actOnCoords =[]# set()
		needToTraverse = set()
		needToTraverse.add(startVert)
		while (len(needToTraverse) > 0):
			traverse = needToTraverse.pop()
			# mvUp = Tile(traverse.curX, (traverse.curY - 1))
			# mvDown = Tile(traverse.curX, (traverse.curY + 1))
			# mvLeft = Tile((traverse.curX - 1), traverse.curY)
			# mvRight = Tile((traverse.curX + 1), traverse.curY)
			for tile in [
						 Tile(traverse.curX, (traverse.curY - 1)),
			             Tile(traverse.curX, (traverse.curY + 1)),
			             Tile((traverse.curX - 1), traverse.curY),
			             Tile((traverse.curX + 1), traverse.curY)
						]:
				tileLocation = ((tile.curX * 20), (tile.curY * 20))
				if tileLocation not in self.actOnCoords and tileLocation not in charPositions:
					tile.distance = traverse.distance + 1 # Replace 1 with a representation of the terrain traverse cost
					if tile.distance <= rangeNum:
						self.actOnCoords.append(tileLocation)
						needToTraverse.add(tile)

		return

	def displayRange(self):
		tileRangeBG = pygame.image.load(constants.mainPath + "\\gfx\\tileShowRange.png").convert_alpha()

		for coordinate in self.actOnCoords:
			self.screen.blit(tileRangeBG, coordinate)

	def setCURtoMenuLocation(self, CUR):
		CUR.setSprite("menuItemSelect")
		CUR.setLocation(self.mapWi, 0,"map")
		self.menuCurrentLocation = 0
		return

	def actFromMapInput(self, locationSelected, locX, locY, CUR):
		if self.currentAction == "Move":
			self.menuForChar.setLocation(locX, locY, "map")
			self.getMapInput = False
			self.setCURtoMenuLocation(CUR)
			self.actOnCoords = set()
			self.didMove = True
		return

class Tile():

	def __init__(self, orgX, orgY):
		self.curX = orgX
		self.curY = orgY
		self.distance = 0