from u import u


# love a good brute
def valid(r):
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
            print("X" + str(r))
            return True

        last = i
    return False


def main():
    d = u.read_ssv("i.txt")
    s = 0

    for r in d[:40]:
        parts = list()
        print(" " + str(r))
        for iidx in range(len(r)):
            part = list()
            for oidx in range(len(r)):
                if iidx != oidx:
                    part.append(r[oidx])
            parts.append(part)

        for part in parts:
            if valid(part):
                s += 1
                break

    print(s)


if __name__ == "__main__":
    main()
