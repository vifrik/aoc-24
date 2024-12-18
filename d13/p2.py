import re


def min_cost(ax, ay, bx, by, rx, ry):
    b, br = divmod(ay * rx - ax * ry, ay * bx - ax * by)
    a, ar = divmod(rx - b * bx, ax)

    if ar or br:
        return 0

    return 3 * a + b


with open("i.txt", "r") as f:
    content = f.read()

machines = content.split("\n\n")
parsed_machines = list()
for machine in machines:
    vals = re.findall(r"\d+", machine)
    parsed_machines.append(tuple(map(int, vals)))

s = 0
padding = 10000000000000
for machine in parsed_machines:
    ax, ay, bx, by, rx, ry = machine
    cost = min_cost(ax, ay, bx, by, rx + padding, ry + padding)
    s += cost

print(s)
