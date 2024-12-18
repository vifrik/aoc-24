import re

def mincost(ax, ay, bx, by, px, py):
    b, brem = divmod(ay * px - ax * py, ay * bx - ax * by)
    a, arem = divmod(px - b * bx, ax)
    return 0 if arem or brem else a * 3 + b

with open("i.txt", "r") as f:
    content = f.read()
machines = [tuple(map(int, re.findall(r'\d+', machine)))
            for machine in content.split('\n\n')]
print(sum(mincost(*m) for m in machines))
base = 10000000000000
print(sum(mincost(ax, ay, bx, by, base + px, base + py)
        for ax, ay, bx, by, px, py in machines))
