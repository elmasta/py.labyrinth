# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *

from classes import *

def main():
    """Main game function"""
    
    pygame.init()
    pygame.time.Clock().tick(30)
    main_game = Game()
    main_game.game_init()
    main_game.game_loop()

main()
