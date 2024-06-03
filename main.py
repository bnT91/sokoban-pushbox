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
b = pg.image.load("pic/box.png").convert()
box_sprite = pg.transform.scale(b, (64, 64))
b_on_t = pg.image.load("pic/box_on_target.png").convert()
box_on_target_sprite = pg.transform.scale(b_on_t, (64, 64))
t = pg.image.load("pic/target.png").convert()
target_sprite = pg.transform.scale(t, (64, 64))
v = pg.image.load("pic/void.png").convert()
void_sprite = pg.transform.scale(v, (64, 64))


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
            if levels[current_level][y][x] == "#":
                scr.blit(wall_sprite, (x*64, y*64))
            elif levels[current_level][y][x] == "P":
                scr.blit(player_sprite, (x*64, y*64))
            elif levels[current_level][y][x] == "B":
                scr.blit(box_sprite, (x*64, y*64))
            elif levels[current_level][y][x] == "T":
                scr.blit(target_sprite, (x*64, y*64))
            elif levels[current_level][y][x] == "X":
                scr.blit(box_on_target_sprite, (x*64, y*64))
            elif levels[current_level][y][x] == ".":
                scr.blit(void_sprite, (x*64, y*64))
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if ev.type == pg.KEYUP:
            if ev.key == pg.K_UP:
                if levels[current_level][pos[1] - 1][pos[0]] == ".":
                    levels[current_level][pos[1] - 1][pos[0]] = "P"
                    levels[current_level][pos[1]][pos[0]] = "."
                    pos = [pos[0], pos[1] - 1]
            if ev.key == pg.K_DOWN:
                if levels[current_level][pos[1] + 1][pos[0]] == ".":
                    levels[current_level][pos[1] + 1][pos[0]] = "P"
                    levels[current_level][pos[1]][pos[0]] = "."
                    pos = [pos[0], pos[1] + 1]
            if ev.key == pg.K_RIGHT:
                if levels[current_level][pos[1]][pos[0] + 1] == ".":
                    levels[current_level][pos[1]][pos[0] + 1] = "P"
                    levels[current_level][pos[1]][pos[0]] = "."
                    pos = [pos[0] + 1, pos[1]]
            if ev.key == pg.K_LEFT:
                if levels[current_level][pos[1]][pos[0] - 1] == ".":
                    levels[current_level][pos[1]][pos[0] - 1] = "P"
                    levels[current_level][pos[1]][pos[0]] = "."
                    pos = [pos[0] - 1, pos[1]]

    pg.display.flip()
    clock.tick(50)
