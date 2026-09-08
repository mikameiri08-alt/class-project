import random
from constants import *


def generate_mines(NUM_OF_MINES):
    field = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    all_possible_positions = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if row == 0 and col == 0:
                continue
            all_possible_positions.append((row, col))

    mine_positions = random.sample(all_possible_positions, NUM_OF_MINES)

    for row, col in mine_positions:
        field[row][col] = 1

    return field, mine_positions