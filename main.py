# Нотация символов.
#
# . - Пустое место в уровне
# _ - Пустое место вне уровня
# # - Блок стены
# B - Ящик
# T - Цель для ящика
# P - Стартовая позиция игрока

import pygame as pg
import sys

# Init
pg.init()

# Images
icon = pg.image.load("pic/wall.png")

# Screen
scr = pg.display.set_mode((8*32, 8*32))
pg.display.set_caption("PushBoxPush")
pg.display.set_icon(icon)

while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()
