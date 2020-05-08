import pygame as pg


class Control:
    def __init__(self):
        self.flag_game = True
        self.direction_1 = True
        self.direction_2 = False

    def control(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.flag_game = False
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_UP:
                    self.direction_2 = False
                elif event.key == pg.K_DOWN:
                    self.direction_2 = True

                if event.key == pg.K_w:
                    self.direction_1 = False
                elif event.key == pg.K_s:
                    self.direction_1 = True
