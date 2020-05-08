from settings import *


class Desks:
    class First:

        def __init__(self):
            self.pos_x = DESKS_START_POS_X[0]
            self.pos_y = DESKS_START_POS_Y

        def move(self, direction):
            if direction and self.pos_y != SCREEN_HEIGHT - DESKS_HEIGHT:
                self.pos_y += DESKS_SPEED
            elif not direction and self.pos_y != 0:
                self.pos_y -= DESKS_SPEED

    class Second:
        def __init__(self):
            self.pos_x = DESKS_START_POS_X[1]
            self.pos_y = DESKS_START_POS_Y

        def move(self, direction):
            if direction and self.pos_y != SCREEN_HEIGHT - DESKS_HEIGHT:
                self.pos_y += DESKS_SPEED
            elif not direction and self.pos_y != 0:
                self.pos_y -= DESKS_SPEED
