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

# Icon
icon = pg.image.load("pic/wall.png")

# Screen
scr = pg.display.set_mode((8*64, 8*64))
pg.display.set_caption("PushBoxPush")
pg.display.set_icon(icon)

# Images
wall_sprite = pg.transform.scale(icon.convert(), (64, 64))
p = pg.image.load("pic/player.png").convert()
player_sprite = pg.transform.scale(p, (64, 64))
b = pg.image.load("pic/box.png")
box_sprite = pg.transform.scale(b, (64, 64))
b_on_t = pg.image.load("pic/box_on_target.png")
box_on_target_sprite = pg.transform.scale(b_on_t, (64, 64))
t = pg.image.load("pic/target.png")
target_sprite = pg.transform.scale(t, (64, 64))

# Level
side = len(levels[0])
current_level = 0

# Player
pos = []

for x in range(8):
    for y in range(8):
        if levels[0][x][y] == "P":
            pos = [x, y]


while True:
    for x in range(side):
        for y in range(side):
            if levels[current_level][x][y] == "#":
                scr.blit(wall_sprite, (x*64, y*64))
            elif levels[current_level][x][y] == "P":
                scr.blit(player_sprite, (x*64, y*64))
            elif levels[current_level][x][y] == "B":
                scr.blit(box_sprite, (x*64, y*64))
            elif levels[current_level][x][y] == "T":
                scr.blit(target_sprite, (x*64, y*64))
            elif levels[current_level][x][y] == "X":
                scr.blit(box_on_target_sprite, (x*64, y*64))
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()
    clock.tick(20)
