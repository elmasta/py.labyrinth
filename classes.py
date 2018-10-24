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

    def Display(self, floor, window):
        """Méthode permettant d'afficher le niveau en fonction
        de la liste de structure renvoyée par generer()"""        
        wall = pygame.image.load("sprites/walls.png").convert()
        guardian = pygame.image.load("sprites/Gardien.png").convert()
        guardian.set_colorkey((255, 0, 255))
        x = 0
        string = 0
        while string != 15:
            for element in self.layout[string]:
                if element is "W":
                    window.blit(wall, (x * 40, string * 40))
                else:
                    window.blit(floor, (x * 40, string * 40))
                x += 1
            string += 1
            x = 0
        window.blit(guardian, guardian_position)
        pygame.display.flip()

    def ItemPlacement(self, window):
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
        self.player_position = 0
        self.picked_up_ether = 0
        self.picked_up_needle = 0
        self.picked_up_sringe = 0
        self.picked_up_plastic_tube = 0
        self.victory_condition_marquer = ""
        self.keep_playing = 1


    def PlayerGeneration(self):
        player = pygame.image.load("sprites/MacGyver.png").convert()
        player.set_colorkey((255, 0, 255))
        player_position = player.get_rect()
        player_position = player_position.move(MacGyver_starting_position)
        window.blit(player, MacGyver_starting_position)
        pygame.display.flip()
        return player_position, player

    def PlayerMovement(self, layout, ether_position, needle_position, 
        syringe_position, plastic_tube_position):
        if event.key == K_DOWN:
            if level[player_position[1] // 40 + 1] \
                    [player_position[0] // 40] != "W":
                window.blit
                self.player_position = self.player_position.move(0, 40)
                keep_playing = victory_condition(
                    ether_position, needle_position, syringe_position,
                    plastic_tube_position, player_position
                )
        if event.key == K_UP:
            if level[player_position[1] // 40 - 1] \
                    [player_position[0] // 40] != "W":
                self.player_position = self.player_position.move(0, -40)
                keep_playing = victory_condition(
                    ether_position, needle_position, syringe_position,
                    plastic_tube_position, player_position
                )
        if event.key == K_RIGHT:
            if level[player_position[1] // 40] \
                    [player_position[0] // 40 + 1] != "W":
                self.player_position = self.player_position.move(40, 0)
                keep_playing = victory_condition(
                    ether_position, needle_position, syringe_position,
                    plastic_tube_position, player_position
                )
        if event.key == K_LEFT:
            if level[player_position[1] // 40] \
                    [player_position[0] // 40 - 1] != "W":
                self.player_position = self.player_position.move(-40, 0)
                keep_playing = victory_condition(
                    ether_position, needle_position, syringe_position,
                    plastic_tube_position, player_position
                )

    def VictoryCondition(self):
        player_position_tuple = (
            self.player_position[0], self.player_position[1]
        )
        if player_position_tuple == ether_position and\
                self.picked_up_ether == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_ether = 1
        elif player_position_tuple == needle_position and\
                self.picked_up_needle == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_needle = 1
        elif player_position_tuple == syringe_position and\
                self.picked_up_syringe == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_syringe = 1
        elif player_position_tuple == plastic_tube_position and\
                self.picked_up_plastic_tube == 0:
            self.victory_condition_marquer += "V"
            self.picked_up_plastic_tube = 1
        if player_position_tuple == guardian_position and \
                self.victory_condition_marquer == "VVVV":
            print("victory")
            self.keep_playing = 0
        elif player_position_tuple == guardian_position:
            print("defeat")
            self.keep_playing = 0

class Game:
    """Main class"""
    def __init__(self):
        self.labyrinth_generation = Generation()
        self.character_control = Player()
        floor = pygame.image.load("sprites/floor.png").convert()
        window = pygame.display.set_mode((600, 600))

    def GameInit(self):
        self.labyrinth_generation.Display(floor, window)
        self.labyrinth_generation.ItemPlacement(window)

    def GameLoop(self):
        pygame.key.set_repeat(400, 30)
        while self.character_control.keep_playing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.character_control.keep_playing = 0
                else:
                    self.character_control.PlayerMovement(
                        self.labyrinth_generation.layout,
                        self.labyrinth_generation.ether_position,
                        self.labyrinth_generation.needle_position,
                        self.labyrinth_generation.syringe_position,
                        self.labyrinth_generation.plastic_tube_position
                    )
                    self.character_control.VictoryCondition(
                        self.labyrinth_generation.ether_position,
                        self.labyrinth_generation.needle_position,
                        self.labyrinth_generation.syringe_position,
                        self.labyrinth_generation.plastic_tube_position                       
                        )
