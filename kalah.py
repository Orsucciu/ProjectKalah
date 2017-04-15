#!/usr/bin/python

#main file, with the game loop

import pygame
from pygame import *
from copy import copy
import os, time, sys
import kalahGUI
from kalahGUI import *
import kalahKeyEvents
from kalahKeyEvents import *
import pickle
import os.path
import AI
from AI import *

game = Kalah()

loop = 1

fontObj = initText() #prepare the font.
screen = Prepare_window()
assets = LoadImages()
pygame.key.set_repeat(400, 30)

houses = list()
### houses creation loop
houses.append(House(0))
houses.append(House(1))
houses[0].createRect(16, 11)
houses[1].createRect(685, 11)
###

boxes = list()
### boxes creation
x = 135 #coordinates. shouldn't be hardcoded but meh
y = 300
#boxes are 37 on 37 squares
#the houses coordinates are = 7,6 and 291,6; they are rectangles 42 on 268
i = 0
xChanged = 0

while(i < 12):
	
	boxes.append(Box(4, i))
	boxes[i].createRect(x, y)
	boxes[i].position[0] = x
	boxes[i].position[1] = y
	if(i <= 5):	
		x = x + 90
	if(i >= 5 and xChanged == 0):
		x = x - 90
		y = 150
		#xChanged = 1
	i = i +1
###

### button init
reloadButton = ReloadGame("reload", 0)
reloadButton.createRect(572, 11, "reload")
saveButton = SaveGame("save", 1)
saveButton.createRect(572, 11, "save")
buttons = [reloadButton, saveButton]
###
if(os.path.isfile("save.dump") == False): #if there isn't a save file, we make it
	saveFile = open("save.dump", "w+")
else:
	#saveFile = open("save.dump", "w+")
	print "save file found !"
	saveFile = open("save.dump", "r+")#if the file exists, we read it
	loadSave(game, boxes, houses, saveFile)

while loop == 1:
	
	Draw(screen, assets)
	for element in houses:
		element.Draw(screen)
		element.populate(screen)
		
	for element in boxes:
		element.Draw(screen)
		element.populate(screen) #populate has to be called last
	
	if(game.turn == 1 or game.turn == 2):
		printText("player " + str(game.turn) + "'s turn.", screen, fontObj, 148, 20)
		saveButton.Draw(screen)
	else:
		printText("game finished.", screen, fontObj, 148, 20)
		reloadButton.Draw(screen)
	
	for event in pygame.event.get():
		if(game.turn == 1):
			KeyHandler(event, boxes, houses, game, screen, fontObj, buttons, saveFile)
		else:
			AI.play(event, boxes, houses, game, screen, fontObj, buttons, saveFile)
	pygame.display.flip()		#the elements are drawn in the order they are called -> the dots have to be last or they're overdrawn