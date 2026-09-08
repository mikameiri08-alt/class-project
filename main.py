import pygame
from constants import *
import screen
from soldier import move_soldier, draw_soldier

def main():
    pygame.init()
    screen.create_screen()

    player_x = START_X_PLAYER
    player_y = START_Y_PLAYER

    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.screen.fill(SCREEN_COLOR)

        screen.draw_grass()
        screen.draw_flag()

        player_x, player_y = move_soldier(player_x, player_y)
        draw_soldier(player_x, player_y, screen.screen)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()


