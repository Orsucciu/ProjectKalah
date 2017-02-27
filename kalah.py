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

game = Kalah()

loop = 1

screen = Prepare_window()
assets = LoadImages()
print assets
pygame.key.set_repeat(400, 30)

houses = list()
### houses creation loop
houses.append(House())
houses.append(House())
houses[0].createRect(16, 11)
houses[1].createRect(685, 11)
###

boxes = list()
### boxes creation
x = 135 #coordinates. shouldn't be hardcoded but meh
y = 150
#boxes are 37 on 37 squares
#the houses coordinates are = 7,6 and 291,6; they are rectangles 42 on 268
i = 0
xChanged = 0

while(i < 12):
	
	boxes.append(Box(4, i))
	boxes[i].createRect(x, y)
	boxes[i].position[0] = x
	boxes[i].position[1] = y
	x = x + 90
	if(i >= 5 and xChanged == 0):
		x = 135
		y = 300
		xChanged = 1
	i = i +1
###

#useless. just initialization and testing
Draw(screen, assets)

for element in houses:
	element.Draw(screen)
	
for element in boxes:
	print element.box[0]
	print element.box[1]
	print element.getCoords()
	element.Draw(screen)
	
pygame.display.flip()	
###

while loop == 1:
	Draw(screen, assets)
	for element in houses:
		element.Draw(screen)
		element.populate(screen)
		
	for element in boxes:
		element.Draw(screen)
		element.populate(screen) #populate has to be called last
	pygame.display.flip()		#the elements are drawn in the order they are called -> the dots have to be last or they're overdrawn

	for event in pygame.event.get():   
		KeyHandler(event, boxes)
