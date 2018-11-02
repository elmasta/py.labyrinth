# -*- coding: Utf-8 -*

from classes import *

def main():
    """Main game function"""

    main_game = Game()
    main_game.game_init()
    main_game.game_loop()
    if main_game.reset_game == 1:
        return main()

main()
