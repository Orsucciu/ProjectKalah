#!/usr/bin/python
import pygame
from copy import copy
import kalahGUI
from kalahGUI import *
import os, time, sys

def KeyHandler():
	for event in pygame.event.get():   
		if event.type == QUIT:
			loop = 0     

		if event.type == K_LEFT:
			moveLeft(shroom)
		if event.type == K_UP:
			moveUp(shroom)
		if event.type == K_RIGHT:
			moveRight(shroom)
		if event.type == K_DOWN:
			moveDown(shroom)