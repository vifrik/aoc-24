from libaoc.grid import Grid
from libaoc.point import Point
from libaoc.compass import arrows

with open("i.txt", "r") as f:
    content = f.read()

gvisisted = set()


def find_partition(grid: Grid, p: Point, visited):
    if p in visited:
        return 0, 0

    cv = grid.get(p).v
    dirs = arrows.values()

    area = 1
    perimiter = 0

    visisted.add(p)
    gvisisted.add(p)

    for dir in dirs:
        np = p + dir
        if not grid.in_range(np):
            perimiter += 1
            continue
        nv = grid.get(np).v

        if cv != nv:
            perimiter += 1
        else:
            rarea, rperimiter = find_partition(grid, np, visisted)
            area += rarea
            perimiter += rperimiter

    return area, perimiter


grid = Grid(content)
s = 0

for p in grid.get_data():
    if p.to_point() in gvisisted:
        continue

    visisted = set()
    area, perim = find_partition(grid, p.to_point(), visisted)
    s += area * perim

print(s)
