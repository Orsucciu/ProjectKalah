#!/usr/bin/python
import pygame
from copy import copy
import os, time, sys
from random import randint

def Prepare_window(): #create the game window
	#os.environ['SDL_VIDEO_CENTERED'] = '1' #should center pygame window on the screen
	pygame.init()
	pygame.display.init()
	screen = pygame.display.set_mode((850,500))
	pygame.display.set_caption('Python Kalah')
	return screen

def LoadImages(): #loads the sprites
	board = [1,1]
	shroom = [1,1]
	board[0] = pygame.image.load(os.path.join("assets","board.png")).convert()
	board[0] = pygame.transform.scale(board[0], (800, 500))
	shroom[0] = pygame.image.load(os.path.join("assets","shroom.png")).convert_alpha()
	board[1] = (0,0)
	shroom[1] = (50,50)
	return [board, shroom]



def Draw(screen, assets): #draws all the surfaces in assets
	for element in assets:
		screen.blit(element[0], element[1])
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

def moveLeft(sprite): #move a pygame surface object in a direction
	position = sprite[0].get_rect()
	print position
	print type(position)
	print position.x
	position = position.move(position.x -10, 0)
	sprite[1] = position

def moveUp(sprite):
	position = sprite[0].get_rect()
	position = position.move(0, position.y -10)
	sprite[1] = position

def moveDown(sprite):
	position = sprite[0].get_rect()
	position = position.move(0, position.y +10)
	sprite[1] = position

def moveRight(sprite):
	position = sprite[0].get_rect()
	position = position.move(position.x + 10, 0)
	sprite[1] = position


class Box:

	def __init__(self, seeds):
		self.seeds = seeds
		self.dots = list()
		self.box = [1,1]

	def addSeed():
		self.seeds = self.seeds + 1

	def removeSeed():
		if self.seeds > 0:
			self.seeds = self.seeds - 1

	def createRect(self, x, y): #create the box
		self.box[0] = pygame.image.load(os.path.join("assets","box.png")).convert()
		self.box[1] = (x,y)

	def getRandCords():
		box = self.get_rect()
		x = randint(box.x, box.x + box.width)
		y = randint(box.y, box.y + box.height)
		return (x, y)

	def populate():
		i = 0
		while(i < self.seeds):
			self.dots.append(Dot(i))
			self.dots[i].createRect(getRandCords())
			i = i+1	

class Dot:

	def __init__(self):
		self = self

	def createRect(x, y):
		dot = [1,1]
		dot[0] = pygame.image.load(os.path.join("assets", "dot.png")).convert_alpha()
		dot[1] = (x, y)
		return dot

