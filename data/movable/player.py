import pygame
from data.movable.movable import Movable
from utils import load_image


class Player(Movable):
    sheet = load_image('player.png')
    sh_y, sh_x = 1, 6

    def __init__(self, speed, pos, group):
        super().__init__(speed, Player.sheet, Player.sh_y, Player.sh_x, pos, group)
        self.score = 0
        self.lives = 3
        self.protected = False

    def move(self, up, left, down, right):
        if up:
            self.rect.y -= self.speed
        if left:
            self.rect.x -= self.speed
            self.flip_left = True
        if down:
            self.rect.y += self.speed
        if right:
            self.rect.x += self.speed

    def update(self):
        pressed = pygame.key.get_pressed()
        controls = [pressed[pygame.K_w] or pressed[pygame.K_UP], pressed[pygame.K_a] or pressed[pygame.K_LEFT], pressed[pygame.K_s] or pressed[pygame.K_DOWN], pressed[pygame.K_d] or pressed[pygame.K_RIGHT]]
        if any(controls):
            super().update()
            self.move(*controls)
