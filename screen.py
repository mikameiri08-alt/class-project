import pygame
from constants import *
import random
import game_field

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# יצירת מסך
def create_screen():
    background_colour =SCREEN_COLOR
    pygame.display.set_caption('The flag')
    screen.fill(background_colour)
    draw_grass()

    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




def draw_grass():

    imp = pygame.image.load('grass.png')
    img = pygame.transform.scale(imp, (3 * CELL_SIZE, 2 * CELL_SIZE))


    for i in range (NUM_GRASS):
        x=random.randint(0,WINDOW_WIDTH-(3 * CELL_SIZE))
        y=random.randint(0,WINDOW_HEIGHT-(2 * CELL_SIZE))
        screen.blit(img, (x,y))



def drawGrid():
    screen.fill(BLACK)
    blockSize = BLOCK_SIZE  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, GREEN, rect, 1)

    field=game_field.generate_mines(NUM_OF_MINES)
    for i in range (len (field)):
        for j in range (len(field[i])):


