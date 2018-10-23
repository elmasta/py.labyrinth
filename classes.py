from random import randrange

import pygame
from pygame.locals import *

from data import *

floor = pygame.image.load("sprites/floor.png").convert()
window = pygame.display.set_mode((600, 600))

class Generation:

    def __init__(self):
        self.layout = LEVEL
        self.ether_position = possible_item_position.pop(randrange(17))
        self.needle_position = possible_item_position.pop(randrange(16))
        self.syringe_position = possible_item_position.pop(randrange(15))
        self.plastic_tube_position = possible_item_position.pop(randrange(14))

    def Display(self):
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

    def ItemPlacement(self):

        ether = pygame.image.load("sprites/ether.png").convert()
        needle = pygame.image.load("sprites/aiguille.png").convert()
        syringe = pygame.image.load("sprites/seringue.png").convert()
        plastic_tube = pygame.image.load("sprites/tube_plastique.png").convert()
        ether.set_colorkey((255, 0, 255))
        needle.set_colorkey((255, 0, 255))
        syringe.set_colorkey((255, 0, 255))
        plastic_tube.set_colorkey((255, 0, 255))   
        ether_position = possible_item_position.pop(randrange(17))
        needle_position = possible_item_position.pop(randrange(16))
        syringe_position = possible_item_position.pop(randrange(15))
        plastic_tube_position = possible_item_position.pop(randrange(14))
        window.blit(ether, self.ether_position)
        window.blit(needle, self.needle_position)
        window.blit(syringe, self.syringe_position)
        window.blit(plastic_tube, self.plastic_tube_position)

class Player:

    def PlayerGeneration(self):
        player = pygame.image.load("sprites/MacGyver.png").convert()
        player.set_colorkey((255, 0, 255))
        player_position = player.get_rect()
        player_position = player_position.move(MacGyver_starting_position)
        window.blit(player, MacGyver_starting_position)
        pygame.display.flip()
        return player_position, player


    def PlayerMovement(self):

    def VictoryCondition(self):