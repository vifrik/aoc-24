from libaoc.grid import Grid
from libaoc.compass import compass
from collections import defaultdict
from heapq import heappop, heappush

with open("i.txt", "r") as f:
    content = f.read()
    grid = Grid(content)

print(grid)


def dijkstra(grid, start):
    heap = [(0, start, compass["e"], [start])]
    costs = defaultdict(lambda: float("inf"))
    best_cost = float("inf")
    seen_paths = []

    while heap:
        cost, pos, dir, path = heappop(heap)

        if cost > costs[pos, dir]:
            continue
        costs[pos, dir] = cost

        if grid.get(pos).v == "E" and cost <= best_cost:
            seen_paths += path
            best_cost = cost

        for d, c in [(dir, 1), (dir.rotate(), 1000 + 1), (dir.rotate_ccw(), 1000 + 1)]:
            npos = pos + d
            if not grid.in_range(npos):
                continue
            if grid.get(npos).v == "#":
                continue
            heappush(heap, (cost + c, npos, d, path + [npos]))

    return len(set(seen_paths))


start = grid.find("S")
places_to_sit = dijkstra(grid, start)
print(places_to_sit)
