from random import choice, randint
import pygame as pg
from data.movable.movable import Movable
from utils import load_image, WIDTH, HEIGHT
TO_GENERATE_ENEMY = pg.USEREVENT + 1


class Enemy(Movable):
    speeds = [1, 2, 3]
    sheet = load_image('enemy.png')
    sh_y, sh_x = 1, 6

    def __init__(self, speed, pos, group):
        super().__init__(speed, Enemy.sheet, Enemy.sh_y, Enemy.sh_x, pos, group)

    def move(self, player=None):
        if player.rect.x < self.rect.x:
            self.rect.x -= self.speed
            self.flip_left = True
        else:
            self.rect.x += self.speed
        if player.rect.y < self.rect.y:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def update(self, player=None):
        self.move(player)
        super().update()

    @staticmethod
    def generate(n, group):
        for i in range(n):
            Enemy(choice(Enemy.speeds), (randint(0, WIDTH), randint(0, HEIGHT)), group)
