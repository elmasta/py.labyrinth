from random import randrange

import pygame
from pygame.locals import *

from data import *

floor = pygame.image.load("sprites/floor.png").convert()
window = pygame.display.set_mode((600, 600))

class Generation:

    def display(self):
        """Méthode permettant d'afficher le niveau en fonction 
        de la liste de structure renvoyée par generer()"""
        #Chargement des images (seule celle d'arrivée contient de la transparence)

        wall = pygame.image.load("sprites/walls.png").convert()
        guardian = pygame.image.load("sprites/Gardien.png").convert()
        guardian.set_colorkey((255, 0, 255))
        #On parcourt la liste du niveau
        x = 0
        string = 0
        while string != 15:
            for element in LEVEL[string]:
                if element is "W":
                    window.blit(wall, (x * 40, string * 40))
                else:
                    window.blit(floor, (x * 40, string * 40))
                x += 1
            string += 1
            x = 0
        window.blit(guardian, guardian_position)
        pygame.display.flip()