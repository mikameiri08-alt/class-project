import pygame

from constants import SOLDIER_COLS,CELL_SIZE,SOLDIER_ROWS,WINDOW_WIDTH,SOLDIER_BODY_ROWS,GUARD_START_ROW

guard_image = pygame.image.load(r'guard.png')
guard_img = pygame.transform.scale(guard_image,
                                     (SOLDIER_COLS * CELL_SIZE,
                                      SOLDIER_ROWS * CELL_SIZE))
def draw_guard(GUARD_START_ROW, GUARD_START_COL, screen):
    """Draws the guard on the screen"""
    # screen.blit(guard_img, (GUARD_START_ROW, GUARD_START_COL))


def touched_guard(player_x, player_y, guard_x, GUARD_START_ROW):
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
