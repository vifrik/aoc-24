from libaoc.point import Point


compass = {
    "n": Point(-1, 0),
    "e": Point(0, 1),
    "s": Point(1, 0),
    "w": Point(0, -1),
    "ne": Point(-1, 1),
    "se": Point(1, 1),
    "sw": Point(1, -1),
    "nw": Point(-1, -1),
}

arrows = {
    "^": compass["n"],
    ">": compass["e"],
    "<": compass["w"],
    "v": compass["s"],
}

pipes = {
    "|": (compass["n"], compass["s"]),
    "-": (compass["w"], compass["e"]),
    "L": (compass["n"], compass["e"]),
    "J": (compass["n"], compass["w"]),
    "7": (compass["w"], compass["s"]),
    "F": (compass["s"], compass["e"]),
}
