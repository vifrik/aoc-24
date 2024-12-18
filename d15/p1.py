from libaoc.grid import Grid
from libaoc.compass import arrows 

with open("i.txt", "r") as f:
    grid, moves = f.read().strip().split("\n\n")
    grid = Grid(grid)
    moves = moves.replace("\n", "")

print(grid)
print(moves)

player = grid.find("@")
if player is None:
    exit(0)

grid.set(player, ".")

for move in moves:
    dir = arrows[move]
    np = player + dir
    ns = grid.get(np).v
    print(move)

    if ns == ".":
        player = np
    elif ns == "#":
        continue
    elif ns == "O":
        nss = np.copy()
        stack = list()
        while grid.get(nss).v == "O":
            stack.append(nss)
            nss += dir
        if grid.get(nss).v == "#":
            continue

        while len(stack) > 0:
            sv = stack.pop()
            grid.set(sv + dir, "O")
            grid.set(sv, ".")
        player = np

    grid.set(player, "@")
    print(grid)
    grid.set(player, ".")

boxes = grid.find_all("O")
s = 0
for box in boxes:
    print(box)
    s += box.x + 100 * box.y

print(s)

