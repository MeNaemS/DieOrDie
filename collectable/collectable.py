from animated_sprite import AnimatedSprite


class Collectable(AnimatedSprite):
    def __init__(self, sheet, rows, columns, pos, group):
        super().__init__(sheet, rows, columns, pos, group)

    def collect(self, player):
        self.kill()
