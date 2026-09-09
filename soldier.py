import pygame
from constants import *

soldier_image = pygame.image.load(r'soldier.png')
soldier_img = pygame.transform.scale(soldier_image,
                                     (SOLDIER_COLS * CELL_SIZE,
                                      SOLDIER_ROWS * CELL_SIZE))


def move_soldier(x, y):
    """Moves the soldier based on keystrokes and keeps him within the screen boundaries.
     Returns the soldier's updated x and y, and whether Enter was pressed."""

    key = pygame.key.get_pressed()
    enter_pressed = False


    if key[pygame.K_LEFT]:
        x = x - CELL_SIZE
    elif key[pygame.K_RIGHT]:
        x = x + CELL_SIZE
    elif key[pygame.K_UP]:
        y = y - CELL_SIZE
    elif key[pygame.K_DOWN]:
        y = y + CELL_SIZE
    elif key[pygame.K_RETURN]:
        enter_pressed = True


    # Screen border blocking mechanism
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    soldier_width = SOLDIER_COLS * CELL_SIZE
    soldier_height = SOLDIER_ROWS * CELL_SIZE

    if x + soldier_width > WINDOW_WIDTH:
        x = WINDOW_WIDTH - soldier_width
    if y + soldier_height > WINDOW_HEIGHT:
        y = WINDOW_HEIGHT - soldier_height

    return x, y, enter_pressed


def draw_soldier(player_x, player_y, screen):
    """Draws the soldier on the screen"""
    screen.blit(soldier_img, (player_x, player_y))




def check_mine_collision(player_x, player_y, mine_positions):
    """Checks whether the soldier's feet are touching one of the mines"""
    legs_y = player_y + (SOLDIER_BODY_ROWS * CELL_SIZE)
    legs_rect = pygame.Rect(player_x, legs_y, SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_FEET_ROWS * CELL_SIZE)

    for row, col in mine_positions:
        mine_x = col * CELL_SIZE
        mine_y = row * CELL_SIZE
        mine_rect = pygame.Rect(mine_x, mine_y, 3 * CELL_SIZE,
                                MINE_ROWS * CELL_SIZE)

        if legs_rect.colliderect(mine_rect):
            return True
    return False


def touched_flag(player_x, player_y, flag_x, flag_y):
    """Checking whether the soldier's body is touching the flag"""
    body_rect = pygame.Rect(player_x, player_y,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_BODY_ROWS * CELL_SIZE)

    flag_rect = pygame.Rect(flag_x, flag_y,
                            FLAG_COLS * CELL_SIZE,
                            FLAG_ROWS * CELL_SIZE)

    return body_rect.colliderect(flag_rect)
