__author__ = 'Policenaut'

from pygame.locals import *
import constants
from menus import InstMenu


def getBattleMapInput(curBat, event):
	if event.type == KEYDOWN and event.key == K_UP:
		if curBat.CUR.getY() - 1 >= 0:
			curBat.CUR.setLocation(curBat.CUR.getX(), curBat.CUR.getY() - 1, "map")
	elif event.type == KEYDOWN and event.key == K_DOWN:
		if curBat.CUR.getY() + 1 < constants.mapHi:
			curBat.CUR.setLocation(curBat.CUR.getX(), curBat.CUR.getY() + 1, "map")
	elif event.type == KEYDOWN and event.key == K_LEFT:
		if curBat.CUR.getX() - 1 >= 0:
			curBat.CUR.setLocation(curBat.CUR.getX() - 1, curBat.CUR.getY(), "map")
	elif event.type == KEYDOWN and event.key == K_RIGHT:
		if curBat.CUR.getX() + 1 < constants.mapWi:
			curBat.CUR.setLocation(curBat.CUR.getX() + 1, curBat.CUR.getY(), "map")
	elif event.type == KEYDOWN and event.key == K_z:
		if curBat.thisMenu[0] is not None and curBat.thisMenu[0].getMapInput and curBat.CUR.getLocation() in curBat.thisMenu[0].actOnCoords:
			curBat.thisMenu[0].actFromMapInput(curBat.CUR.getLocation(), curBat.CUR.getX(), curBat.CUR.getY(), curBat.CUR)
		elif curBat.thisMenu[0] is None and curBat.CUR.getLocation() == curBat.currentActiveCharacter.getLocation():
			curBat.thisMenu[0] = InstMenu(curBat.currentActiveCharacter, "baseMenu", curBat)
			curBat.CUR.setSprite("menuItemSelect")
			curBat.CUR.setLocation(constants.mapWi, 0, "map")
	elif event.type == KEYDOWN and event.key == K_x and curBat.thisMenu[0] is not None and curBat.thisMenu[0].getMapInput:
		curBat.thisMenu[0].getMapInput = False
		curBat.thisMenu[0].actOnCoords = set()
		curBat.thisMenu[0].setCURtoMenuLocation(curBat.CUR)
	return

def getBattleMenuInput(curBat, event):
	nextAction = str(curBat.thisMenu[0].useMenu(curBat.CUR, event))
	if nextAction == "Move" and not curBat.thisMenu[0].didMove:
		curBat.CUR.setLocation(curBat.thisMenu[0].menuForChar.getX(), curBat.thisMenu[0].menuForChar.getY(), "map")
		curBat.CUR.setSprite("cursorMv")
	elif nextAction == "Attack" and not curBat.thisMenu[0].didAct:
		curBat.CUR.setLocation(curBat.thisMenu[0].menuForChar.getX(), curBat.thisMenu[0].menuForChar.getY(), "map")
		curBat.CUR.setSprite("cursorMv")
	elif nextAction == "Wait":
		curBat.thisMenu[0] = None
		curBat.CUR.setSprite("cursor")
		curBat.determineNextTurn()
		curBat.CUR.setLocation(curBat.currentActiveCharacter.getX(), curBat.currentActiveCharacter.getY(), "map")
	elif nextAction == "end":
		curBat.thisMenu[0] = None
		curBat.CUR.setSprite("cursor")
		curBat.CUR.setLocation(curBat.currentActiveCharacter.getX(), curBat.currentActiveCharacter.getY(), "map")
	return
