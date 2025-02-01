import pygame as pg


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, sheet, rows, columns, pos, group):
        super().__init__(group)
        self.frames = []  # список кадров
        self.index = 0  # текущий индекс
        self.cut_sheet(sheet, rows, columns)
        self.image = self.frames[self.index]
        self.rect.center = pos

    def cut_sheet(self, sheet, rows, columns):
        self.rect = pg.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)

        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                cur_frame = sheet.subsurface(frame_location, self.rect.size)
                self.frames.append(cur_frame)

    def update(self):
        self.index = (self.index + 1) % (len(self.frames))
        self.image = self.frames[self.index]
