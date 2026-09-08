import pygame
from constants import *
import screen
from soldier import move_soldier, draw_soldier, check_mine_collision, touched_flag

def main():
    pygame.init()
    screen.create_screen()

    player_x = START_X_PLAYER
    player_y = START_Y_PLAYER

    clock = pygame.time.Clock()

    # חישוב מיקום קבוע לדגל בפיקסלים (בשביל בדיקת הניצחון)
    flag_x = WINDOW_WIDTH - (FLAG_COLS * CELL_SIZE)
    flag_y = WINDOW_HEIGHT - (FLAG_ROWS * CELL_SIZE)

    # המשתנים שמנהלים את הטיימר של השנייה האחת
    show_grid = False
    grid_timer_start = 0

    run = True
    while run:
        current_time = pygame.time.get_ticks()  # הזמן הנוכחי במילישניות

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # א) ציור שכבות הרקע התמידיות: צבע, דשא ודגל
        screen.screen.fill(SCREEN_COLOR)
        screen.draw_grass()
        screen.draw_flag()

        # ב) קליטת מקשי המקלדת של החייל (בודק גם את ה-Enter)
        player_x, player_y, enter_pressed = move_soldier(player_x, player_y)

        # ג) ניהול הטיימר: אם לחצו Enter והרשת/מוקשים לא מוצגים, מפעילים את השעון
        if enter_pressed and not show_grid:
            show_grid = True
            grid_timer_start = pygame.time.get_ticks()  # צילום זמן ההתחלה

        # ד) מנגנון כיבוי אוטומטי: אם עברה שנייה אחת (1000 מילישניות), מחביאים שוב
        if show_grid and (current_time - grid_timer_start > 1000):
            show_grid = False

        # ה) --- כאן מתרחש הקסם: ציור הרשת והמוקשים רק בתוך השנייה הזו! ---
        if show_grid:
            screen.drawGrid()               # מצייר את קווי הרשת
            screen.draw_mines_on_screen()   # מציג את המוקשים (נקרא לפונקציה שיצרנו ב-screen)

        # ו) בדיקת התנגשויות ברקע (החייל יכול להתפוצץ גם כשהמוקשים נסתרים!)
        if check_mine_collision(player_x, player_y, screen.level_mines):
            print("בום! דרכת על מוקש נסתר. המשחק נגמר!")
            run = False

        if touched_flag(player_x, player_y, flag_x, flag_y):
            print("כל הכבוד! הגעת לדגל וניצחת!")
            run = False

        # ז) ציור החייל מעל הכל ועדכון המסך
        draw_soldier(player_x, player_y, screen.screen)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
