import pygame
from constants import *
import random

teleport_image = pygame.image.load('teleport.png')
teleport_img = pygame.transform.scale(teleport_image,
                                      (3 * CELL_SIZE, TRAP_ROWS * CELL_SIZE))


def generate_traps(num_of_traps):
    """Grids locations for traps of length 3 and returns the matrix and list of coordinates"""
    field = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    trap_positions = []

    all_possible_positions = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 2):
            # Preventing the planting of traps in the area of the soldier's first steps
            if row < SOLDIER_ROWS and col < SOLDIER_COLS:
                continue
            all_possible_positions.append((row, col))

    sampled_positions = random.sample(all_possible_positions, min(num_of_traps,
                                                                  len(all_possible_positions)))

    for row, col in sampled_positions:
        field[row][col] = 1
        field[row][col + 1] = 1
        field[row][col + 2] = 1
        trap_positions.append((row, col))

    return field, trap_positions


def check_trap_collision(player_x, player_y, trap_positions):
    """Checks whether the soldier's feet are touching one of the traps"""
    legs_y = player_y + (SOLDIER_BODY_ROWS * CELL_SIZE)
    legs_rect = pygame.Rect(player_x, legs_y, SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_FEET_ROWS * CELL_SIZE)

    for row, col in trap_positions:
        trap_x = col * CELL_SIZE
        trap_y = row * CELL_SIZE
        trap_rect = pygame.Rect(trap_x, trap_y, 3 * CELL_SIZE,
                                TRAP_ROWS * CELL_SIZE)

        if legs_rect.colliderect(trap_rect):
            return True
    return False


def teleport_player(player_x, player_y, trap_positions):
    """Teleports the player to a random safe cell on the board if they hit a trap"""
    if check_trap_collision(player_x, player_y, trap_positions):
        print("You stepped on a teleport trap!")

        random_col = random.randint(0, BOARD_COLS - SOLDIER_COLS)
        random_row = random.randint(0, BOARD_ROWS - SOLDIER_ROWS)

        player_x = random_col * CELL_SIZE
        player_y = random_row * CELL_SIZE

    return player_x, player_y
