from random import randrange

import pygame
from pygame.locals import *

from data import NW_LABYRINTH_PARTS, NE_LABYRINTH_PARTS, SW_LABYRINTH_PARTS,\
SE_LABYRINTH_PARTS, GUARDIAN_POSITION, EXIT_POSITION,\
MACGYVER_STARTING_POSITION



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
        """Method that select four pre-made labyrinth parts and put
        them together to create the labyrinth."""
        string_nb = 0
        nw_labyrinth_parts_save = NW_LABYRINTH_PARTS.copy()
        north_west = nw_labyrinth_parts_save.pop(randrange(len(
            nw_labyrinth_parts_save)))
        ne_labyrinth_parts_save = NE_LABYRINTH_PARTS.copy()
        north_east = ne_labyrinth_parts_save.pop(randrange(len(
            ne_labyrinth_parts_save)))
        while string_nb != 8:
            self.layout.append(north_west[string_nb] + north_east[string_nb])
            string_nb += 1
        string_nb = 0
        sw_labyrinth_parts_save = SW_LABYRINTH_PARTS.copy()
        south_west = sw_labyrinth_parts_save.pop(randrange(len(
            sw_labyrinth_parts_save)))
        se_labyrinth_parts_save = SE_LABYRINTH_PARTS.copy()
        south_east = se_labyrinth_parts_save.pop(randrange(len(
            se_labyrinth_parts_save)))
        while string_nb != 7:
            self.layout.append(south_west[string_nb] + south_east[string_nb])
            string_nb += 1
        self.labyrinth_selected = north_west[8] + north_east[8]\
        + south_west[7] + south_east[7]

    def selected_labyrinth_scan(self, floor, window):
        """Method that scan the labyrinth created by the method
        'labyrinth_randomiser' and display either a floor, a wall, the
        guardian or the exit tile for each coordinate. Also create a
        list for possible item position spawn during the scan."""

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
                    #3 wall tiles.
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
        window.blit(guardian, GUARDIAN_POSITION)
        window.blit(exit_labyrinth, EXIT_POSITION)

    def item_placement_display(self, window, ether, needle, plastic_tube):
        """Method that randomly choose a position for each item base on
        a list made by the 'selected_labyrinth_scan' method and display
        them."""

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
    """class that put and move the player in the labyrinth. Also check
    and keep infos about items taken, update the HUD and if victory
    conditions are met."""

    SYRINGE = pygame.image.load("sprites/seringue.png")
    SYRINGE.set_colorkey((255, 0, 255))

    def __init__(self):
        self.player_picture = pygame.image.load("sprites/MacGyver.png").\
            convert()
        self.player_picture.set_colorkey((255, 0, 255))
        self.player_position = 0
        self.picked_up_ether = 0
        self.picked_up_needle = 0
        self.picked_up_plastic_tube = 0
        self.victory_condition_marquer = ""
        self.end_game = 0

    def player_generation(self):
        """Method that put the player on the starting position. only
        called when initialising the labyrinth."""

        self.player_position = self.player_picture.get_rect()
        self.player_position = self.player_position.move(
            MACGYVER_STARTING_POSITION)

    def move_down(self, layout, floor, window):
        """Method that make the player move down if the down arrow key
        is pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40 + 1]\
                [self.player_position[0] // 40] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(0, 40)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def move_up(self, layout, floor, window):
        """Method that make the player move up if the up arrow key is
        pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40 - 1]\
                [self.player_position[0] // 40] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(0, -40)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def move_right(self, layout, floor, window):
        """Method that make the player move right if the right arrow
        key is pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40]\
                [self.player_position[0] // 40 + 1] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(40, 0)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def move_left(self, layout, floor, window):
        """Method that make the player move left if the left arrow key
        is pressed unless there's a wall on the way."""

        if layout[self.player_position[1] // 40]\
                [self.player_position[0] // 40 - 1] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(-40, 0)
            window.blit(floor, self.player_position)
            window.blit(self.player_picture, self.player_position)

    def victory_condition(self, window, ether_position, needle_position,
                          plastic_tube_position):
        """Method that update which items are taken and if the victory
        conditions are met when encountering the guardian. This method
        also stop the game if you're on the exit position (victory) or
        if you're on the guardian position without having every item
        (defeat)."""

        player_position = (
            self.player_position[0], self.player_position[1]
        )
        if player_position == ether_position\
                and self.picked_up_ether == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_ether = 1
        elif player_position == needle_position\
                and self.picked_up_needle == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_needle = 1
        elif player_position == plastic_tube_position\
                and self.picked_up_plastic_tube == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_plastic_tube = 1

        key_pressed = 1
        #victory conditions
        if player_position == EXIT_POSITION:
            victory = pygame.image.load("sprites/victory.png").convert()
            self.end_game = 1
            window.blit(victory, (200, 200))
            pygame.display.flip()
            while key_pressed:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        key_pressed = 0
        #defeat conditions
        elif player_position == GUARDIAN_POSITION\
                and self.victory_condition_marquer != "VVV":
            self.end_game = 1
            defeat = pygame.image.load("sprites/defeat.png").convert()
            window.blit(defeat, (200, 200))
            pygame.display.flip()
            while key_pressed:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        key_pressed = 0

    def hud_update(self, window, needle, ether, plastic_tube):
        """method that update the HUD if items are taken"""

        if self.victory_condition_marquer == "VVV":
            window.blit(self.SYRINGE, (601, 380))
        else:
            if self.picked_up_needle:
                window.blit(needle, (621, 390))
            if self.picked_up_ether:
                window.blit(ether, (661, 390))
            if self.picked_up_plastic_tube:
                window.blit(plastic_tube, (701, 390))


class Game:
    """This is the main class that contains most of the sprites info,
    the HUD scripts to display it and call the methods from the other
    classes to make the game work."""

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
    HUD_INVENTORY = pygame.image.load("sprites/inventory.png").convert()
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
        self.keep_playing = 1
        self.reset_game = 0

    def game_init(self):
        """method that initialise the game which mean creating and
        displaying the labyrinth, displaying the HUD and initialisation
        of the player starting point."""

        #labyrinth layout (floor, walls and items) and display initialisation
        pygame.init()
        pygame.time.Clock().tick(30)
        self.labyrinth_generation.labyrinth_randomiser()
        self.labyrinth_generation.selected_labyrinth_scan(self.FLOOR,
                                                          self.WINDOW)
        self.labyrinth_generation.item_placement_display(
            self.WINDOW, self.ETHER, self.NEEDLE, self.PLASTIC_TUBE)

        #HUD initialisation, background is only useful when reseting the game
        self.WINDOW.blit(self.HUD_BACKGROUND, (601, 0))
        self.WINDOW.blit(self.HUD_BACKGROUND, (601, 350))
        self.WINDOW.blit(self.HUD_INVENTORY, (611, 350))
        self.WINDOW.blit(self.HUD_GAME_RULES, (601, 75))
        self.WINDOW.blit(self.HUD_CONTROL_SCHEME, (601, 462))
        self.WINDOW.blit(self.HUD_DIGIT_HEADER, (601, 0))
        pixel_length_position = 641
        for number in self.labyrinth_generation.labyrinth_selected:
            if number == "1":
                self.WINDOW.blit(self.HUD_DIGIT_ONE, (pixel_length_position,
                                                      28))
            elif number == "2":
                self.WINDOW.blit(self.HUD_DIGIT_TWO, (pixel_length_position,
                                                      28))
            elif number == "3":
                self.WINDOW.blit(self.HUD_DIGIT_THREE, (pixel_length_position,
                                                        28))
            else:
                self.WINDOW.blit(self.HUD_DIGIT_FOUR, (pixel_length_position,
                                                       28))
            pixel_length_position += 20

        #player initialisation
        self.character_control.player_generation()
        self.WINDOW.blit(self.character_control.player_picture,
                         self.character_control.player_position)

    def game_loop(self):
        """Method that made the game play and loop."""

        while self.reset_game != 1 and self.keep_playing:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.keep_playing = 0
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
                        self.keep_playing = 0
                    self.character_control.victory_condition(
                        self.WINDOW, self.labyrinth_generation.ether_position,
                        self.labyrinth_generation.needle_position,
                        self.labyrinth_generation.plastic_tube_position)
                    if self.character_control.end_game:
                        self.reset_game = 1
                    self.character_control.hud_update(
                        self.WINDOW, self.NEEDLE, self.ETHER, self.PLASTIC_TUBE
                    )
