from random import randrange

import pygame
from pygame.locals import *

from data import *


class LabyrinthGeneration:
    """Class that generate a labyrinth based on infos in 'data.py'"""
    
    def __init__(self):
        self.layout = []
        self.labyrinth_selected = 0
        self.possible_item_position = []
        self.ether_position = 0
        self.needle_position = 0
        self.plastic_tube_position = 0

    def labyrinth_randomiser(self):
        """Method that select four pre-made labyrinth parts and put them
        together to create the labyrinth."""

        string_nb = 0
        north_west = NW_labyrinth_parts.pop(randrange(4))
        north_east = NE_labyrinth_parts.pop(randrange(4))
        while string_nb != 8:
            self.layout.append(north_west[string_nb] + north_east[string_nb])
            string_nb += 1
        string_nb = 0
        south_west = SW_labyrinth_parts.pop(randrange(4))
        south_east = SE_labyrinth_parts.pop(randrange(4))
        while string_nb != 7:
            self.layout.append(south_west[string_nb] + south_east[string_nb])
            string_nb += 1
        self.labyrinth_selected = north_west[8] + north_east[8]\
        + south_west[7] + south_east[7]

    def selected_labyrinth_scan(self, floor, window):
        """Method that scan the labyrinth created by the method
        'labyrinth_randomiser' and display either a floor, a wall, the
        guardian or the exit tile for each coordinate. Also create a list for
        possible item position spawn during the scan."""

        wall = pygame.image.load("sprites/walls.png").convert()
        exit_labyrinth = pygame.image.load("sprites/exit_sign.png").convert()
        guardian = pygame.image.load("sprites/Gardien.png").convert()
        guardian.set_colorkey((255, 0, 255))
        string_nb = 0
        while string_nb != 15:
            string_index = 0
            for tile in self.layout[string_nb]:
                if tile == "W":
                    window.blit(wall, (string_index * 40, string_nb * 40))
                else:
                    window.blit(floor, (string_index * 40, string_nb * 40))
                    #Scan every coordinate if it's a floor tile surrounded by
                    #3 wall tile.
                    #Return a list of coordinate that can be used to spawn
                    #items.
                    if tile == "F":
                        tile_env = self.layout[string_nb]\
                            [string_index - 1: string_index]
                        tile_env += self.layout[string_nb]\
                            [string_index + 1: string_index + 2]
                        tile_env += self.layout[string_nb - 1]\
                            [string_index: string_index + 1]
                        tile_env += self.layout[string_nb + 1]\
                            [string_index: string_index + 1]
                        possible_item_position_test = tile_env.count("W")
                        if possible_item_position_test == 3:
                            self.possible_item_position.append(
                                (string_index * 40, string_nb * 40))
                string_index += 1
            string_nb += 1
        window.blit(guardian, guardian_position)
        window.blit(exit_labyrinth, exit_position)

    def item_placement_display(self, window, ether, needle, plastic_tube):
        """Method that randomly choose a position for each item base on a list
        made by the 'selected_labyrinth_scan' method and display them."""

        self.ether_position = self.possible_item_position.pop(randrange(len(
            self.possible_item_position)))
        self.needle_position = self.possible_item_position.pop(randrange(len(
            self.possible_item_position)))
        self.plastic_tube_position = self.possible_item_position.pop(
            randrange(len(self.possible_item_position)))
        window.blit(ether, self.ether_position)
        window.blit(needle, self.needle_position)
        window.blit(plastic_tube, self.plastic_tube_position)


class Player:
    """class that put and move the player in the labyrinth. Also check and
    keep infos about items taken and if vistory condition are meet."""

    def __init__(self):
        self.player_picture = pygame.image.load("sprites/MacGyver.png").\
            convert()
        self.player_picture.set_colorkey((255, 0, 255))
        self.player_position = 0
        self.picked_up_ether = 0
        self.picked_up_needle = 0
        self.picked_up_plastic_tube = 0
        self.victory_condition_marquer = ""
        self.keep_playing = 1


    def player_generation(self):
        """Method that put the player on the starting position. only called
        when initialising the labyrinth."""

        self.player_position = self.player_picture.get_rect()
        self.player_position = self.player_position.move(
            MacGyver_starting_position)

    def move_down(self, layout, floor, window):
        """Method that make the player move down if the left arrow key is
        pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40 + 1]\
                [self.player_position[0] // 40] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(0, 40)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def move_up(self, layout, floor, window):
        """Method that make the player move up if the left arrow key is
        pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40 - 1]\
                [self.player_position[0] // 40] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(0, -40)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def move_right(self, layout, floor, window):
        """Method that make the player move right if the left arrow key is
        pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40]\
                [self.player_position[0] // 40 + 1] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(40, 0)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def move_left(self, layout, floor, window):
        """Method that make the player move left if the left arrow key is
        pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40]\
                [self.player_position[0] // 40 - 1] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(-40, 0)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def victory_condition(self, window, ether_position, needle_position,
                          plastic_tube_position):
        """Method that update which items are taken and if the victory
        condition is meet when encountering the guardian. This method also
        stop the game if you're on the exit position (victory) or if you're on
        the guardian position without having every item (defeat)."""

        player_position_tuple = (
            self.player_position[0], self.player_position[1]
        )
        if player_position_tuple == ether_position\
                and self.picked_up_ether == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_ether = 1
        elif player_position_tuple == needle_position\
                and self.picked_up_needle == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_needle = 1
        elif player_position_tuple == plastic_tube_position\
                and self.picked_up_plastic_tube == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_plastic_tube = 1

        #victory condition
        if player_position_tuple == exit_position:
            victory = pygame.image.load("sprites/victory.png").convert()
            window.blit(victory, (200, 200))
            print("victory")
            pygame.display.flip()
            self.keep_playing = 0
        #defeat condition
        elif player_position_tuple == guardian_position\
                and self.victory_condition_marquer != "VVV":
            defeat = pygame.image.load("sprites/defeat.png").convert()
            window.blit(defeat, (200, 200))
            print("defeat")
            pygame.display.flip()
            self.keep_playing = 0


class Game:
    """This is the main class that contains most of the sprites info,
    the HUD scripts to display it and call the methods from the other classes
    to make the game work."""

    WINDOW = pygame.display.set_mode((761, 600))
    FLOOR = pygame.image.load("sprites/floor.png").convert()
    ETHER = pygame.image.load("sprites/ether.png").convert()
    NEEDLE = pygame.image.load("sprites/aiguille.png").convert()
    PLASTIC_TUBE = pygame.image.load("sprites/tube_plastique.png").convert()
    HUD_DIGIT_HEADER = pygame.image.load("sprites/level_number.png").convert()
    HUD_DIGIT_ONE = pygame.image.load("sprites/HUD_1.png").convert()
    HUD_DIGIT_TWO = pygame.image.load("sprites/HUD_2.png").convert()
    HUD_DIGIT_THREE = pygame.image.load("sprites/HUD_3.png").convert()
    HUD_DIGIT_FOUR = pygame.image.load("sprites/HUD_4.png").convert()
    HUD_BACKGROUND = pygame.image.load("sprites/HUD_brackground.png").\
        convert()
    HUD_CONTROL_SCHEME = pygame.image.load("sprites/controls.png").convert()
    HUD_GAME_RULES = pygame.image.load("sprites/rules.png").convert()
    HUD_DIGIT_HEADER.set_colorkey((255, 0, 255))
    HUD_DIGIT_ONE.set_colorkey((255, 0, 255))
    HUD_DIGIT_TWO.set_colorkey((255, 0, 255))
    HUD_DIGIT_THREE.set_colorkey((255, 0, 255))
    HUD_DIGIT_FOUR.set_colorkey((255, 0, 255))
    HUD_CONTROL_SCHEME.set_colorkey((255, 0, 255))
    ETHER.set_colorkey((255, 0, 255))
    NEEDLE.set_colorkey((255, 0, 255))
    PLASTIC_TUBE.set_colorkey((255, 0, 255))

    def __init__(self):
        self.labyrinth_generation = LabyrinthGeneration()
        self.character_control = Player()

    def game_init(self):
        """method that initialise the game which mean creating and displaying
        the labyrinth, displaying the HUD and initialisation of the player
        starting point."""

        #labyrinth layout (floor, walls and items) and display initialisation
        self.labyrinth_generation.labyrinth_randomiser()
        self.labyrinth_generation.selected_labyrinth_scan(self.FLOOR,
                                                          self.WINDOW)
        self.labyrinth_generation.item_placement_display(self.WINDOW,
                                                         self.ETHER,
                                                         self.NEEDLE,
                                                         self.PLASTIC_TUBE)

        #HUD initialisation
        self.WINDOW.blit(self.HUD_BACKGROUND, (601, 0))
        self.WINDOW.blit(self.HUD_GAME_RULES, (601, 75))
        self.WINDOW.blit(self.HUD_CONTROL_SCHEME, (601, 462))
        self.WINDOW.blit(self.HUD_DIGIT_HEADER, (601, 0))
        width = 641
        for number in self.labyrinth_generation.labyrinth_selected:
            if number == "1":
                self.WINDOW.blit(self.HUD_DIGIT_ONE, (width, 28))
            elif number == "2":
                self.WINDOW.blit(self.HUD_DIGIT_TWO, (width, 28))
            elif number == "3":
                self.WINDOW.blit(self.HUD_DIGIT_THREE, (width, 28))
            else:
                self.WINDOW.blit(self.HUD_DIGIT_FOUR, (width, 28))
            width += 20

        #player initialisation
        self.character_control.player_generation()
        self.WINDOW.blit(self.character_control.player_picture,
                         self.character_control.player_position)

    def game_loop(self):
        """Method that made the game loop."""

        pygame.key.set_repeat(400, 30)
        while self.character_control.keep_playing:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.character_control.keep_playing = 0
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.character_control.move_down(
                            self.labyrinth_generation.layout, self.FLOOR,
                            self.WINDOW)
                    elif event.key == K_UP:
                        self.character_control.move_up(
                            self.labyrinth_generation.layout, self.FLOOR,
                            self.WINDOW)
                    elif event.key == K_RIGHT:
                        self.character_control.move_right(
                            self.labyrinth_generation.layout, self.FLOOR,
                            self.WINDOW)
                    elif event.key == K_LEFT:
                        self.character_control.move_left(
                            self.labyrinth_generation.layout, self.FLOOR,
                            self.WINDOW)
                    elif event.key == K_q:
                        self.character_control.keep_playing = 0
                    self.character_control.victory_condition(
                        self.WINDOW, self.labyrinth_generation.ether_position,
                        self.labyrinth_generation.needle_position,
                        self.labyrinth_generation.plastic_tube_position)
