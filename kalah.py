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

class Kalah: #Kalah object. the game board

	def __init__(self, board):
		self.board = board

	def getBoard(self):
		return self.board

game = Kalah([0,4,4,4,4,4,4,0,4,4,4,4,4,4])

loop = 1

seeds_per_box = 4

screen = Prepare_window()
assets = LoadImages()
print assets
pygame.key.set_repeat(400, 30)

boxes = list()
x = 102 #coordinates. shouldn't be hardcoded but meh
y = 6
#boxes are 37 on 37 squares
#the houses coordinates are = 7,6 and 291,6; they are rectangles 42 on 268
for i in range(12):
	boxes.append(Box(4))
	boxes[i].createRect(x, y)
	boxes[i].populate
	x = x + 80
	if(i > 6):
		x = 52
		y = 300
	y = y

while loop == 1:
	Draw(screen, assets)
	for element in boxes:
		print element.box[0]
		print element.box[1]
		element.Draw(screen)
	
	pygame.display.flip()		

	for event in pygame.event.get():   
		KeyHandler(event)
