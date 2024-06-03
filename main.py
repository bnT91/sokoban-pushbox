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
wall_sprite = icon
player_sprite = pg.image.load("pic/player.png")
box_sprite = pg.image.load("pic/box.png")
box_on_target_sprite = pg.image.load("pic/box_on_target.png")
target_sprite = pg.image.load("pic/target.png")

# Screen
scr = pg.display.set_mode((8*32, 8*32))
pg.display.set_caption("PushBoxPush")
pg.display.set_icon(icon)

# Player
pos = []

for x in range(8):
    for y in range(8):
        if levels[0][x][y] == "P":
            pos = [x, y]

while True:
    for x in range(8):
        for y in range(8):
            if levels[0][x][y] == "#":
                scr.blit(wall_sprite, (x*32, y*32))
            elif levels[0][x][y] == "P":
                scr.blit(player_sprite, (x*32, y*32))
            elif levels[0][x][y] == "B":
                scr.blit(box_sprite, (x*32, y*32))
            elif levels[0][x][y] == "T":
                scr.blit(target_sprite, (x*32, y*32))
            elif levels[0][x][y] == "X":
                scr.blit(box_on_target_sprite, (x*32, y*32))
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()
    clock.tick(20)
