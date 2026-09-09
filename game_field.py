import pygame
import random
from constants import *

# Loading and resizing images
mine_image = pygame.image.load('mine.png')
mine_img = pygame.transform.scale(mine_image,
                                  (3 * CELL_SIZE, MINE_ROWS * CELL_SIZE))

flag_image = pygame.image.load('flag.png')
flag_img = pygame.transform.scale(flag_image,
                                  (FLAG_COLS * CELL_SIZE, FLAG_ROWS * CELL_SIZE))


def generate_mines(num_of_mines):
    """Grids locations for mines of length 3 and returns the matrix and list of coordinates"""
    field = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    mine_positions = []

    all_possible_positions = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 2):
            # Preventing the planting of mines in the area of the soldier's first steps
            if row < SOLDIER_ROWS and col < SOLDIER_COLS:
                continue
            all_possible_positions.append((row, col))

    sampled_positions = random.sample(all_possible_positions, min(num_of_mines,
                                                                  len(all_possible_positions)))

    for row, col in sampled_positions:
        field[row][col] = 1
        field[row][col + 1] = 1
        field[row][col + 2] = 1
        mine_positions.append((row, col))

    return field, mine_positions


def draw_mines(screen, mine_positions):
    """Draws all keys on the screen according to the list of locations."""
    for row, col in mine_positions:
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        screen.blit(mine_img, (x, y))


def get_flag_position():
    """Returns the position of the flag in pixels (bottom right corner of the panel)"""
    flag_x = WINDOW_WIDTH - (FLAG_COLS * CELL_SIZE)
    flag_y = WINDOW_HEIGHT - (FLAG_ROWS * CELL_SIZE)
    return flag_x, flag_y


def draw_flag(screen, flag_x, flag_y):
    """Draws the flag on the screen at its location"""
    screen.blit(flag_img, (flag_x, flag_y))

