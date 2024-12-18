from libaoc.grid import Grid
from libaoc.compass import arrows, compass

with open("i.txt", "r") as f:
    grid, moves = f.read().strip().split("\n\n")
    moves = moves.replace("\n", "")

# extend grid
new_grid = ""
for row in grid:
    for c in row:
        if c == "@":
            new_grid += "@."
        elif c == "O":
            new_grid += "[]"
        elif c == "\n":
            new_grid += c
        else:
            new_grid += c * 2

grid = Grid(new_grid)
print(grid)
print(moves)

player = grid.find("@")
grid.set(player, ".")


def can_vertical(grid, dir, point, stack, depth=0):
    c = grid.get(point).v
    can = True
    other = None

    if depth not in stack:
        stack[depth] = list()

    if c == "#":
        return False
    elif c == ".":
        return True
    elif c == "[":
        if point not in stack[depth]:
            stack[depth].append(point)
            other = point + compass["e"]
            stack[depth].append(other)
    elif c == "]":
        if point not in stack[depth]:
            other = point + compass["w"]
            stack[depth].append(other)
            stack[depth].append(point)
    else:
        print("wtf", c)

    return (
        can
        and can_vertical(grid, dir, point + dir, stack, depth + 1)
        and (
            can_vertical(grid, dir, other + dir, stack, depth + 1)
            if other is not None
            else True
        )
    )


for move in moves:
    dir = arrows[move]
    np = player + dir
    ns = grid.get(np).v
    print(move)

    if ns == ".":
        player = np
    elif ns == "#":
        continue
    elif ns in ["[", "]"]:
        nss = np.copy()
        stack = list()
        if dir in [compass["n"], compass["s"]]:
            d = dict()
            can = can_vertical(grid, dir, nss, d)
            if not can:
                continue

            sorted_keys = sorted(d)
            for key in sorted_keys:
                stack.extend(d[key])
        else:
            while grid.get(nss).v in ["[", "]"]:
                stack.append(nss)
                nss += dir
        if grid.get(nss).v == "#":
            continue

        while len(stack) > 0:
            sv = stack.pop()
            grid.set(sv + dir, grid.get(sv).v)
            grid.set(sv, ".")
        player = np

    grid.set(player, "@")
    os.system("clear")
    print(grid)
    grid.set(player, ".")
    # input()

boxes = grid.find_all("[")
s = 0
for box in boxes:
    print(box)
    s += box.x + 100 * box.y

print(s)
