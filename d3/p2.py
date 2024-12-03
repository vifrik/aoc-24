from u import u


def main():
    d = u.read_tokens("i.txt", r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
    s = 0
    enabled = True
    for t in d:
        if t[2] != "":
            enabled = True
        elif t[3] != "":
            enabled = False
        elif enabled:
            l, r = int(t[0]), int(t[1])
            s += l * r

    print(s)


if __name__ == "__main__":
    main()
