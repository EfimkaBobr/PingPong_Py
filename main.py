import pygame as pg

from circle import Circle
from control import Control
from counter import Counter
from desks import Desks
from settings import *

pg.init()
pg.display.set_caption("PingPong")
screen = pg.display.set_mode(SCREEN_SIZE)

control = Control()
circle = Circle()
f_desk = Desks.First()
s_desk = Desks.Second()
counter = Counter()

while control.flag_game:
    control.control()

    screen.fill(BG_COLOR)

    circle.move_check(control.direction_1, control.direction_2, f_desk, s_desk)
    circle.move()
    pg.draw.circle(screen, CIR_COLOR, circle.center, CIR_RAD)

    f_desk.move(control.direction_1)
    s_desk.move(control.direction_2)
    pg.draw.rect(screen, DESKS_COLOR, (f_desk.pos_x, f_desk.pos_y, DESKS_WIDTH, DESKS_HEIGHT))
    pg.draw.rect(screen, DESKS_COLOR, (s_desk.pos_x, s_desk.pos_y, DESKS_WIDTH, DESKS_HEIGHT))

    counter.update_counter(circle.check_walls())
    screen.blit(counter.res, (0, 0))

    pg.display.update()
    pg.time.delay(GAME_SPEED)
