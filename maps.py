__author__ = 'Policenaut'

import sys
import os
import pygame
import numpy
import constants


class Mapping():
	pygame.display.set_mode((1, 1),  pygame.NOFRAME)

	mainPath = os.path.dirname(os.path.realpath(sys.argv[0]))

	# ----- map tile dictionary ------------------------------------------------
	tile_dict = {
				 1 : (pygame.image.load(mainPath + "\\gfx\\grass.png").convert(),1),
				}
	# --------------------------------------------------------------------------
	map_dict = {
				"allGrass" : numpy.ones((constants.mapWi,constants.mapHi))
			   }

	def __init__(self, mapName):
		self.screen = pygame.display.get_surface()
		self.mapArray = Mapping.map_dict[mapName]
		return

	def displayMap(self):
		for x in xrange(0, constants.mapWi):
			for y in xrange(0, constants.mapHi):
				# Determines tile type.
				current_tile = Mapping.tile_dict[self.mapArray[x, y]][0]
				self.screen.blit(current_tile, (x*20, y*20))
		return

	def getTileCostFromLocation(self, location):
		return Mapping.tile_dict[self.mapArray[location]][1]