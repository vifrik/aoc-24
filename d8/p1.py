from libaoc.grid import Grid

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
            an1 = ap - (apz - ap)
            if grid.in_range(an1):
                ans.add(an1)

            an2 = apz - (ap - apz)
            if grid.in_range(an2):
                ans.add(an2)

print(len(ans))
