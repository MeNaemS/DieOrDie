import sys
import pygame as pg
from pygame import mixer
from pygame.mixer import music
from collectable.coin import Coin, TO_GENERATE_COIN
from collectable.life import TO_GENERATE_LIFE, Life
from collectable.shield import TO_GENERATE_SHIELD, Shield, TO_LOSE_SHIELD
from data.movable.enemy import Enemy, TO_GENERATE_ENEMY
from data.movable.player import Player
from utils import WIDTH, HEIGHT, window, FONT


def render_hud(player):
    score = FONT.render(f'score: {player.score}', True, 'black')
    window.blit(score, (5, 26))
    lives = FONT.render(f'life: {player.lives}', True, 'red')
    shield = FONT.render(f'protected: {player.protected}', True, 'blue')
    window.blit(shield, (WIDTH - 200, 0))
    window.blit(lives, (3, 0))


def set_timers():
    pg.time.set_timer(TO_GENERATE_COIN, 1_500)
    pg.time.set_timer(TO_GENERATE_ENEMY, 5_000)
    pg.time.set_timer(TO_GENERATE_LIFE, 20_000)
    pg.time.set_timer(TO_GENERATE_SHIELD, 10_000)


def handle_events(player, enemies, collectables):
    sound_2 = pg.mixer.Sound('data/sounds/shield_down.wav')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == TO_GENERATE_ENEMY:
            Enemy.generate(1, enemies)
        if event.type == TO_GENERATE_COIN:
            Coin.generate(1, collectables)
        if event.type == TO_GENERATE_LIFE:
            Life.generate(1, collectables)
        if event.type == TO_GENERATE_SHIELD:
            Shield.generate(1, collectables)
        if event.type == TO_LOSE_SHIELD:
            player.protected = False
            sound_2.play()


def render_frame(player, player_group, enemies, collectables):
    window.fill('lightgreen')
    render_hud(player)
    player_group.update()
    player_group.draw(window)
    collectables.draw(window)
    collectables.update()
    enemies.update(player)
    enemies.draw(window)
    pg.display.update()


def main():
    music.load('data/sounds/main_battle.mp3')
    music.set_volume(0.1)
    music.play(-1)
    player_group = pg.sprite.Group()
    player = Player(5, (WIDTH // 2, HEIGHT // 2), player_group)
    enemies = pg.sprite.Group()
    collectables = pg.sprite.Group()
    Enemy.generate(1, enemies)
    clock = pg.time.Clock()
    set_timers()
    FPS = 30
    while True:
        handle_events(player, enemies, collectables)
        to_collect = pg.sprite.spritecollideany(player, collectables)
        render_frame(player, player_group, enemies, collectables)
        enemy_collided = pg.sprite.spritecollideany(player, enemies)
        if enemy_collided:
            enemy_collided.kill()
            if not player.protected:
                player.lives -= 1
                mixer.Sound('data/sounds/player_hit.wav').play()
            else:
                mixer.Sound('data/sounds/enemy_hit.wav').play()
            if player.lives == 0:
                lose_game(player)
        if to_collect:
            to_collect.collect(player)
        clock.tick(FPS)


def start_game():
    music.load('data/sounds/main1.mp3')
    music.set_volume(0.1)
    music.play(-1)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type in {pg.MOUSEBUTTONDOWN or pg.KEYDOWN}:
                main()
        window.fill('lightgreen')
        title = FONT.render(f'Die or die', True, 'red')
        subtitle = FONT.render(f'please, press any key to restart', True, 'red')
        window.blit(title, (WIDTH // 2 - title.get_rect().width // 2, HEIGHT // 2 - title.get_rect().height // 2))
        window.blit(subtitle, (WIDTH // 2 - subtitle.get_rect().width // 2, HEIGHT // 2 + 2))
        pg.display.update()


def lose_game(player):
    with open('data/high_score.data.txt', 'r') as f:
        high_score = int(f.read())
        if player.score > high_score:
            message = f'New high score: {player.score}'
            with open('data/high_score.data.txt', 'w') as file:
                file.write(str(player.score))
        else:
            message = f'High score: {high_score}'
    music.load('data/sounds/game_over1.wav')
    music.set_volume(0.1)
    music.play(-1)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type in {pg.MOUSEBUTTONDOWN or pg.KEYDOWN}:
                main()
        window.fill('lightgreen')
        title = FONT.render(f'You lose. {message}', True, 'black')
        subtitle = FONT.render(f'please, press any key to restart', True, 'black')
        window.blit(title, (WIDTH // 2 - title.get_rect().width // 2, HEIGHT // 2 - title.get_rect().height // 2))
        window.blit(subtitle, (WIDTH // 2 - subtitle.get_rect().width // 2, HEIGHT // 2 + 2))
        pg.display.update()


if __name__ == '__main__':
    start_game()
