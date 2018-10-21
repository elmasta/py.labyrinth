import pygame
from data import *
from random import randrange
from pygame.locals import *

window = pygame.display.set_mode((600, 600))
floor = pygame.image.load("sprites/floor.png").convert()
picked_up_ether = 0
picked_up_needle = 0
picked_up_syringe = 0
picked_up_plastic_tube = 0
victory_condition_marquer = ""

def create_labyrinth(labyrinth_patern):

    x = 0
    string = 0

    wall = pygame.image.load("sprites/walls.png").convert()
    guardian = pygame.image.load("sprites/Gardien.png").convert()
    guardian.set_colorkey((255, 0, 255))

    while string != 15:
        for element in labyrinth_patern[string]:
            if element is "W":
                window.blit(wall, (x * 40, string * 40))
            else:
                window.blit(floor, (x * 40, string * 40))
            x += 1
        string += 1
        x = 0

    window.blit(guardian, guardian_position)
    pygame.display.flip()

def item_placement():

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
    window.blit(ether, ether_position)
    window.blit(needle, needle_position)
    window.blit(syringe, syringe_position)
    window.blit(plastic_tube, plastic_tube_position)
    return ether_position, needle_position, syringe_position , plastic_tube_position

def create_player():
    
    player = pygame.image.load("sprites/MacGyver.png").convert()
    player.set_colorkey((255, 0, 255))
    player_position = player.get_rect()
    player_position = player_position.move(MacGyver_starting_position)
    window.blit(player, MacGyver_starting_position)
    pygame.display.flip()
    return player_position, player


def victory_condition(ether_position, needle_position, syringe_position, 
                      plastic_tube_position, player_position):

    global picked_up_ether
    global picked_up_needle
    global picked_up_syringe
    global picked_up_plastic_tube
    global victory_condition_marquer
    
    player_position_tuple = (player_position[0], player_position[1])
    if player_position_tuple == ether_position and picked_up_ether == 0:
        victory_condition_marquer += "V"
        picked_up_ether = 1
    elif player_position_tuple == needle_position and picked_up_needle == 0:
        victory_condition_marquer += "V"
        picked_up_needle = 1
    elif player_position_tuple == syringe_position and picked_up_syringe == 0:
        victory_condition_marquer += "V"
        picked_up_syringe = 1
    elif player_position_tuple == plastic_tube_position and\
            picked_up_plastic_tube == 0:
        victory_condition_marquer += "V"
        picked_up_plastic_tube = 1
    if player_position_tuple == guardian_position and \
            victory_condition_marquer == "VVVV":
        print("victory")
        return 0
    elif player_position_tuple == guardian_position:
        print("defeat")
        return 0
    else:
        return 1