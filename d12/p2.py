from libaoc.grid import Grid
from libaoc.point import Point
from libaoc.compass import arrows

with open("i.txt", "r") as f:
    content = f.read()

gvisisted = set()


def find_partition(grid: Grid, p: Point, visited, perims):
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
            if p not in perims:
                perims[p] = list()
            perims[p].append(dir)
            if not next_to_perim(grid, p, dir, perims):
                perimiter += 1

            continue
        nv = grid.get(np).v

        if cv != nv:
            if p not in perims:
                perims[p] = list()
            perims[p].append(dir)
            if not next_to_perim(grid, p, dir, perims):
                perimiter += 1
        else:
            rarea, rperimiter = find_partition(grid, np, visisted, perims)
            area += rarea
            perimiter += rperimiter

    return area, perimiter


def next_to_perim(grid, p, pdir, perims):
    perp1 = Point(pdir.y, -pdir.x)
    pcp = p.copy() + perp1

    while grid.in_range(pcp) and grid.get(pcp).v == grid.get(p).v:
        if grid.in_range(pcp + pdir) and grid.get(pcp + pdir).v == grid.get(p).v:
            break
        if pcp in perims:
            npp = perims[pcp]
            if pdir in npp:
                return True
        pcp += perp1

    perp2 = Point(-pdir.y, pdir.x)
    pcp = p.copy() + perp2
    while grid.in_range(pcp) and grid.get(pcp).v == grid.get(p).v:
        if grid.in_range(pcp + pdir) and grid.get(pcp + pdir).v == grid.get(p).v:
            break
        if pcp in perims:
            npp = perims[pcp]
            if pdir in npp:
                return True
        pcp += perp2

    return False


grid = Grid(content)
print(grid)
s = 0

for p in grid.get_data():
    if p.to_point() in gvisisted:
        continue

    visisted = set()
    perims = dict()
    area, perim = find_partition(grid, p.to_point(), visisted, perims)
    s += area * perim

print(s)
