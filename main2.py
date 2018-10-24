#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from classes import *
from data import *
from pygame.locals import *



labyrinth_generation = Generation()
character_control = Player()
labyrinth_generation.display(floor, window)
labyrinth_generation.item_placement(window)
character_control.PlayerMovement(labyrinth_generation.layout)
