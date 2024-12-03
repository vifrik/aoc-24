from u import u


def main():
    d = u.read_tokens("s.txt", r"mul\((\d+),(\d+)\)")
    s = 0
    for t in d:
        l, r = int(t[0]), int(t[1])
        s += l * r

    print(s)


if __name__ == "__main__":
    main()
