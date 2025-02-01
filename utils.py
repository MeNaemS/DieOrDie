import os
import sys
import pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()
SIZE = WIDTH, HEIGHT = 700, 700
pg.display.set_caption('die_or_die')
window = pg.display.set_mode(SIZE)
FONT = pg.font.Font('data/fonts/PermanentMarker-Regular.ttf', 25)


def load_image(name, color_key=None):
    fullname = os.path.join('data/sprites', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не существует')
        sys.exit()
    image = pg.image.load(fullname)
    if color_key is not None:
        image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image.convert_alpha()
    return image
