import pygame
from constants import *
import screen
from soldier import move_soldier, draw_soldier, check_mine_collision, \
    touched_flag
import database
from teleport import *
from guard import *

def main():
    pygame.init()
    screen.create_screen()

    player_x = START_X_PLAYER
    player_y = START_Y_PLAYER

    guard_x = GUARD_START_COL

    clock = pygame.time.Clock()
    flag_x = WINDOW_WIDTH - (FLAG_COLS * CELL_SIZE)
    flag_y = WINDOW_HEIGHT - (FLAG_ROWS * CELL_SIZE)

    show_grid = False
    grid_timer_start = 0

    key_press_times = {}  # when the key got pressed
    key_already_triggered = {}  # if already had long press in this num


    run = True
    while run:
        current_time_ticks = pygame.time.get_ticks()
        draw_guard(GUARD_START_ROW, GUARD_START_COL, screen.screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.short_press_num("autosave", player_x, player_y)
                run = False

            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    digit = event.key - pygame.K_0
                    if digit not in key_press_times:
                        key_press_times[digit] = current_time_ticks
                        key_already_triggered[digit] = False
                        print(f"Key {digit} pressed.")

            elif event.type == pygame.KEYUP:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    digit = event.key - pygame.K_0

                    if digit in key_press_times:
                        # short press
                        if not key_already_triggered.get(digit, False):
                            database.short_press_num(digit, player_x, player_y)
                        else:
                            print(f"Key {digit} released after a long press.")

                        key_press_times.pop(digit, None)
                        key_already_triggered.pop(digit, None)

            # long press
        for digit, start_time in list(key_press_times.items()):
            if current_time_ticks - start_time >= LONG_PRESS_THRESHOLD:
                if not key_already_triggered.get(digit, False):
                    print(
                        f"Long press detected (> 1 second)! Loading data from slot {digit}...")

                    # loading the game
                    loaded_coords = database.long_num_press(digit)
                    if loaded_coords:
                        player_x, player_y = loaded_coords

                    key_already_triggered[digit] = True

        screen.screen.fill(SCREEN_COLOR)
        screen.draw_grass()
        screen.draw_flag()
        screen.draw_traps_on_screen()

        player_x, player_y, enter_pressed = move_soldier(player_x, player_y)
        if enter_pressed and not show_grid:
            show_grid = True
            grid_timer_start = current_time_ticks

        if show_grid and (current_time_ticks - grid_timer_start > 1000):
            show_grid = False

        if show_grid:
            screen.drawGrid()
            screen.draw_mines_on_screen()


        if check_mine_collision(player_x, player_y, screen.level_mines):
            print("BOOM!!! you stepped on a landmine")
            run = False

        if touched_flag(player_x, player_y, flag_x, flag_y):
            print("VICTORY!! you reached the flag")
            run = False

        if check_trap_collision(player_x, player_y, screen.level_traps):
            player_x, player_y = teleport_player(player_x, player_y, screen.level_traps)

        if touched_guard(player_x, player_y, guard_x, GUARD_START_ROW):
            print("you touched the guard!")
            run = False

        draw_soldier(player_x, player_y, screen.screen)
        draw_guard(GUARD_START_ROW, GUARD_START_COL, screen.screen)
        pygame.display.flip()

        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()
