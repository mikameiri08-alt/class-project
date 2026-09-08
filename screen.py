import pygame
from constants import *



screen = pygame.display.set_mode((BOARD_ROWS, BOARD_COLS))

background_colour =SCREEN_COLOR
pygame.display.set_caption('Geeksforgeeks')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
