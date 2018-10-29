from random import randrange

import pygame
from pygame.locals import *

from data import *

class Generation:

    def __init__(self):
        self.layout = level
        self.ether_position = possible_item_position.pop(randrange(17))
        self.needle_position = possible_item_position.pop(randrange(16))
        self.syringe_position = possible_item_position.pop(randrange(15))
        self.plastic_tube_position = possible_item_position.pop(randrange(14))

    def fixed_elements_display(self, floor, window):
        """Méthode permettant d'afficher le niveau en fonction
        de la liste de structure renvoyée par generer()"""        
        wall = pygame.image.load("sprites/walls.png").convert()
        guardian = pygame.image.load("sprites/Gardien.png").convert()
        guardian.set_colorkey((255, 0, 255))
        list_index = 0
        string = 0
        while string != 15:
            for element in self.layout[string]:
                if element is "W":
                    window.blit(wall, (list_index * 40, string * 40))
                else:
                    window.blit(floor, (list_index * 40, string * 40))
                list_index += 1
            string += 1
            list_index = 0
        window.blit(guardian, guardian_position)

    def item_placement_display(self, window):
        ether = pygame.image.load("sprites/ether.png").convert()
        needle = pygame.image.load("sprites/aiguille.png").convert()
        syringe = pygame.image.load("sprites/seringue.png").convert()
        plastic_tube = pygame.image.load("sprites/tube_plastique.png").\
            convert()
        ether.set_colorkey((255, 0, 255))
        needle.set_colorkey((255, 0, 255))
        syringe.set_colorkey((255, 0, 255))
        plastic_tube.set_colorkey((255, 0, 255))
        window.blit(ether, self.ether_position)
        window.blit(needle, self.needle_position)
        window.blit(syringe, self.syringe_position)
        window.blit(plastic_tube, self.plastic_tube_position)

class Player:

    def __init__(self):
        self.player_picture = pygame.image.load("sprites/MacGyver.png").convert()
        self.player_picture.set_colorkey((255, 0, 255))
        self.player_position = 0
        self.player_position_tuple = 0
        self.picked_up_ether = 0
        self.picked_up_needle = 0
        self.picked_up_syringe = 0
        self.picked_up_plastic_tube = 0
        self.victory_condition_marquer = ""
        self.keep_playing = 1


    def player_generation(self):
        self.player_position = self.player_picture.get_rect()
        self.player_position = self.player_position.move(MacGyver_starting_position)

    def move_down(self, layout, floor, window):
        if layout[self.player_position[1] // 40 + 1] \
                [self.player_position[0] // 40] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(0, 40)
            window.blit(self.player_picture, self.player_position)

    def move_up(self, layout, floor, window):
        if layout[self.player_position[1] // 40 - 1] \
                [self.player_position[0] // 40] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(0, -40)
            window.blit(self.player_picture, self.player_position)

    def move_right(self, layout, floor, window):
        if layout[self.player_position[1] // 40] \
                [self.player_position[0] // 40 + 1] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(40, 0)
            window.blit(self.player_picture, self.player_position)

    def move_left(self, layout, floor, window):
        if layout[self.player_position[1] // 40] \
                [self.player_position[0] // 40 - 1] != "W":
            window.blit(floor, self.player_position)
            self.player_position = self.player_position.move(-40, 0)
            window.blit(self.player_picture, self.player_position)

    def victory_condition(self, ether_position, needle_position, 
                          syringe_position, plastic_tube_position):
        self.player_position_tuple = (
            self.player_position[0], self.player_position[1]
        )
        if self.player_position_tuple == ether_position and\
                self.picked_up_ether == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_ether = 1
        elif self.player_position_tuple == needle_position and\
                self.picked_up_needle == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_needle = 1
        elif self.player_position_tuple == syringe_position and\
                self.picked_up_syringe == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_syringe = 1
        elif self.player_position_tuple == plastic_tube_position and\
                self.picked_up_plastic_tube == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_plastic_tube = 1
        if self.player_position_tuple == guardian_position and \
                self.victory_condition_marquer == "VVVV":
            print("victory")
            self.keep_playing = 0
        elif self.player_position_tuple == guardian_position:
            print("defeat")
            self.keep_playing = 0

class Game:
    """Main class"""
    WINDOW = pygame.display.set_mode((600, 600))
    FLOOR = pygame.image.load("sprites/floor.png").convert()

    def __init__(self):
        self.labyrinth_generation = Generation()
        self.character_control = Player()

    def game_init(self):
        self.labyrinth_generation.fixed_elements_display(self.FLOOR, self.WINDOW)
        self.labyrinth_generation.item_placement_display(self.WINDOW)
        self.character_control.player_generation()
        self.WINDOW.blit(self.character_control.player_picture, self.character_control.player_position)

    def game_loop(self):
        pygame.key.set_repeat(400, 30)
        while self.character_control.keep_playing:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.character_control.keep_playing = 0
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.character_control.move_down(self.labyrinth_generation.layout, self.FLOOR, self.WINDOW)
                    elif event.key == K_UP:
                        self.character_control.move_up(self.labyrinth_generation.layout, self.FLOOR, self.WINDOW)
                    elif event.key == K_RIGHT:
                        self.character_control.move_right(self.labyrinth_generation.layout, self.FLOOR, self.WINDOW)
                    elif event.key == K_LEFT:
                        self.character_control.move_left(self.labyrinth_generation.layout, self.FLOOR, self.WINDOW)
                    self.character_control.victory_condition(
                        self.labyrinth_generation.ether_position,
                        self.labyrinth_generation.needle_position,
                        self.labyrinth_generation.syringe_position,
                        self.labyrinth_generation.plastic_tube_position
                    )
