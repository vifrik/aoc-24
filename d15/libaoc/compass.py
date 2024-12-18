from libaoc.point import Point


compass = {
    "n": Point(0, -1),
    "e": Point(1, 0),
    "s": Point(0, 1),
    "w": Point(-1, 0),
    "ne": Point(1, -1),
    "se": Point(1, 1),
    "sw": Point(-1, 1),
    "nw": Point(-1, -1),
}

arrows = {
    "^": compass["n"],
    ">": compass["e"],
    "v": compass["s"],
    "<": compass["w"],
}

pipes = {
    "|": (compass["n"], compass["s"]),
    "-": (compass["w"], compass["e"]),
    "L": (compass["n"], compass["e"]),
    "J": (compass["n"], compass["w"]),
    "7": (compass["w"], compass["s"]),
    "F": (compass["s"], compass["e"]),
}
