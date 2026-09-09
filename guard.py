import pygame
from constants import *

guard_image = pygame.image.load(r'guard.png')
guard_img = pygame.transform.scale(guard_image,
                                   (GUARD_COLS * CELL_SIZE,
                                    GUARD_ROWS * CELL_SIZE))

def draw_guard(guard_row, guard_x_pixels, screen):
    """Draws the guard using raw pixel coordinates directly."""
    y = guard_row * CELL_SIZE
    screen.blit(guard_img, (guard_x_pixels, y))


def touched_guard(player_x, player_y, guard_x_pixels, guard_row):
    """Checks guard collision using raw pixel rect matching."""
    player_rect = pygame.Rect(player_x, player_y,
                              SOLDIER_COLS * CELL_SIZE,
                              SOLDIER_ROWS * CELL_SIZE)

    y = guard_row * CELL_SIZE
    guard_rect = pygame.Rect(guard_x_pixels, y,
                             GUARD_COLS * CELL_SIZE,
                             GUARD_ROWS * CELL_SIZE)

    return player_rect.colliderect(guard_rect)


def move_guard_right(guard_x_pixels):
    """Moves the guard smoothly to the right by a small pixel step."""
    guard_x_pixels += 4  # Moves 4 pixels every frame for smooth pacing
    return guard_x_pixels


def move_guard_left(guard_x_pixels):
    """Moves the guard smoothly to the left by a small pixel step."""
    guard_x_pixels -= 4
    return guard_x_pixels
