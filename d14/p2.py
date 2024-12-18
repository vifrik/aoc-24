import re
import numpy as np

from libaoc.vector import Vector

with open("i.txt", "r") as f:
    robots = f.read().strip().splitlines()

N_STEPS = 100
WIDTH = 101
HEIGHT = 103

QW = WIDTH // 2
QH = HEIGHT // 2

vrs = list()
for robot in robots:
    vals = re.findall(r"-?\d+", robot)
    vr = Vector(*tuple(map(int, vals)))
    vrs.append(vr)
# 6667, too low

for second in range(10000):
    grid = list()
    for _ in range(HEIGHT):
        grid.append([0] * WIDTH)

    for vr in vrs:
        vr.x = (vr.x + vr.dx) % WIDTH
        vr.y = (vr.y + vr.dy) % HEIGHT

        grid[vr.y][vr.x] += 1

    s = ""
    for row in grid:
        for c in row:
            s += str(c)

    if "1" * 16 in s:
        print(second + 1)
