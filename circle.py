from pygame import mixer

from settings import *


class Circle:
    def __init__(self):
        self.pos_x = CIR_CENTER[0]
        self.pos_y = CIR_CENTER[1]
        self.move_x = CIR_X_START_MOVE
        self.move_y = CIR_Y_START_MOVE
        self.center = CIR_CENTER
        mixer.music.load('hit.mp3')

    def move(self):

        if self.move_x:
            self.pos_x += CIR_SPEED
        else:
            self.pos_x -= CIR_SPEED

        if self.move_y:
            self.pos_y += CIR_SPEED
        else:
            self.pos_y -= CIR_SPEED

        self.center = (self.pos_x, self.pos_y)

    def move_check(self, direction_1, direction_2, f_desk, s_desk):

        if self.pos_x - CIR_RAD == 0 or self.pos_x + CIR_RAD == SCREEN_WIDTH:
            self.move_x = not self.move_x

        if self.pos_y - CIR_RAD == 0 or self.pos_y + CIR_RAD == SCREEN_HEIGHT:
            self.move_y = not self.move_y

        if self.pos_x - CIR_RAD == f_desk.pos_x + DESKS_WIDTH and \
                (f_desk.pos_y <= self.pos_y + CIR_RAD <= f_desk.pos_y + DESKS_HEIGHT or \
                 f_desk.pos_y <= self.pos_y - CIR_RAD <= DESKS_HEIGHT):
            if direction_1 and self.move_y:
                self.move_x = not self.move_x

            if direction_1 and not self.move_y:
                self.move_y = not self.move_y
                self.move_x = not self.move_x

            if not direction_1 and self.move_y:
                self.move_y = not self.move_y
                self.move_x = not self.move_x

            if not direction_1 and not self.move_y:
                self.move_x = not self.move_x


        elif self.pos_x + CIR_RAD == s_desk.pos_x and \
                (s_desk.pos_y <= self.pos_y + CIR_RAD <= s_desk.pos_y + DESKS_HEIGHT or \
                 s_desk.pos_y <= self.pos_y - CIR_RAD <= DESKS_HEIGHT):
            if direction_2 and self.move_y:
                self.move_x = not self.move_x

            if direction_2 and not self.move_y:
                self.move_y = not self.move_y
                self.move_x = not self.move_x

            if not direction_2 and self.move_y:
                self.move_y = not self.move_y
                self.move_x = not self.move_x

            if not direction_2 and not self.move_y:
                self.move_x = not self.move_x

    def check_walls(self):
        if self.pos_x - CIR_RAD == 0:
            return 1

        elif self.pos_x + CIR_RAD == SCREEN_WIDTH:
            return 2

        else:
            return None
