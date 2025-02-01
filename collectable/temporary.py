import pygame.time
from collectable.collectable import Collectable


class Temporary(Collectable):
    def __init__(self, sheet, rows, columns, pos, group, ttl=5000):
        super().__init__(sheet, rows, columns, pos, group)
        self.ttl = ttl
        self.created_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.created_time > self.ttl:
            self.kill()
        super().update()