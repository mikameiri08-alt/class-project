import pygame
from constants import *
import screen
from soldier import move_soldier, draw_soldier, check_mine_collision, \
    touched_flag

def main():
    pygame.init()
    screen.create_screen()

    player_x = START_X_PLAYER
    player_y = START_Y_PLAYER

    clock = pygame.time.Clock()

    flag_x = WINDOW_WIDTH - (FLAG_COLS * CELL_SIZE)
    flag_y = WINDOW_HEIGHT - (FLAG_ROWS * CELL_SIZE)

    # Variables to manage the 1-second visibility window
    show_grid = False
    grid_timer_start = 0

    run = True
    while run:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.screen.fill(SCREEN_COLOR)
        screen.draw_grass()
        screen.draw_flag()

        player_x, player_y, enter_pressed = move_soldier(player_x, player_y)

        # Trigger the 1-second display timer when Enter is pressed
        if enter_pressed and not show_grid:
            show_grid = True
            grid_timer_start = pygame.time.get_ticks()

        # Turn off the visibility automatically after exactly 1000ms (1 second)
        if show_grid and (current_time - grid_timer_start > 1000):
            show_grid = False

        if show_grid:
            screen.drawGrid()
            screen.draw_mines_on_screen()

        # Collision detection (Triggers game over/victory)
        if check_mine_collision(player_x, player_y, screen.level_mines):
            print("BOOM!!! you stepped on a landmine")
            run = False

        if touched_flag(player_x, player_y, flag_x, flag_y):
            print("VICTORY!! you reached the flag")
            run = False

        draw_soldier(player_x, player_y, screen.screen)
        pygame.display.flip()

        # Limit the frame rate to ensure controlled, grid-based player movement
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
