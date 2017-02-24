#!/usr/bin/python
import pygame
from copy import copy
import os, time, sys
from random import randint

#where the graphics are

def Prepare_window(): #create the game window
	#os.environ['SDL_VIDEO_CENTERED'] = '1' #should center pygame window on the screen
	pygame.init()
	pygame.display.init()
	screen = pygame.display.set_mode((850,500))
	pygame.display.set_caption('Python Kalah')
	return screen

def LoadImages(): #loads the sprites
	board = [1,1]
	board[0] = pygame.image.load(os.path.join("assets","board.png")).convert()
	board[0] = pygame.transform.scale(board[0], (800, 500))
	board[1] = (0,0)
	return [board]



def Draw(screen, assets): #draws all the surfaces in assets
	for element in assets:
		screen.blit(element[0], element[1]) #this method is old, and is kinda same of box's one

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

class Box: #boxes are where the seeds are put

	def __init__(self, seeds):
		self.seeds = seeds
		self.dots = list()
		self.box = [1,1]
		self.position = [1,1]

	def addSeed():
		self.seeds = self.seeds + 1

	def removeSeed():
		if self.seeds > 0:
			self.seeds = self.seeds - 1

	def createRect(self, x, y): #create the box
		self.box[0] = pygame.image.load(os.path.join("assets","box.png")).convert() #the rect object
		self.box[0] = pygame.transform.scale(self.box[0], (80, 80))
		self.box[1] = (x,y) #the coordinates

	#def getRandCords(self): #gives random coordinates inside the box
	#	box = self.box[0].get_rect()
	#	x = randint(self.position[0] - 10, (self.position[0] + box.width) - 10)  ### These two lines are to be modified lightly. So the dots stay far from the borders
	#	y = randint(self.position[1] - 10, (self.position[1] + box.height) - 10) ###
	#	return [x, y]

	###RandCords shouldn't be declared here
	
	def populate(self, screen): #create the seeds in a box
		i = 0
		while(i < self.seeds):
			self.dots.append(Dot(i, self))
			#coord = self.getRandCords()
			self.dots[i].createRect(self.dot[i].position[0], self.dot[i].position[1])
			self.dots[i].DrawDot(screen)
			i = i+1	

	def Draw(self, screen):
		screen.blit(self.box[0] , self.box[1])

	def isClicked(self, x, y): #this function will determine if a box is being clicked or not
		#if(&&):		#on each click event, all the squares with this method will be called
		box = self.box[0].get_rect()
		if(x >= box.x and x <= box.x + box.width and y >= box.y and y <= box.y + box.height):
			print self
			return 1
		else:
			print "fail..."
			print "x = " + str(x) + " box.x = " + str(box.x) + " box.width = " + str(box.width) + " y = " + str(y) + " box.y = " + str(box.y)
			return 0

class Dot: #dots are the seeds

	def __init__(self, num, parentBox):
		self.num = num
		self.dot = [1,1]
		self.position = [1,1]
		
		coords = self.getRandCords(parentBox)
		self.position[0] = coords[0]
		self.position[1] = coords[1]
		
		print "dot created ! " + str(self.num)

	def createRect(self, x, y):
		self.dot[0] = pygame.image.load(os.path.join("assets", "seed.png")).convert_alpha()
		self.dot[0] = pygame.transform.scale(self.dot[0], (5, 5))
		self.dot[1] = (x, y)

	def DrawDot(self, screen):
		screen.blit(self.dot[0], self.dot[1])
	
	def getRandCords(self, Pbox): #gives random coordinates inside the box
		box = Pbox.box[0].get_rect()
		x = randint(box.position[0] - 10, (box.position[0] + box.width) - 10)  ### These two lines are to be modified lightly. So the dots stay far from the borders
		y = randint(box.position[1] - 10, (box.position[1] + box.height) - 10) ###
		return [x, y]

