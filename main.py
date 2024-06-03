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
from time import sleep
# import pprint

# Levels
with open("levels.json", "r") as f:
    levels = json.load(f)
    init_lvls = levels.copy()
    number_of_levels = len(levels)

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

lvl_complete_font = pg.font.Font("fonts/Inter/static/Inter-Black.ttf", 40)
lvl_complete_text = lvl_complete_font.render("Level Completed!", False, "White")

# Level
side = len(levels[0])
current_level = 0
finished = False

# Player
pos = []

for x in range(8):
    for y in range(8):
        if levels[0][x][y] == "P":
            pos = [x, y]


while True:
    if not finished:
        boxes_on_map = False
        for x in range(side):
            for y in range(side):
                if levels[current_level][y][x] == "#":
                    scr.blit(wall_sprite, (x*64, y*64))
                elif levels[current_level][y][x] in ["P", "o"]:
                    scr.blit(player_sprite, (x*64, y*64))
                elif levels[current_level][y][x] == "B":
                    scr.blit(box_sprite, (x*64, y*64))
                    boxes_on_map = True
                elif levels[current_level][y][x] == "T":
                    scr.blit(target_sprite, (x*64, y*64))
                elif levels[current_level][y][x] == "X":
                    scr.blit(box_on_target_sprite, (x*64, y*64))
                elif levels[current_level][y][x] == ".":
                    scr.blit(void_sprite, (x*64, y*64))
        if not boxes_on_map:
            big_void = pg.transform.scale(void_sprite, (side*64, side*64))
            scr.blit(big_void, (0, 0))
            scr.blit(lvl_complete_text, (20, (side-1)//2*64))
            pg.display.flip()
            sleep(1)
            current_level += 1
            if current_level == number_of_levels:
                print("finished")
                finished = True
            else:
                side = len(levels[current_level])
                for x in range(side):
                    for y in range(side):
                        if levels[current_level][x][y] == "P":
                            pos = [y, x]
                pg.display.set_mode((side*64, side*64))
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if ev.type == pg.KEYUP:
            if not finished:
                if ev.key == pg.K_UP:
                    if pos[1] != 0:
                        if levels[current_level][pos[1] - 1][pos[0]] == ".":
                            levels[current_level][pos[1] - 1][pos[0]] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] - 1]
                        elif levels[current_level][pos[1] - 1][pos[0]] == "T":
                            levels[current_level][pos[1] - 1][pos[0]] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] - 1]
                        elif levels[current_level][pos[1] - 1][pos[0]] == "B" and levels[current_level][pos[1] - 2][pos[0]] == ".":
                            levels[current_level][pos[1] - 1][pos[0]] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] - 1]
                            levels[current_level][pos[1] - 1][pos[0]] = "B"
                        elif levels[current_level][pos[1] - 1][pos[0]] == "B" and levels[current_level][pos[1] - 2][pos[0]] == "T":
                            levels[current_level][pos[1] - 1][pos[0]] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] - 1]
                            levels[current_level][pos[1] - 1][pos[0]] = "X"
                        elif levels[current_level][pos[1] - 1][pos[0]] == "X" and levels[current_level][pos[1] - 2][pos[0]] == ".":
                            levels[current_level][pos[1] - 1][pos[0]] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] - 1]
                            levels[current_level][pos[1] - 1][pos[0]] = "B"
                        elif levels[current_level][pos[1] - 1][pos[0]] == "X" and levels[current_level][pos[1] - 2][pos[0]] == "T":
                            levels[current_level][pos[1] - 1][pos[0]] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] - 1]
                            levels[current_level][pos[1] - 1][pos[0]] = "X"
                if ev.key == pg.K_DOWN:
                    if pos[1] != side-1:
                        if levels[current_level][pos[1] + 1][pos[0]] == ".":
                            levels[current_level][pos[1] + 1][pos[0]] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] + 1]
                        elif levels[current_level][pos[1] + 1][pos[0]] == "T":
                            levels[current_level][pos[1] + 1][pos[0]] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] + 1]
                        elif levels[current_level][pos[1] + 1][pos[0]] == "B" and levels[current_level][pos[1] + 2][pos[0]] == ".":
                            levels[current_level][pos[1] + 1][pos[0]] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] + 1]
                            levels[current_level][pos[1] + 1][pos[0]] = "B"
                        elif levels[current_level][pos[1] + 1][pos[0]] == "B" and levels[current_level][pos[1] + 2][pos[0]] == "T":
                            levels[current_level][pos[1] + 1][pos[0]] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] + 1]
                            levels[current_level][pos[1] + 1][pos[0]] = "X"
                        elif levels[current_level][pos[1] + 1][pos[0]] == "X" and levels[current_level][pos[1] + 2][pos[0]] == ".":
                            levels[current_level][pos[1] + 1][pos[0]] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] + 1]
                            levels[current_level][pos[1] + 1][pos[0]] = "B"
                        elif levels[current_level][pos[1] + 1][pos[0]] == "X" and levels[current_level][pos[1] + 2][pos[0]] == "T":
                            levels[current_level][pos[1] + 1][pos[0]] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0], pos[1] + 1]
                            levels[current_level][pos[1] + 1][pos[0]] = "X"
                if ev.key == pg.K_RIGHT:
                    if pos[0] != side-1:
                        if levels[current_level][pos[1]][pos[0] + 1] == ".":
                            levels[current_level][pos[1]][pos[0] + 1] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] + 1, pos[1]]
                        elif levels[current_level][pos[1]][pos[0] + 1] == "T":
                            levels[current_level][pos[1]][pos[0] + 1] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] + 1, pos[1]]
                        elif levels[current_level][pos[1]][pos[0] + 1] == "B" and levels[current_level][pos[1]][pos[0] + 2] == ".":
                            levels[current_level][pos[1]][pos[0] + 1] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] + 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] + 1] = "B"
                        elif levels[current_level][pos[1]][pos[0] + 1] == "B" and levels[current_level][pos[1]][pos[0] + 2] == "T":
                            levels[current_level][pos[1]][pos[0] + 1] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] + 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] + 1] = "X"
                        elif levels[current_level][pos[1]][pos[0] + 1] == "X" and levels[current_level][pos[1]][pos[0] + 2] == ".":
                            levels[current_level][pos[1]][pos[0] + 1] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] + 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] + 1] = "B"
                        elif levels[current_level][pos[1]][pos[0] + 1] == "X" and levels[current_level][pos[1]][pos[0] + 2] == "T":
                            levels[current_level][pos[1]][pos[0] + 1] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] + 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] + 1] = "X"
                if ev.key == pg.K_LEFT:
                    if pos[0] != 0:
                        if levels[current_level][pos[1]][pos[0] - 1] == ".":
                            levels[current_level][pos[1]][pos[0] - 1] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] - 1, pos[1]]
                        elif levels[current_level][pos[1]][pos[0] - 1] == "T":
                            levels[current_level][pos[1]][pos[0] - 1] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] - 1, pos[1]]
                        elif levels[current_level][pos[1]][pos[0] - 1] == "B" and levels[current_level][pos[1]][pos[0] - 2] == ".":
                            levels[current_level][pos[1]][pos[0] - 1] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] - 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] - 1] = "B"
                        elif levels[current_level][pos[1]][pos[0] - 1] == "B" and levels[current_level][pos[1]][pos[0] - 2] == "T":
                            levels[current_level][pos[1]][pos[0] - 1] = "P"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] - 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] - 1] = "X"
                        elif levels[current_level][pos[1]][pos[0] - 1] == "X" and levels[current_level][pos[1]][pos[0] - 2] == ".":
                            levels[current_level][pos[1]][pos[0] - 1] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] - 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] - 1] = "B"
                        elif levels[current_level][pos[1]][pos[0] - 1] == "X" and levels[current_level][pos[1]][pos[0] - 2] == "T":
                            levels[current_level][pos[1]][pos[0] - 1] = "o"
                            if levels[current_level][pos[1]][pos[0]] == "P":
                                levels[current_level][pos[1]][pos[0]] = "."
                            else:
                                levels[current_level][pos[1]][pos[0]] = "T"
                            pos = [pos[0] - 1, pos[1]]
                            levels[current_level][pos[1]][pos[0] - 1] = "X"

    pg.display.flip()
    clock.tick(50)
