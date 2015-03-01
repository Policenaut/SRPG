__author__ = 'Policenaut'

import pygame
import sys
import constants
from char import Character
from maps import Mapping
from input import getBattleMapInput, getBattleMenuInput


class Battle():

	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.menuIsActive = [False]
		self.thisMenu = [None]
		self.currentChars = []
		self.currentActiveCharacter = None

		self.map = Mapping("allGrass")

		self.charPlayer = Character("player")
		self.currentChars.append(self.charPlayer)
		self.charPlayer.setLocation(constants.mapWi - 1, constants.mapHi - 1, "map")

		self.enemyPlayer = Character("player")
		self.currentChars.append(self.enemyPlayer)
		self.enemyPlayer.setLocation(constants.mapWi - 10, constants.mapHi - 10, "map")

		self.determineNextTurn()

		self.CUR = Character("cursor")
		self.currentChars.append(self.CUR)
		self.CUR.setLocation(self.currentActiveCharacter.getX(), self.currentActiveCharacter.getY(), "map")

		fpsClock = pygame.time.Clock()
		battleRunning = True
		while battleRunning:
			self.getInputSetValues()
			self.updateDisplay()
			# Updates display and then sets FPS to 30 FPS.
			#print str(fpsClock.get_fps())
			pygame.display.update()
			fpsClock.tick(30)

	def determineNextTurn(self):
		self.currentActiveCharacter = None
		for character in self.currentChars:
			character.currentActionPoints += character.speed
			if character.currentActionPoints >= 100:
				self.currentActiveCharacter = character
				return
		self.determineNextTurn()

	def getInputSetValues(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if self.thisMenu[0] is not None and self.thisMenu[0].getMapInput:
				getBattleMapInput(self, event)
			elif self.thisMenu[0] is not None:
				getBattleMenuInput(self, event)
			else:
				getBattleMapInput(self, event)
		return

	def updateDisplay(self):
		self.map.displayMap()
		if self.thisMenu[0] is not None:
			if self.thisMenu[0].getMapInput:
				self.thisMenu[0].displayRange()
			else:
				self.thisMenu[0].printMenu()
		else:
			pygame.draw.rect(self.screen, (0, 0, 0), (860, 0, 67, constants.mapHi * 25))
		for chars in self.currentChars:
			if chars.isActive:
				self.screen.blit(chars.getSprite(), chars.getLocation())
		return