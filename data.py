"""Game data, can be modified without breaking the game"""

#  The labyrinth structure:
#  W = Wall tile
#  F = Floor tile
#  P = Player
#  G = gardian
#  E = exit
#  North west corner is a 8 x 8 square
NW_LABYRINTH_PART_ONE = [
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
NW_LABYRINTH_PART_TWO = [
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
NW_LABYRINTH_PART_THREE = [
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
NW_LABYRINTH_PART_FOUR = [
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
#  North east corner is a 7 x 8 square
NE_LABYRINTH_PART_ONE = [
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
NE_LABYRINTH_PART_TWO = [
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
NE_LABYRINTH_PART_THREE = [
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
NE_LABYRINTH_PART_FOUR = [
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
#  South west corner is a 8 x 7 square
SW_LABYRINTH_PART_ONE = [
    "WFWFFFFF",
    "WFWFWWFW",
    "WFWFFWWW",
    "WFFFFFFF",
    "WWWFWWFW",
    "WFFFFWFW",
    "WWWWWWWW",
    "1"
]
SW_LABYRINTH_PART_TWO = [
    "WFFFFFFF",
    "WFWFFWFW",
    "WWWWWWFW",
    "WFFWFFFF",
    "WWFWWWFW",
    "WFFFFFFW",
    "WWWWWWWW",
    "2"
]
SW_LABYRINTH_PART_THREE = [
    "WFFFWFFF",
    "WWWFWFWW",
    "WFFFWWWW",
    "WFWFFFFW",
    "WWWWWWFW",
    "WFFFFFFF",
    "WWWWWWWW",
    "3"
]
SW_LABYRINTH_PART_FOUR = [
    "WFFFWFFW",
    "WFWFFWFF",
    "WFWWFWWW",
    "WFFWFFFF",
    "WWFWWWFW",
    "WFFFFFFW",
    "WWWWWWWW",
    "4"
]
#  South east corner is a 7 x 7 square
SE_LABYRINTH_PART_ONE = [
    "FWFWWFW",
    "FFFFWFW",
    "FWWWWWW",
    "FWFFFFW",
    "FWFWWFW",
    "FFFFWGW",
    "WWWWWEW",
    "1"
]
SE_LABYRINTH_PART_TWO = [
    "FFFFFFW",
    "FWWFWFW",
    "FWFFWFW",
    "FWFWFFW",
    "FWWWWFW",
    "FFFFWGW",
    "WWWWWEW",
    "2"
]
SE_LABYRINTH_PART_THREE = [
    "FFFFFFW",
    "FFWFWFW",
    "WWWWWFW",
    "WFFFFFW",
    "WWFWFWW",
    "WFFWFGW",
    "WWWWWEW",
    "3"
]
SE_LABYRINTH_PART_FOUR = [
    "FWWWWWW",
    "FFFFWFW",
    "FWFWWFW",
    "FWFFFFW",
    "FWFWWWW",
    "FWFFFGW",
    "WWWWWEW",
    "4"
]
NW_LABYRINTH_PARTS = [
    NW_LABYRINTH_PART_ONE,
    NW_LABYRINTH_PART_TWO,
    NW_LABYRINTH_PART_THREE,
    NW_LABYRINTH_PART_FOUR
]
NE_LABYRINTH_PARTS = [
    NE_LABYRINTH_PART_ONE,
    NE_LABYRINTH_PART_TWO,
    NE_LABYRINTH_PART_THREE,
    NE_LABYRINTH_PART_FOUR
]
SW_LABYRINTH_PARTS = [
    SW_LABYRINTH_PART_ONE,
    SW_LABYRINTH_PART_TWO,
    SW_LABYRINTH_PART_THREE,
    SW_LABYRINTH_PART_FOUR,
]
SE_LABYRINTH_PARTS = [
    SE_LABYRINTH_PART_ONE,
    SE_LABYRINTH_PART_TWO,
    SE_LABYRINTH_PART_THREE,
    SE_LABYRINTH_PART_FOUR,
]

#  0, 0 being the top left corner and 14, 14 the bottom right

#  A tile is 40 pixels wide and 40 pixels tall so the cordinate for each
#  sprite is multiplied by 40
MACGYVER_STARTING_POSITION = (1 * 40, 1 * 40)
GUARDIAN_POSITION = (13 * 40, 13 * 40)
EXIT_POSITION = (13 * 40, 14 * 40)
