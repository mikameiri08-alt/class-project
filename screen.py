import pygame
from constants import *
import random

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# יצירת מסך
def create_screen():
    background_colour =SCREEN_COLOR
    pygame.display.set_caption('The flag')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




def draw_grass():
    imp = pygame.image.load('grass.png')
    img = pygame.transform.scale(imp, (6 * CELL_SIZE, 4 * CELL_SIZE))


    for i in range (20):
        x=random.randint(0,WINDOW_WIDTH-10)
        y=random.randint(0,WINDOW_HEIGHT-10)
        screen.blit(img, (x,y))



