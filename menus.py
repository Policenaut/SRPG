__author__ = 'Policenaut'

# !/usr/bin/python -t
import constants
import pygame
from pygame.locals import *
import maps

baseMenu = [
	        "Move",
	        "Attack",
	        "Wait",
	       ]


class InstMenu():

	currentMenu = []

	def __init__(self, charMenu, menuName, initFrom, type = "Battle"):

		self.menuForChar = charMenu
		self.menuCurrentLocation = 0
		self.getMapInput = False
		self.getMapInputRange = 0
		self.actOnCoords = set()
		self.didMove = False
		self.didAct = False
		self.curBattle = initFrom
		self.screen = pygame.display.get_surface()
		self.currentAction = None

		if menuName != "baseMenu":
			print "notDefault"
		else:
			self.menuName = menuName
			self.currentMenu = baseMenu

		self.charPositions = set()
		for char in self.curBattle.currentChars:
			self.charPositions.add((char.currentX, char.currentY))

		self.charPositions.discard((self.curBattle.CUR.currentX, self.curBattle.CUR.currentY))

		self.printMenu()
		return

	def printMenu(self):
		menuBG = pygame.image.load(constants.mainPath + "/gfx/menuItem.png").convert()
		pygame.init()
		text_color = pygame.Color('black')
		font = pygame.font.SysFont(None, 25)
		menuNum = 0
		for menuText in self.currentMenu:
			menuItem = font.render(menuText, True, text_color)
			self.screen.blit(menuBG, (constants.mapWi * 20, menuNum))
			self.screen.blit(menuItem, (constants.mapWi * 20 + 7, 4 + menuNum))
			menuNum += 25

		Hp = font.render("HP", True, text_color)
		HpNum = font.render(str(self.menuForChar.hp), True, text_color)
		self.screen.blit(menuBG, (constants.mapWi * 20, constants.windowHi - 50))
		self.screen.blit(Hp, (constants.mapWi * 20 + 7, 4 + constants.windowHi - 50))
		self.screen.blit(menuBG, (constants.mapWi * 20, constants.windowHi - 25))
		self.screen.blit(HpNum, (constants.mapWi * 20 + 7, 4 + constants.windowHi - 25))
		return

	def useMenu(self, CUR, event):
		if event.type == KEYDOWN and event.key == K_UP:
			if self.menuCurrentLocation - 1 > -1:
				CUR.setLocation(CUR.getX(), +1, "menu")
				self.menuCurrentLocation -= 1
		elif event.type == KEYDOWN and event.key == K_DOWN:
			if self.menuCurrentLocation + 1 < len(self.currentMenu):
				CUR.setLocation(CUR.getX(), -1, "menu")
				self.menuCurrentLocation += 1
		elif event.type == KEYDOWN and event.key == K_z:
			self.currentAction = self.currentMenu[self.menuCurrentLocation]
			self.actFromMenu(self.currentAction)
			return self.currentMenu[self.menuCurrentLocation]
		elif event.type == KEYDOWN and event.key == K_x:
			return "end"
		return

	def actFromMenu(self, action):
		if action == "Attack" and not self.didAct:
			self.getMapInputRange = 1
			self.generateRangeSetForAction(self.getMapInputRange, self.menuForChar.getX(), self.menuForChar.getY())
			self.getMapInput = True
		elif action == "Move" and not self.didMove:
			self.getMapInputRange = self.menuForChar.mvt
			self.generateRangeSetForMove(self.getMapInputRange, self.menuForChar.getX(), self.menuForChar.getY())
			self.getMapInput = True
		elif action == "Wait":
			if self.didAct and self.didMove:
				self.menuForChar.currentActionPoints = 0
			elif self.didAct or self.didMove:
				self.menuForChar.currentActionPoints -= 80
			else:
				self.menuForChar.currentActionPoints -= 60
		return

	def generateRangeSetForAction(self, rangeNum, originX, originY, selfTarget = False):
		self.actOnCoords = set()
		for i in xrange(0, rangeNum + 1):
			for j in xrange(0, rangeNum-i+1):
				if (originX - i) * 20 <= constants.windowWi-87 and (originY - j) * 20 <= constants.windowHi:
					self.actOnCoords.add(((originX - i) * 20, (originY - j) * 20))
				if (originX + i) * 20 <= constants.windowWi-87 and (originY - j) * 20 <= constants.windowHi:
					self.actOnCoords.add(((originX + i) * 20, (originY - j) * 20))
				if (originX + i) * 20 <= constants.windowWi-87 and (originY + j) * 20 <= constants.windowHi:
					self.actOnCoords.add(((originX + i) * 20, (originY + j) * 20))
				if (originX - i) * 20 <= constants.windowWi-87 and (originY + j) * 20 <= constants.windowHi:
					self.actOnCoords.add(((originX - i) * 20, (originY + j) * 20))
		if not selfTarget:
			self.actOnCoords.discard((originX*20,originY*20))
		return

	def generateRangeSetForMove(self, rangeNum, originX, originY, selfTarget = False):
		self.actOnCoords = set()
		startVert = Tile(originX, originY)
		discovered = set()
		discovered.add(startVert)
		explored = set()
		explored.add(startVert)
		while (len(discovered) > 0):
			traverse = discovered.pop()
			for adjacentTile in [Tile(traverse.curX, (traverse.curY - 1)),Tile(traverse.curX, (traverse.curY + 1)),Tile((traverse.curX - 1), traverse.curY),Tile((traverse.curX + 1), traverse.curY)]:
				tileLocation = ((adjacentTile.curX * 20), (adjacentTile.curY * 20))
				explored.add(adjacentTile)
				if tileLocation not in explored and tileLocation not in self.charPositions and tileLocation[0] <= constants.windowWi-87 and tileLocation[1] <= constants.windowHi:
					adjacentTile.distance = traverse.distance + maps.tile_dict[self.curBattle.map.mapArray[adjacentTile.curY, adjacentTile.curX]][1]
					if adjacentTile.distance <= rangeNum:
						self.actOnCoords.add(tileLocation)
						discovered.add(adjacentTile)
		if not selfTarget:
			self.actOnCoords.discard((originX*20,originY*20))
		return

	def displayRange(self):
		tileRangeBG = pygame.image.load(constants.mainPath + "/gfx/tileShowRange.png").convert_alpha()

		for coordinate in self.actOnCoords:
			self.screen.blit(tileRangeBG, coordinate)

	def setCURtoMenuLocation(self, CUR):
		CUR.setSprite("menuItemSelect")
		CUR.setLocation(constants.mapWi, 0,"map")
		self.menuCurrentLocation = 0
		return

	def actFromMapInput(self, locationSelected, locX, locY, CUR):
		if self.currentAction == "Move":
			self.menuForChar.setLocation(locX, locY, "map")
			self.getMapInput = False
			self.setCURtoMenuLocation(CUR)
			self.actOnCoords = set()
			self.didMove = True
		elif self.currentAction == "Attack":
			# TODO: Insert attack calculation
			for charLocation in self.charPositions:
				if charLocation == CUR.getLocation():
					print "target spotted"

			self.getMapInput = False
			self.setCURtoMenuLocation(CUR)
			self.actOnCoords = set()
			self.didAct = True

		return

class Tile():

	def __init__(self, orgX, orgY):
		self.curX = orgX
		self.curY = orgY
		self.distance = 0
