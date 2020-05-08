from pygame import font

from settings import *


class Counter:
    def __init__(self):
        self.pos_x = COUNTER_X
        self.pos_y = COUNTER_Y

        self.scope_first = 0
        self.scope_second = 0

        self.font = font.SysFont('comicsansms', COUNTER_FONT_SIZE)
        self.text = 'SCOPE {0} : {1}'.format(str(self.scope_first), str(self.scope_second))
        self.res = self.font.render(self.text, 0, COUNTER_FONT_COLOR)

    def update_counter(self, check_walls):
        if check_walls == 1:
            self.scope_second += 1
        elif check_walls == 2:
            self.scope_first += 1

        self.text = 'SCOPE {0} : {1}'.format(str(self.scope_first), str(self.scope_second))
        self.res = self.font.render(self.text, 0, COUNTER_FONT_COLOR)
