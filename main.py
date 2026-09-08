import screen
import pygame
from soldier import *
from game_field import *

def main():
    screen.create_screen()
    game_field, level_mines = generate_mines(NUM_OF_MINES)
    screen.draw_grass()


main()