__author__ = 'Policenaut'

from battle import Battle
import constants
import pygame

# class Main():
fpsClock = pygame.time.Clock()
battleInst = Battle()

screen = pygame.display.set_mode((constants.windowWi, constants.windowHi))

pygame.display.set_caption("Game Sampling!")

gameRunning = True

while gameRunning:
    battleInst.getInputSetValues()
    battleInst.updateDisplay()
    # Updates display and then sets FPS to 30 FPS.
    pygame.display.update()
    #fpsClock.tick(60)

pygame.quit()