from libaoc.vector import Vector
from libaoc.grid import Grid
from tqdm import tqdm

with open("i.txt", "r") as f:
    data = f.read()

grid = Grid(data)
datum = grid.find("^")
player = datum.to_point()


def check_loop(grid: Grid):
    observed_states = set()
    visited_coords = set()
    player_vec = Vector(player.x, player.y, 0, -1)

    while True:
        visited_coords.add(player_vec.to_point())
        observed_states.add(player_vec)

        while grid.get(player_vec.predict().to_point()).v == "#":
            player_vec.rotate()
        else:
            player_vec.step()

        if not grid.in_range(player_vec.predict()):
            visited_coords.add(player_vec.to_point())
            return visited_coords, False

        if player_vec in observed_states:
            return visited_coords, True


visited = check_loop(grid)[0]
print(len(visited))

s = 0
for block_pos in tqdm(visited):
    grid = Grid(data)
    grid.set(block_pos, "#")
    grid.set(datum.to_point(), "^")

    if check_loop(grid)[1]:
        s += 1

print(s)
