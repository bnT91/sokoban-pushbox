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
import json

# Levels
with open("levels.json", "r") as f:
    levels = json.load(f)

# Init
pg.init()
clock = pg.time.Clock()

# Images
icon = pg.image.load("pic/wall.png")
wall = icon

# Screen
scr = pg.display.set_mode((8*32, 8*32))
pg.display.set_caption("PushBoxPush")
pg.display.set_icon(icon)

while True:
    for x in range(8):
        for y in range(8):
            if levels[0][x][y] == "#":
                scr.blit(wall, (x*32, y*32))
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()
    clock.tick(20)
