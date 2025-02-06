import pygame
from data.movable.movable import Movable
from utils import load_image, window


class Player(Movable):
    sheet = load_image('player.png')
    sh_y, sh_x = 1, 6

    def __init__(self, speed, pos, group):
        super().__init__(speed, Player.sheet, Player.sh_y, Player.sh_x, pos, group)
        self.score = 0
        self.lives = 3
        self.protected = False

    def move(self, up, left, down, right):
        if up and self.rect.top - self.speed > 0:
            self.rect.y -= self.speed
        if left and self.rect.left - self.speed > 0:
            self.rect.x -= self.speed
            self.flip_left = True
        if down and self.rect.bottom + self.speed < window.get_height():
            self.rect.y += self.speed
        if right and self.rect.right + self.speed < window.get_width():
            self.rect.x += self.speed

    def update(self):
        pressed = pygame.key.get_pressed()
        controls = [pressed[pygame.K_w] or pressed[pygame.K_UP], pressed[pygame.K_a] or pressed[pygame.K_LEFT], pressed[pygame.K_s] or pressed[pygame.K_DOWN], pressed[pygame.K_d] or pressed[pygame.K_RIGHT]]
        if any(controls):
            super().update()
            self.move(*controls)
