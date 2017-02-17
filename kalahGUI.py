#!/usr/bin/python
import pygame
from copy import copy
import os, time, sys

def Prepare_window():
	#os.environ['SDL_VIDEO_CENTERED'] = '1' #should center pygame window on the screen
	pygame.init()
	pygame.display.init()
	screen = pygame.display.set_mode((850,500))
	pygame.display.set_caption('Python Kalah')
	return screen

def LoadImages():
	board = pygame.image.load(os.path.join("assets","board.png")).convert()
	board = pygame.transform.scale(board, (800, 500))
	shroom = pygame.image.load(os.path.join("assets","shroom.png")).convert_alpha()
	return [board, shroom]

def Draw(screen, assets):
	for element in assets:
		screen.blit(element, (0,0))
	pygame.display.flip()

'''
def Resize(screen, assets):
	transformed = []
	size = screen.get_size()
	for element in assets:
		element = pygame.transform.scale(element, (screen[0], screen[1]))
		transformed.append(element)
	return transformed
'''

def moveLeft(sprite):
	position = sprite.get_rect()
	position = position.move(0,3)