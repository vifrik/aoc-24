import re


def main():
    with open("i.txt", "r") as f:
        lines = f.readlines()

    l = list()
    d = dict()

    for line in lines:
        p = int(re.split(r"\s+", line.strip())[0])
        l.append(p)

    for line in lines:
        p = int(re.split(r"\s+", line.strip())[1])
        if p not in d:
            d[p] = 0
        d[p] += 1

    s = 0
    for k in l:
        if k in d:
            s += d[k] * k

    print(s)


if __name__ == "__main__":
    main()
