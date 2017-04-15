#!/usr/bin/python
import pygame
from copy import copy
import os, time, sys
from random import randint
import kalahGUI
from kalahGUI import *

def simulateBoard(boxes, houses, game):
	###this create a copy of the board, where we'll search which play is the best
	###Idea : we copy the game's state, we run plays on it, we save a score for each and
	###play *for real* the best one

	#this is he game's state
	gameState = [boxes, houses, game]
	#this is the possible plays; additional play will be appended (plays.append[]) later
	plays = []

