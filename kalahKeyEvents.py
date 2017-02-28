#!/usr/bin/python
import pygame
from pygame import *
from copy import copy
import kalahGUI
from kalahGUI import *
import os, time, sys

def KeyHandler(event, boxes, houses, game, screen, fontObj): #get the keyboard keys and do stuff

	if event.type == pygame.QUIT:
		sys.exit()

	if event.type == pygame.MOUSEBUTTONDOWN:
		print pygame.mouse.get_pos()
		coord = pygame.mouse.get_pos()

		for element in boxes:
			if (element.isClicked(coord[0], coord[1]) == True):
				if((game.turn == 1 and element.number < 6) or (game.turn == 2 and element.number > 5)):
					print "#############"
					element.distributeSeeds(boxes, houses, game, screen, fontObj)
					print "######End of Distribute#####"
				else:
					print "**********"
					printText("Invalid move !", screen, fontObj, 148, 60)
					print "Invalid move. Cheater."
					print "*********"
					pygame.display.flip()
					pygame.time.delay(1000) #i know this is dirty im' sorry
											#i'm really sorry it's disgusting i doesn't even really does what i want	
				