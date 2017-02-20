#!/usr/bin/python
import pygame
from pygame import *
from copy import copy
import kalahGUI
from kalahGUI import *
import os, time, sys

def KeyHandler(event): #get the keyboard keys and do stuff

	'''
	if event.type == pygame.KEYDOWN: #dead code. leave it be

		if event.key == pygame.QUIT:
			loop = 0   
		if event.key == pygame.K_LEFT:
			moveLeft(shroom)
		if event.key == pygame.K_UP:
			moveUp(shroom)
		if event.key == pygame.K_RIGHT:
			moveRight(shroom)
		if event.key == pygame.K_DOWN:
			moveDown(shroom)
	'''