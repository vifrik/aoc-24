import re

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

ps = [0, 0, 0, 0]

for vr in vrs:
    vr.x = (vr.x + vr.dx * N_STEPS) % WIDTH
    vr.y = (vr.y + vr.dy * N_STEPS) % HEIGHT

    if vr.x < QW and vr.y < QH:
        ps[0] += 1
    elif vr.x > WIDTH - 1 - QW and vr.y < QH:
        ps[1] += 1
    elif vr.x < QW and vr.y > HEIGHT - 1 - QH:
        ps[2] += 1
    elif vr.x > WIDTH - 1 - QW and vr.y > HEIGHT - 1 - QH:
        ps[3] += 1

s = 1
for p in ps:
    print(p)
    if p > 0:
        s *= p
print(s)
