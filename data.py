"""Games data, can be modified without breaking the game"""

#The labyrinth structure:
#W = Wall tile
#F = Floor tile
#P = Player
#G = gardian
#North west parts are 8 x 8
NW_labyrinth_part_one = [
    "WWWWWWWW",
    "WPWFFWFF",
    "WFFFWWFW",
    "WFWFWFFW",
    "WFWFFFFW",
    "WWWFWWFF",
    "WFFFWFFW",
    "WWWFWWWW",
    "1"
]
NW_labyrinth_part_two = [
    "WWWWWWWW",
    "WPFFWWFF",
    "WWWFFWFW",
    "WFWFWWFW",
    "WFFFFWFW",
    "WFWFWWFF",
    "WFWFFFFW",
    "WWWFWWWW",
    "2"
]
NW_labyrinth_part_three = [
    "WWWWWWWW",
    "WPFFFWFF",
    "WFWFWWFW",
    "WFWFWFFW",
    "WFFFFFWW",
    "WFWFWWFF",
    "WFWFFFFW",
    "WWWFWWWW",
    "3"
]
NW_labyrinth_part_four = [
    "WWWWWWWW",
    "WPWFFFFF",
    "WFFFWWWW",
    "WWFWFFFW",
    "WWFFFWFW",
    "WFWFWWFF",
    "WFFFWFFW",
    "WWWFWWWW",
    "4"
]
#North east parts are 7 x 8
NE_labyrinth_part_one = [
    "WWWWWWW",
    "FFFFFFW",
    "FWWWWFW",
    "FFFWFFW",
    "FWWWWFW",
    "FWFFFFW",
    "FFFWFFW",
    "WWFWWFW",
    "1"
]
NE_labyrinth_part_two = [
    "WWWWWWW",
    "FFFFFFW",
    "FWWWWFW",
    "FFFFWFW",
    "FWWWWFW",
    "FFFFWFW",
    "FWFWFFW",
    "WWFWWFW",
    "2"
]
NE_labyrinth_part_three = [
    "WWWWWWW",
    "FWFFFFW",
    "FWWFWFW",
    "FFWFWWW",
    "WFWFFFW",
    "FFFFWFW",
    "FWFWWFW",
    "WWFWWFW",
    "3"
]
NE_labyrinth_part_four = [
    "WWWWWWW",
    "FFFFFFW",
    "WFWWWFW",
    "FFFFWFW",
    "WFWWWFW",
    "WFFFWFW",
    "FFWFWFW",
    "WWFFWFW",
    "4"
]
#South west parts are 8 x 7
SW_labyrinth_part_one = [
    "WFWFFFFF",
    "WFWFWWFW",
    "WFWFFWWW",
    "WFFFFFFF",
    "WWWFWWFW",
    "WFFFFWFW",
    "WWWWWWWW",
    "1"
]
SW_labyrinth_part_two = [
    "WFFFFFFF",
    "WFWFFWFW",
    "WWWWWWFW",
    "WFFWFFFF",
    "WWFWWWFW",
    "WFFFFFFW",
    "WWWWWWWW",
    "2"
]
SW_labyrinth_part_three = [
    "WFFFWFFF",
    "WWWFWFWW",
    "WFFFWWWW",
    "WFWFFFFW",
    "WWWWWWFW",
    "WFFFFFFF",
    "WWWWWWWW",
    "3"
]
SW_labyrinth_part_four = [
    "WFFFWFFW",
    "WFWFFWFF",
    "WFWWFWWW",
    "WFFWFFFF",
    "WWFWWWFW",
    "WFFFFFFW",
    "WWWWWWWW",
    "4"
]
#South east parts are 7 x 7
SE_labyrinth_part_one = [
    "FWFWWFW",
    "FFFFWFW",
    "FWWWWWW",
    "FWFFFFW",
    "FWFWWFW",
    "FFFFWGW",
    "WWWWWWW",
    "1"
]
SE_labyrinth_part_two = [
    "FFFFFFW",
    "FWWFWFW",
    "FWFFWFW",
    "FWFWFFW",
    "FWWWWFW",
    "FFFFWGW",
    "WWWWWWW",
    "2"
]
SE_labyrinth_part_three = [
    "FFFFFFW",
    "WFWFWFW",
    "WWWWWFW",
    "WFFFFFW",
    "WWFWFWW",
    "WFFWFGW",
    "WWWWWWW",
    "3"
]
SE_labyrinth_part_four = [
    "WWWWWWW",
    "FFFFWFW",
    "FWFWWFW",
    "FWFFFFW",
    "FWFWWWW",
    "FWFFFGW",
    "WWWWWWW",
    "4"
]
NW_labyrinth_parts = [
    NW_labyrinth_part_one,
    NW_labyrinth_part_two,
    NW_labyrinth_part_three,
    NW_labyrinth_part_four
]
NE_labyrinth_parts = [
    NE_labyrinth_part_one,
    NE_labyrinth_part_two,
    NE_labyrinth_part_three,
    NE_labyrinth_part_four
]
SW_labyrinth_parts = [
    SW_labyrinth_part_one,
    SW_labyrinth_part_two,
    SW_labyrinth_part_three,
    SW_labyrinth_part_four,
]
SE_labyrinth_parts = [
    SE_labyrinth_part_one,
    SE_labyrinth_part_two,
    SE_labyrinth_part_three,
    SE_labyrinth_part_four,
]

#0, 0 being the top left corner and 14, 14 the bottom right
#each item should be put in a dead end, you should modifie this list
#if you modifie the labyrinth above
possible_item_position = [
    (1* 40, 6 * 40), (1 * 40, 9 * 40), (1 * 40, 11* 40), (1 * 40, 13* 40),
    (3 * 40, 1 * 40), (3 * 40, 3 * 40), (4 * 40, 11 * 40), (5 * 40, 6 * 40),
    (6 * 40, 7 * 40), (6 * 40, 9 * 40), (7 * 40, 5 * 40), (11 * 40, 3 * 40),
    (11 * 40, 5 * 40), (11 * 40, 7 * 40), (11 * 40, 9 * 40),
    (11 * 40, 13 * 40), (13 * 40, 9 * 40)
]

#a tile is 40 pixels wide so the cordinate for each sprite is multiplied by 40
MacGyver_starting_position = (1 * 40, 1 * 40)
guardian_position = (13 * 40, 13 * 40)
