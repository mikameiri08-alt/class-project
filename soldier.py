import pygame
from constants import *
# from screen import *


def move_soldier(x, y, event, velocity=12):
    """
    מזיזה את החייל על סמך לחיצות מקשים ושומרת עליו בתוך גבולות המסך.
    מחזירה את ה-x וה-y המעודכנים של החייל.
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x -= velocity
        if event.key == pygame.K_RIGHT:
            x += velocity
        if event.key == pygame.K_UP:
            y -= velocity
        if event.key == pygame.K_DOWN:
            y += velocity

    # --- מנגנון חסימת יציאה מגבולות המסך ---
    # חסימה משמאל ומלמעלה
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    # חסימה מימין ומלמטה (מתחשב בגודל החייל בפיקסלים)
    soldier_width = SOLDIER_COLS * CELL_SIZE
    soldier_height = SOLDIER_ROWS * CELL_SIZE

    if x + soldier_width > WINDOW_WIDTH:
        x = WINDOW_WIDTH - soldier_width
    if y + soldier_height > WINDOW_HEIGHT:
        y = WINDOW_HEIGHT - soldier_height

    return x, y


def draw_soldier(START_X_PLAYER, START_Y_PLAYER,screen):
    """מציירת את החייל על המסך במיקום הנוכחי שלו"""
    soldier_image = pygame.image.load(r'soldier.png')
    soldier_img = pygame.transform.scale(soldier_image,
                                         (SOLDIER_COLS * CELL_SIZE,
                                          SOLDIER_ROWS * CELL_SIZE))

    screen.blit(soldier_img, (START_X_PLAYER, START_Y_PLAYER))


def check_mine_collision(player_x, player_y, mine_positions):
    """בודק האם רגלי החייל נוגעות באחד מהמוקשים ללא שימוש במחלקה"""
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
    """בדיקה האם גוף החייל נוגע בדגל"""
    body_rect = pygame.Rect(player_x, player_y,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_BODY_ROWS * CELL_SIZE)

    flag_rect = pygame.Rect(flag_x, flag_y,
                            FLAG_COLS * CELL_SIZE,
                            FLAG_ROWS * CELL_SIZE)

    return body_rect.colliderect(flag_rect)

