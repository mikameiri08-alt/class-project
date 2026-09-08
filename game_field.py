import pygame
import random
from constants import *

mine_image = pygame.image.load('mine.png')
mine_img = pygame.transform.scale(mine_image,
                                  (3 * CELL_SIZE, MINE_ROWS * CELL_SIZE))


def generate_mines(num_of_mines):
    """מגריל מיקומים למוקשים באורך 3 ומחזיר את המטריצה ורשימת הקואורדינטות"""
    field = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    mine_positions = []

    all_possible_positions = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 2):
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
    """מצייר את כל המוקשים על המסך לפי רשימת המיקומים"""
    for row, col in mine_positions:
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        screen.blit(mine_img, (x, y))
