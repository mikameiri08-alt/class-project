import pygame
from constants import SOLDIER_COLS,CELL_SIZE,SOLDIER_ROWS,WINDOW_WIDTH,SOLDIER_BODY_ROWS,GUARD_Y

guard_image = pygame.image.load(r'guard.png')
guard_img = pygame.transform.scale(guard_image,
                                     (SOLDIER_COLS * CELL_SIZE,
                                      SOLDIER_ROWS * CELL_SIZE))
def draw_guard(player_x, player_y, screen):
    """Draws the soldier on the screen"""
    screen.blit(guard_img, (player_x, player_y))


def touched_guard(player_x, player_y, guard_x, guard_y):
    body_rect = pygame.Rect(player_x, player_y,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_BODY_ROWS * CELL_SIZE)

    flag_rect = pygame.Rect(guard_x, guard_y,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_BODY_ROWS * CELL_SIZE)

    return body_rect.colliderect(flag_rect)

def move_guard(guard_x, GUARD_Y):
    