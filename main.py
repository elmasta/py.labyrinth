#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from func import *
from data import *
from pygame.locals import *

keep_playing = 1

pygame.init()
pygame.time.Clock().tick(30)
create_labyrinth(level)
player_position, player = create_player()
ether_position, needle_position, syringe_position, plastic_tube_position =\
    item_placement()
old_player_position = player_position

pygame.key.set_repeat(400, 30)
while keep_playing:
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_playing = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if level[player_position[1] // 40 + 1] \
                        [player_position[0] // 40] != "W":
                    player_position = player_position.move(0, 40)
                    keep_playing = victory_condition(ether_position, \
                        needle_position, syringe_position, plastic_tube_position, player_position)
            if event.key == K_UP:
                if level[player_position[1] // 40 - 1] \
                        [player_position[0] // 40] != "W":
                    player_position = player_position.move(0, -40)
                    keep_playing = victory_condition(ether_position, \
                        needle_position, syringe_position, plastic_tube_position, player_position)
            if event.key == K_RIGHT:
                if level[player_position[1] // 40] \
                        [player_position[0] // 40 + 1] != "W":
                    player_position = player_position.move(40, 0)
                    keep_playing = victory_condition(ether_position, \
                        needle_position, syringe_position, plastic_tube_position, player_position)
            if event.key == K_LEFT:
                if level[player_position[1] // 40] \
                        [player_position[0] // 40 - 1] != "W":
                    player_position = player_position.move(-40, 0)
                    keep_playing = victory_condition(ether_position, \
                        needle_position, syringe_position, plastic_tube_position, player_position)

    window.blit(floor, old_player_position)
    old_player_position = player_position
    window.blit(player, player_position)
    pygame.display.flip()