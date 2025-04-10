import os
from random import choice, randrange
import pygame as pg

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1980, 1080
ALPHA = 100

pg.init()

screen = pg.display.set_mode(RES)
surface = pg.Surface(RES, pg.SRCALPHA)
surface.set_alpha(ALPHA)
clock = pg.time.Clock()

katakana_chars = ['=', '@', '£', '$', '%', '*', '~', '#', '!', '?', '|', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Symbol:
    def __init__(self, x, y, font_size, speed):
        self.x = x
        self.y = y
        self.y0 = - font_size
        self.font_size = font_size
        self.speed = speed
        self.char_change_speed = randrange(20, 40)
        self.value = choice(katakana_chars)
        self.font_increase = 0

    def draw(self, position):
        self.font_increase_speed = int(self.y / 80)
        self.font_increase = self.font_size + self.font_increase_speed if 0 < self.y <HEIGHT else 0
        font = pg.font.SysFont(None, self.font_size)
        frames = pg.time.get_ticks()
        if not frames % self.char_change_speed:
            self.value = choice(katakana_chars)

        self.y = self.y + self.speed if self.y <HEIGHT else self.y0
        
        if position < 8:
            self.char = font.render(self.value, True, (255 - 32 * position, 255, 255 - 32 * position))
        if position >= 8:
            self.char = font.render(self.value, True, (0, 255 - 22 * (position - 8), 0))

        screen.blit(self.char, (self.x, self.y))


class SymbolColumn: 
    def __init__(self, x, y, font_size):
        self.column_height = randrange(5,20)
        self.speed = randrange(5, 20)
        self.font_size = font_size
        self.symbols = [Symbol(x=x, y=i, font_size=self.font_size, speed=self.speed) for i in range(y, y - (self.font_size + 10) * self.column_height, -(self.font_size + 10))]

    def draw(self):
        [Symbol.draw(position=i) for i, Symbol in enumerate (self.symbols)]

Symbolm_columns = [SymbolColumn(x=i, y=0, font_size=20) for i in range(100, WIDTH - 100, 200)]
        

symbols = [Symbol(x=WIDTH / 2, y=0, font_size=20, speed=5)]

def main():
    running = True
    while running:
        screen.blit(surface, (0, 0))
        surface.fill(pg.Color('black'))

        [symbol_column.draw() for symbol_column in Symbolm_columns]

        [exit() for event in pg.event.get() if event.type == pg.QUIT]

        pg.display.update()

        clock.tick(100)


if __name__ == "__main__":
    main()