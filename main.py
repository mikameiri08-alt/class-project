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
    guard_x = 0
    guard_row = BOARD_ROWS // 2  # Initialize the guard row early to prevent undefined errors
    clock = pygame.time.Clock()
    flag_x = WINDOW_WIDTH - (FLAG_COLS * CELL_SIZE)
    flag_y = WINDOW_HEIGHT - (FLAG_ROWS * CELL_SIZE)
    show_grid = False
    grid_timer_start = 0
    key_press_times = {}

    guard_direction = "right"
    run = True

    while run:
        current_time_ticks = pygame.time.get_ticks()

        # 1. EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.short_press_num("autosave", player_x, player_y,
                                         guard_row, guard_x)
                run = False

            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    digit = event.key - pygame.K_0
                    if digit not in key_press_times:
                        key_press_times[digit] = current_time_ticks
                        print(f"Key {digit} pressed.")

            elif event.type == pygame.KEYUP:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    digit = event.key - pygame.K_0
                    if digit in key_press_times:
                        press_duration = current_time_ticks - key_press_times[
                            digit]

                        # Long press logic - Trigger Load
                        if press_duration >= LONG_PRESS_THRESHOLD:
                            print(
                                f"Long press detected! Loading data from slot {digit}...")
                            loaded_data = database.long_num_press(digit)
                            if loaded_data:  # Verify file exists and returned valid tuples
                                player_x, player_y, guard_row, guard_x = loaded_data
                        # Short press logic - Trigger Save
                        else:
                            print(
                                f"Short press detected! Saving data to slot {digit}...")
                            database.short_press_num(digit, player_x, player_y,
                                                     guard_row, guard_x)

                        del key_press_times[digit]

        # 2. UPDATE GAME STATE
        if guard_direction == "right":
            guard_x = move_guard_right(guard_x)
            if guard_x >= WINDOW_WIDTH - (GUARD_COLS * CELL_SIZE):
                guard_direction = "left"
        else:
            guard_x = move_guard_left(guard_x)
            if guard_x <= 0:
                guard_direction = "right"

        player_x, player_y, enter_pressed = move_soldier(player_x, player_y)

        if enter_pressed and not show_grid:
            show_grid = True
            grid_timer_start = current_time_ticks

        if show_grid and (current_time_ticks - grid_timer_start > 1000):
            show_grid = False

        # Collision Detections
        if check_mine_collision(player_x, player_y, screen.level_mines):
            print("BOOM!!! you stepped on a landmine")
            run = False

        if touched_flag(player_x, player_y, flag_x, flag_y):
            print("VICTORY!! you reached the flag")
            run = False

        if check_trap_collision(player_x, player_y, screen.level_traps):
            player_x, player_y = teleport_player(player_x, player_y,
                                                 screen.level_traps)

        if touched_guard(player_x, player_y, guard_x, guard_row):
            print("you touched the guard!")
            run = False

        # 3. RENDER ENVIRONMENT
        screen.screen.fill(SCREEN_COLOR)
        screen.draw_grass()
        screen.draw_flag()
        screen.draw_traps_on_screen()

        if show_grid:
            screen.drawGrid()
            screen.draw_mines_on_screen()

        draw_soldier(player_x, player_y, screen.screen)
        draw_guard(guard_row, guard_x, screen.screen)

        pygame.display.flip()
        clock.tick(
            30)  # Faster frame tick rate for highly responsive keyboard sensing

    pygame.quit()


if __name__ == "__main__":
    main()
