import pygame
from constants import *
from screen import screen


class Soldier:
    def __init__(self, x=0, y=0, velocity=12):
        self.x = x
        self.y = y
        self.velocity = velocity

        # Load and scale the sprite image using CELL_SIZE
        image = pygame.image.load(r'soldier.png')
        self.img = pygame.transform.scale(image,
                                          (2 * CELL_SIZE, 4 * CELL_SIZE))

    def handle_event(self, event):
        """Update coordinates based on keyboard input"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= self.velocity
            if event.key == pygame.K_RIGHT:
                self.x += self.velocity
            if event.key == pygame.K_UP:
                self.y -= self.velocity
            if event.key == pygame.K_DOWN:
                self.y += self.velocity

    def draw(self):
        """Draw the soldier onto the main display window"""
        screen.blit(self.img, (self.x, self.y))

    def touched_flag(self, flag):
        player_rect = pygame.Rect(self.x, self.y, self.img.get_width(),
                                  self.img.get_height())

        flag_rect = pygame.Rect(flag.x, flag.y, flag.img.get_width(),
                                flag.img.get_height())

        return player_rect.colliderect(flag_rect)

    def touched_mine(self, mine):
        player_rect = pygame.Rect(self.x, self.y, self.img.get_width(),
                                  self.img.get_height())

        mine_rect = pygame.Rect(mine.x, mine.y, mine.img.get_width(),
                                mine.img.get_height())

        return player_rect.colliderect(mine_rect)
