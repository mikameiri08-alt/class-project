from constants import *
import pygame
from pygame.locals import *

pygame.init()

# Create the display surface object of specific dimension.
window = pygame.display.set_mode((600, 600))

# Add caption in the window
pygame.display.set_caption('Player Movement')

# Add player sprite image (make sure 'soldier.png' is in the same folder)
image = pygame.image.load(r'soldier.png')
img = pygame.transform.scale(image, (2*CELL_SIZE, 4*CELL_SIZE))



# Store the initial coordinates of the player
x = 0
y = 0

# Create a variable to store the velocity of player's movement
velocity = 12

# Creating an Infinite loop
run = True
while run:
    # Fill the window with a background color (e.g., White: 255, 255, 255)
    window.fill((255, 255, 255))

    # Iterate over the list of Event objects
    for event in pygame.event.get():
        # Closing the window and program if the type of the event is QUIT
        if event.type == pygame.QUIT:
            run = False

        # Checking event key if the type of the event is KEYDOWN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= velocity
            if event.key == pygame.K_RIGHT:
                x += velocity
            if event.key == pygame.K_UP:
                y -= velocity
            if event.key == pygame.K_DOWN:
                y += velocity

    # Display the player sprite at updated x and y coordinates
    window.blit(img, (x, y))

    # Draws the surface object to the screen.
    pygame.display.update()

pygame.quit()
quit()
