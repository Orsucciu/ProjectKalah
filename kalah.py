#!/usr/bin/python

import pygame
from pygame import *
from copy import copy
import os, time, sys
import kalahGUI
from kalahGUI import *
import kalahKeyEvents
from kalahKeyEvents import *

class Kalah:

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
shroom = assets[1]

boxes = list()
for i in range(12):
	boxes.append(Box(4))
	print boxes[i]	#added for testing purposes
	boxes[i].createRect(50, 50)
	print boxes[i].box[0].get_rect()
	boxes[i].populate
	print boxes[i].dots #test again

#Resize(screen, assets)

while loop == 1:
	Draw(screen, assets)

	for event in pygame.event.get():   
		KeyHandler(event, shroom)
