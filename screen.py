import pygame
from constants import *
import random
import game_field
import teleport

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

imp = pygame.image.load('grass.png')
img = pygame.transform.scale(imp, (3 * CELL_SIZE, 2 * CELL_SIZE))

flag_image = pygame.image.load(r'flag.png')
flag_img = pygame.transform.scale(flag_image, (FLAG_COLS * CELL_SIZE, FLAG_ROWS * CELL_SIZE))

grass_positions = []
for i in range(NUM_GRASS):
    gx = random.randint(0, WINDOW_WIDTH - (3 * CELL_SIZE))
    gy = random.randint(0, WINDOW_HEIGHT - (2 * CELL_SIZE))
    grass_positions.append((gx, gy))

field_matrix, level_mines = game_field.generate_mines(NUM_OF_MINES)
field_matrix, level_traps = teleport.generate_traps(TRAP_COUNT)


def create_screen():
    """setting up the game window title"""
    pygame.display.set_caption('The flag')


def draw_grass():
    """drawing the grass where we randomized it"""
    for pos in grass_positions:
        screen.blit(img, pos)


def draw_flag():
    """drawing the flag"""
    flag_x = WINDOW_WIDTH - (FLAG_COLS * CELL_SIZE)
    flag_y = WINDOW_HEIGHT - (FLAG_ROWS * CELL_SIZE)
    screen.blit(flag_img, (flag_x, flag_y))


def draw_mines_on_screen():
    """drawing the generated mines from the static list onto the screen"""
    game_field.draw_mines(screen, level_mines)

def draw_traps_on_screen():
    """drawing the generated traps from the static list onto the screen"""
    game_field.draw_mines(screen, level_traps)


def drawGrid():
    """drawing the visual grid lines across the field"""
    screen.fill(BLACK)  # clears the background to black for the grid view
    blockSize = CELL_SIZE
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, GREEN, rect, 1)
