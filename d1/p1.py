import re


def main():
    with open("i.txt", "r") as f:
        lines = f.readlines()

    l1 = list()
    l2 = list()

    for line in lines:
        p1, p2 = re.split(r"\s+", line.strip())
        l1.append(int(p1))
        l2.append(int(p2))

    l1.sort()
    l2.sort()

    s = 0
    for x, y in zip(l1, l2):
        s += abs(x - y)

    print(s)


if __name__ == "__main__":
    main()
