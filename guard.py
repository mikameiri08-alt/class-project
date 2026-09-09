import pygame
from constants import *

guard_image = pygame.image.load(r'guard.png')
guard_img = pygame.transform.scale(guard_image,
                                   (GUARD_COLS * CELL_SIZE,
                                    GUARD_ROWS * CELL_SIZE))

def draw_guard(guard_row, guard_col, screen):
    """Draws the guard on the screen at the correct pixel coordinates"""
    x = GUARD_START_ROW
    y = GUARD_START_COL

    screen.blit(guard_img, (x, y))


def touched_guard(player_x, player_y, guard_x, GUARD_START_ROW):
    """Checking whether the player's body is touching the guard"""
    body_rect = pygame.Rect(player_x, player_y,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_BODY_ROWS * CELL_SIZE)

    guard_rect = pygame.Rect(guard_x, GUARD_START_ROW,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_BODY_ROWS * CELL_SIZE)

    return body_rect.colliderect(guard_rect)


def move_guard_right(guard_x):
    guard_x += CELL_SIZE

def move_guard_left(guard_x):
    guard_x -=CELL_SIZE