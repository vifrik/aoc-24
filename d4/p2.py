import string
from u import u

xs = list()


def dataparser(c):
    if c in string.ascii_uppercase:
        return c


def atuple(d, x, y):
    loc = (x[0] + y[0], x[1] + y[1])
    if 0 <= loc[0] < len(d) and 0 <= loc[1] < len(d[0]):
        return loc


def check(d, x):
    diagps = [[(1, 1), (-1, -1)], [(-1, 1), (1, -1)]]

    for diagp in diagps:
        l, r = diagp
        nx = atuple(d, x, l)
        nxx = atuple(d, x, r)

        if nx is None or nxx is None:
            return False

        c1 = d[nx[0]][nx[1]]
        c2 = d[nxx[0]][nxx[1]]
        if not (c1 == "M" and c2 == "S" or c1 == "S" and c2 == "M"):
            return False

    return True


def main():
    d = u.read_grid("i.txt", dataparser)
    s = 0

    for l_idx, l in enumerate(d):
        for c_idx, c in enumerate(l):
            if c == "A":
                xs.append((l_idx, c_idx))

    for x in xs:
        if check(d, x):
            s += 1

    print(s)


if __name__ == "__main__":
    main()
