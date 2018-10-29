#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from classes import *
from data import *
from pygame.locals import *

def main():
    pygame.init()
    pygame.time.Clock().tick(30)
    main_game = Game()
    main_game.game_init()
    main_game.game_loop()

main()
