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

def initText(): #does stuff so i can draw over the screen.
	pygame.font.init()
	font_path = "assets/Font/FantasqueSansMono-Regular.ttf"
	font_size = 32
	return pygame.font.Font(font_path, font_size)

def printText(text, screen, fontObj, x, y):
	display = fontObj.render(text, 1, (0, 0, 0))
	screen.blit(display, (x, y))
	
def textPrinter(text, screen, fontObj, x, y, delay): #almost same as printText but do some more stuff
	printText(text, screen, fontObj, x, y)			#delay is the milliseconds. Integer
	print text
	pygame.display.flip()
	pygame.time.delay(delay) #i know this is dirty im' sorry
											#i'm really sorry it's disgusting i doesn't even really does what i want	

def checkRules(box, game, houses, boxes, screen, fontObj): #this is going to check if kalah rules apply.
	freeTurn = False	

	if(isinstance(box, Box)):
		seeds = 0
		print "last box sowed : " + str(box.number)
		if(box.seeds == 1): #the box have been sowed just now. you empty the opposite one
			if(game.turn == 1 and box.number < 6):	
				print "the opposite box is : " + str(getOppositeBox(box))
				if(boxes[getOppositeBox(box)].seeds > 0):
					seeds = seeds + box.removeAllSeeds() #the removeAllSeeds functions returns the seeds removed
					seeds = seeds + boxes[getOppositeBox(box)].removeAllSeeds()
					houses[1].addSeeds(seeds)
			if(game.turn == 2 and box.number > 5):
				print "the opposite box is : " + str(getOppositeBox(box))
				if(boxes[getOppositeBox(box)].seeds > 0):
					seeds = seeds + box.removeAllSeeds() #the removeAllSeeds functions returns the seeds removed
					seeds = seeds + boxes[getOppositeBox(box)].removeAllSeeds()
					houses[0].addSeeds(seeds)

	if(canCurrentPlayerPlay(boxes, game) == False):
		emptyAllBoxes(boxes, houses)
		print "game finished !"
		result = whoWon(houses)
		if(result == 0):
			textPrinter("player 1 won !!! Mazeltov", screen, fontObj, 148, 60, 3000)
		if(result == 1):
			textPrinter("player 2 won !!! Mazeltov", screen, fontObj, 148, 60, 3000)
		if(result == 3):
			textPrinter("it's a draw.", screen, fontObj, 148, 60, 3000)

###BUGGED
	#First you check if the player can play again
	#if he does he plays again
	if(isinstance(box, House)): #check if the last play filled a player's house (and give him another turn)
		if(box.number == houses[0].number and game.turn == 2): #if the last filled house's number is the same as the player two's house (and therefore is the same house) AND it's player two's turn
			print "player two gets another turn"
			freeTurn = True
		if(box.number == houses[1].number and game.turn == 1):
			print "player one gets another turn"
			freeTurn = True
	
	#if he can't you change turn
	if(freeTurn == False): #handle which player's turn it is.
		if(game.turn == 1):
			game.turn = 2
		else:
			game.turn = 1
###

def getOppositeBox(box): #takes a box as a parameter and returns the number|the box opposed to it
	return (11 - box.number)

def areAllBoxesEmpty(boxes): #checks if all the boxes are empty
	seeds = 0
	for element in boxes:
		seeds = seeds + element.getSeeds()
	
	if(seeds == 0):
		return True
	else:
		return False

def whoWon(houses):
	if(houses[0].getSeeds() > houses[1].getSeeds()):
		return 1 #player 2 won
	elif(houses[1].getSeeds() > houses[0].getSeeds()):
		return 0 #player 1 won
	elif(houses[0].getSeeds() == houses[1].getSeeds()):
		return 3 #it's a draw !!!

def canCurrentPlayerPlay(boxes, kalah): #says if the player of the current turn can play. Takes the boxes (to see if they're empty) and the board (to get the player) as param
	seeds = 0
	if(kalah.turn == 1):
		for element in boxes:
			if element.number < 6:	
				seeds = seeds + element.getSeeds()
			
		if(seeds > 0):
			return True
		else:
			return False
	
	if(kalah.turn == 2):
		for element in boxes:
			if element.number > 5:
				seeds = seeds + element.getSeeds()
			
		if(seeds > 0):
			return True
		else:
			return False
		
def emptyAllBoxes(boxes, houses): #to be called when a player can't play anymore. it puts the remaining seeds in the corresponding house
	seeds0 = 0
	seeds1 = 0
	for element in boxes:
		if(element.number < 6):
			seeds1 = seeds1 + element.getSeeds()
			element.removeAllSeeds()
			houses[1].addSeeds(seeds1)
		
		if(element.number > 5):
			seeds0 = seeds0 + element.getSeeds()
			element.removeAllSeeds()
			houses[0].addSeeds(seeds0)
		

class Kalah: #Kalah object. the game board

	def __init__(self):
		self.board = [4,4,4,4,4,4,4,4,4,4,4,4] #represent the board's boxes
		self.houses = [0, 0] #represent the houses
		self.turn = 1 #represent the player's turn. 1 for you, and 2 for anyone someone. Or whatever it doesn't matter

	def getBoard(self):
		return self.board

class House: #houses are where the seeds end up
	
	def __init__(self, number): #houses are really like boxes, but they can't move their dots out and stuff like that
		self.seeds = 0
		self.dots = list()
		self.house = [1,1]
		self.number = number ###Useful to check which house is it exactly (since they're all the sames)
	
	def addSeed(self):
		self.seeds = self.seeds + 1
	
	def addSeeds(self, number):
		self.seeds = self.seeds + number
		
	def getSeeds(self):
		return self.seeds
	
	def removeSeed(self):
		if self.seeds > 0:
			self.seeds = self.seeds - 1
	
	def getCoords(self):
		return [ self.house[1][0], self.house[1][1], self.house[0].get_width(), self.house[0].get_height() ] #returns data in this order : box's x, box's y, box's width, box's height
	
	def createRect(self, x, y): #create the house
		self.house[0] = pygame.image.load(os.path.join("assets","house.png")).convert_alpha() #the rect object #change this to convert() to see the house
		self.house[0] = pygame.transform.scale(self.house[0], (100, 480))
		self.house[1] = (x,y) #the coordinates
	
	def Draw(self, screen):
		screen.blit(self.house[0] , self.house[1])
	
	def populate(self, screen): #create the seeds in a box
		i = 0					#the seeds will be distributed by rows of four
		coord = self.getCoords()
		x = coord[0] + 10
		y = coord[1] + 5
	
		while(i < self.seeds):
			if(i % 4 == 0):
				x = coord[0] + 5
				y = y + 10
				
			self.dots.append(Dot(i, self))
			self.dots[i].createRect(x, y)
			self.dots[i].DrawDot(screen)
			
			x = x + 10
			
			i = i+1
			
class Box: #boxes are where the seeds are put

	def __init__(self, seeds, number): 
		self.seeds = seeds
		self.number = number #number is used to keep track of the boxes (like, to know which one is it)
		self.dots = list() #contains the dots stored in the box
		self.box = [1,1] #contains the surface object, and its coordinates (in the box[1])
		self.position = [1,1]
		
	def isEmpty(self):
		if(self.getSeeds() == 0):
			return True
		else:
			return False
	
	def getSeeds(self):
		return self.seeds

	def getCoords(self):
		return [ self.box[1][0], self.box[1][1], self.box[0].get_width(), self.box[0].get_height() ] #returns data in this order : box's x, box's y, box's width, box's height

	def addSeed(self):
		self.seeds = self.seeds + 1

	def removeSeed(self):
		if self.seeds > 0:
			self.seeds = self.seeds - 1
	
	def removeAllSeeds(self): #remove all the seeds of a box and return how much were removed
		seeds = self.seeds
		self.seeds = 0 #used for when you sow an empty box, with the opposite one non-empty
		return seeds

	def createRect(self, x, y): #create the box
		self.box[0] = pygame.image.load(os.path.join("assets","box.png")).convert() #the rect object
		self.box[0] = pygame.transform.scale(self.box[0], (80, 80))
		self.box[1] = (x,y) #the coordinates
	
	def populate(self, screen): #create the seeds in a box
		i = 0					#the seeds will be distributed by rows of four
		coord = self.getCoords()
		x = coord[0] + 10
		y = coord[1] + 5
		
		while(i < self.seeds):
			if(i % 4 == 0):
				x = coord[0] + 5
				y = y + 10
				
			self.dots.append(Dot(i, self))
			self.dots[i].createRect(x, y)
			self.dots[i].DrawDot(screen)
			
			x = x + 10
			
			i = i+1	

	def Draw(self, screen):
		screen.blit(self.box[0] , self.box[1])

	def isClicked(self, x, y): #this function will determine if a box is being clicked or not
		#if(&&):		#on each click event, all the squares with this method will be called
		boxCoords = self.getCoords() #if a box is being clicked, this function will return true
		if(x >= boxCoords[0] and x <=boxCoords[0] + 80 and y >= boxCoords[1] and y <= boxCoords[1] + 80): #box's height and width are harcoded. could be changed in the future
			print self
			print self.number
			return True
		else:
			#print "fail..." #those two are debug lines
			#print "x = " + str(x) + " box.x = " + str(boxCoords[0]) + " box.width = " + str(80) + " y = " + str(y) + " box.y = " + str(boxCoords[1])
			return False
		
	def distributeSeeds(self, boxes, houses, game, screen, fontObj): #distribute the seeds in the boxes and houses. annoying as fuck
		lastBox = None #this will contain the last object we put a seed in
		i = self.number
		
		while(self.seeds > 0 ):
			
			if(self.seeds > 0): #can be removed
				if(i != 11 and i != 5):#this is broken (or not in the end. it's not)
					i = i +1
					boxes[i].addSeed()
					if(self.seeds == 1):
						lastBox = boxes[i]
						#checkRules(lastBox)
				elif(i == 5): #if we're at the fifth cell, there's special stuff to do
					i = 6
					houses[1].addSeed()
					self.removeSeed()
					lastBox = houses[1]
					if(self.seeds > 0):
						boxes[6].addSeed()
						if(self.seeds == 1):
							lastBox = boxes[6]
							#checkRules(lastBox)
				elif(i == 11):
					i = 0
					houses[0].addSeed()
					self.removeSeed()
					lastBox = houses[0]
					if(self.seeds > 0):		
						boxes[0].addSeed()
						if(self.seeds == 1):
							lastBox = boxes[0]
							#checkRules(lastBox)
				
			self.removeSeed()
			#i = i + 1
		
		if(isinstance(lastBox, Box) or isinstance(lastBox, House)):
			print "the last box is  : " + str(lastBox)
			checkRules(lastBox, game, houses, boxes, screen, fontObj)

class Dot: #dots are the seeds

	def __init__(self, num, parentBox): #parentbox can be removed, but no time for this
		self.num = num
		self.dot = [1,1]
		self.position = [1,1]
		
		#print "dot created ! " + str(self.num)

	def createRect(self, x, y):
		self.dot[0] = pygame.image.load(os.path.join("assets", "seed.png")).convert_alpha()
		self.dot[0] = pygame.transform.scale(self.dot[0], (5, 5))
		self.dot[1] = (x, y)

	def DrawDot(self, screen):
		screen.blit(self.dot[0], self.dot[1])
	
	###dead code ?
	'''def getRandCords(self, Pbox): #gives random coordinates inside the box
		#the pbox arg is the Parent box, where the dot will be stored
		box = Pbox.box[1]
		x = randint(self.position[0] - 10, (self.position[0] + box[0]) - 10)  ### These two lines are to be modified lightly. So the dots stay far from the borders
		y = randint(self.position[1] - 10, (self.position[1] + box[1]) - 10) ###
		
		return [x, y]'''
	###
