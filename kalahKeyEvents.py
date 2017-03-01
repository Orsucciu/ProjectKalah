#!/usr/bin/python
import pygame
from pygame import *
from copy import copy
import kalahGUI
from kalahGUI import *
import os, time, sys

def KeyHandler(event, boxes, houses, game, screen, fontObj, buttons, saveFile): #get the keyboard keys and do stuff

	if event.type == pygame.QUIT:
		sys.exit()

	if event.type == pygame.MOUSEBUTTONDOWN:
		printGameState(game, boxes, houses)
		#print pygame.mouse.get_pos()
		coord = pygame.mouse.get_pos()

		for element in boxes:
			if (element.isClicked(coord[0], coord[1]) == True):
				if((game.turn == 1 and element.number < 6) or (game.turn == 2 and element.number > 5)):
					element.distributeSeeds(boxes, houses, game, screen, fontObj)
				else:
					'''print "**********"
					printText("Invalid move !", screen, fontObj, 148, 60)
					print "Invalid move. Cheater."
					print "*********"'''
					pygame.display.flip()
					pygame.time.delay(1000) #i know this is dirty im' sorry
											#i'm really sorry it's disgusting i doesn't even really does what i want	
		
		if(buttons[0].isClicked(coord[0], coord[1]) == True and game.turn != 0):
			buttons[1].save(game, boxes, houses, screen, fontObj, buttons, saveFile)
			
		if(buttons[1].isClicked(coord[0], coord[1]) == True and game.turn == 0):
			buttons[0].reload(game, boxes, houses)
			