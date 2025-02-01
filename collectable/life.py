from random import randint
import pygame
from collectable.temporary import Temporary
from utils import load_image, WIDTH, HEIGHT
TO_GENERATE_LIFE = pygame.USEREVENT + 3


class Life(Temporary):
    def __init__(self, pos, group):
        super().__init__(load_image('life.png'), 5, 6, pos, group)
        self.sound = pygame.mixer.Sound('data/sounds/life3.wav')

    def collect(self, player):
        self.sound.play()
        player.lives += 1
        super().collect(player)

    @staticmethod
    def generate(n, group):
        for i in range(n):
            Life((randint(0, WIDTH), randint(0, HEIGHT)), group)