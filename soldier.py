import pygame
from constants import *
from screen import screen

# טעינת תמונת החייל ושינוי גודל פעם אחת מראש
soldier_image = pygame.image.load(r'soldier.png')
soldier_img = pygame.transform.scale(soldier_image,
                                      (SOLDIER_COLS * CELL_SIZE,
                                       SOLDIER_ROWS * CELL_SIZE))

def move_soldier(x, y, event, velocity=12):
    """
    מזיזה את החייל על סמך לחיצות מקשים.
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


    return x, y


def draw_soldier(x, y):
    """מציירת את החייל על המסך במיקום הנוכחי שלו"""
    screen.blit(soldier_img, (x, y))

def touched_mine(player_x, player_y, mine_x, mine_y):
    """בדיקה האם רגלי החייל נוגעות במוקש מסוים"""
    # הרגליים מתחילות מתחת לגוף (מורידים את גובה הגוף בפיקסלים)
    legs_y = player_y + (SOLDIER_BODY_ROWS * CELL_SIZE)

    legs_rect = pygame.Rect(player_x, legs_y,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_FEET_ROWS * CELL_SIZE)

    # המוקש באורך 3 משבצות אופקית (כפי שהגדרנו ב-game_field)
    mine_rect = pygame.Rect(mine_x, mine_y,
                            3 * CELL_SIZE,
                            MINE_ROWS * CELL_SIZE)

    return legs_rect.colliderect(mine_rect)

def touched_flag(player_x, player_y, flag_x, flag_y):
    """בדיקה האם גוף החייל נוגע בדגל"""
    body_rect = pygame.Rect(player_x, player_y,
                            SOLDIER_COLS * CELL_SIZE,
                            SOLDIER_BODY_ROWS * CELL_SIZE)

    # יצירת מלבן הדגל בפיקסלים (החלפנו לרוחב ואז גובה)
    flag_rect = pygame.Rect(flag_x, flag_y,
                            FLAG_COLS * CELL_SIZE,
                            FLAG_ROWS * CELL_SIZE)

    return body_rect.colliderect(flag_rect)
