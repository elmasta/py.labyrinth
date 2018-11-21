# -*- coding: Utf-8 -*

from classes import *


def main():
    """Main game function"""

    end = 0
    while end == 0:
        main_game = Game()
        main_game.game_init()
        main_game.game_loop()
        if main_game.reset_game == 0:
            end = 1


main()
