from u import u


def main():
    d = u.read_ssv("i.txt")

    s = 0

    for r in d:
        last = None
        dec = None
        for idx in range(1, len(r)):
            last = r[idx - 1]
            i = r[idx]
            if dec is None:
                dec = i < last

            if dec != (i < last):
                break

            if abs(i - last) < 1 or abs(i - last) > 3:
                break

            if idx == len(r) - 1:
                print(r)
                s += 1
                break

            last = i
    print(s)


if __name__ == "__main__":
    main()
