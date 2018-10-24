"""Games data, can be modified without breaking the game"""


#The labyrinth structure:
#W = Wall tile
#F = Floor tile

level = [
    "WWWWWWWWWWWWWWW",
    "WFWFFFWFFFFFFFW",
    "WFWWWFWFWFWWWFW",
    "WFWFWFWFWFFFWFW",
    "WFFFFFFFWFWWWFW",
    "WWWFWWWFWFFFWFW",
    "WFWFWFWWWFWWWFW",
    "WFFFFFFWFFWFFFW",
    "WWWWFWWWFWWWWFW",
    "WFFFFWFFFFFFWFW",
    "WWFWWWWWFWWWWWW",
    "WFFWFFFFFWFFFFW",
    "WWWWWWFWFWFWWFW",
    "WFFFFFFWFFFFWFW",
    "WWWWWWWWWWWWWWW"
]

#0, 0 being the top left corner and 14, 14 the bottom right
#each item should be put in a dead end, you should modifie this list
#if you modifie the labyrinth above
possible_item_position = [
    (3 * 40, 1 * 40), (3 * 40, 3 * 40), (4 * 40, 11 * 40), (5 * 40, 6 * 40),
    (6 * 40, 7 * 40), (6 * 40, 9 * 40), (7 * 40, 5 * 40), (11 * 40, 3 * 40),
    (11 * 40, 5 * 40), (11 * 40, 7 * 40), (11 * 40, 9 * 40),
    (11 * 40, 13 * 40), (13 * 40, 9 * 40)
]

#a tile is 40 pixels wide so the cordinate for each sprite is multiplied by 40
MacGyver_starting_position = (1 * 40, 1 * 40) 
guardian_position = (13 * 40, 13 * 40)