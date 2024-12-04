import string
from u import u

xs = list()


def dataparser(c):
    if c in string.ascii_uppercase:
        return c


def check(d, x):
    dirs = [
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    chars = [c for c in "XMAS"]
    s = 0

    for dir in dirs:
        loc = x
        for c in chars[1:]:
            loc = (loc[0] + dir[0], loc[1] + dir[1])
            if not 0 <= loc[0] < len(d) or not 0 <= loc[1] < len(d[0]):
                break
            if d[loc[0]][loc[1]] != c:
                break
            if c == "S":
                s += 1

    return s


def main():
    d = u.read_grid("i.txt", dataparser)
    s = 0

    for l_idx, l in enumerate(d):
        for c_idx, c in enumerate(l):
            if c == "X":
                xs.append((l_idx, c_idx))

    for x in xs:
        s += check(d, x)

    print(s)


if __name__ == "__main__":
    main()
