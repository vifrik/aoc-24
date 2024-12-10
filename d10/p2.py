from libaoc.grid import Grid
from libaoc.vector import Vector
from libaoc.compass import arrows

with open("i.txt", "r") as f:
    content = f.read()

def walk(grid, pos, nines):
    if grid.get(pos).v == "9":
        if pos not in nines:
            nines[pos] = 0
        nines[pos] += 1

    current_val = int(grid.get(pos).v)
    
    dirs = arrows.values()
    for dir in dirs:
        v = Vector(pos.x, pos.y, dir.x, dir.y)
        next_v = v.predict()
        if grid.in_range(next_v):
            next_value = int(grid.get(next_v.to_point()).v)
            if next_value == current_val + 1:
                walk(grid, v.step().to_point(), nines)

grid = Grid(content)
print(grid)

s = 0
for p in grid.find_all("0"):
    nines = dict()
    x = walk(grid, p, nines)
    s += sum([v for v in nines.values()])
print(s)
