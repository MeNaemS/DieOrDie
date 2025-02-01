import pygame as pg
from animated_sprite import AnimatedSprite


class Movable(AnimatedSprite):
    def __init__(self, speed, sheet, rows, columns, pos, group):
        super().__init__(sheet, rows, columns, pos, group)
        self.speed = speed
        self.flip_left = False

    def move(self):
        pass

    def update(self):
        super().update()
        if self.flip_left:
            self.flip_left = False
            self.image = pg.transform.flip(self.image, True, False)