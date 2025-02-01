import pygame
import pygame as pg
from collectable.collectable import Collectable
from random import randint
from utils import load_image, HEIGHT, WIDTH
TO_GENERATE_COIN = pg.USEREVENT + 2


class Coin(Collectable):
    def __init__(self, cost, pos, group):
        super().__init__(load_image('coin_gold.png'), 1, 8, pos, group)
        self.cost = cost
        self.sound = pygame.mixer.Sound('data/sounds/coin (2).wav')

    def collect(self, player):
        player.score += self.cost
        self.sound.play()
        super().collect(player)

    @staticmethod
    def generate(n, group):
        for i in range(n):
            Coin(randint(0, 20), (randint(0, WIDTH), randint(0, HEIGHT)), group)
