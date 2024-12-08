from libaoc.grid import Grid
from libaoc.vector import Vector

with open("i.txt", "r") as f:
    content = f.read()

grid = Grid(content)
print(grid)
ans = set()

for antenna in grid.get_unique_values():
    if antenna == ".":
        continue
    
    aps = grid.find_all(antenna)
    for ap_idx, ap in enumerate(aps):
        for apz in aps[ap_idx+1:]:

            d1 = apz - ap
            v1 = Vector(ap.x, ap.y, d1.x, d1.y).step()

            d2 = ap - apz
            v2 = Vector(apz.x, apz.y, d2.x, d2.y).step()

            while grid.in_range(v1):
                ans.add(v1.to_point())
                v1.step()

            while grid.in_range(v2):
                ans.add(v2.to_point())
                v2.step()

print(len(ans))
