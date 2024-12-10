with open("i.txt", "r") as f:
    content = f.read().strip()


# p // 2 >> 9, needs more than char to store
class Datum:
    def __init__(self, v, start, width) -> None:
        self.v = v
        self.start = start
        self.width = width

    def __str__(self) -> str:
        return f"({self.v}, {self.start}, {self.start + self.width})"

    def __repr__(self) -> str:
        return self.__str__()


p = 0
s = list()
while p < len(content):
    offset = 0
    if len(s) > 0:
        offset = s[-1].start + s[-1].width
    f_id = content[p]
    s.append(Datum(p // 2, offset, int(f_id)))
    p += 1
    if p >= len(content):
        break
    p_id = content[p]
    s.append(Datum(-1, offset + int(f_id), int(p_id)))
    p += 1


# shift
for f in s[::-1]:
    if f.v == -1:
        continue

    for g_idx, g in enumerate(s):
        if g.v != -1:
            continue

        if g.width == 0:
            continue

        if g.width >= f.width and g.start < f.start:
            g.v = f.v
            if g.width != f.width:
                s.insert(g_idx + 1, Datum(-1, g.start + f.width, g.width - f.width))
                g.width = f.width

            f.v = -1
            break


# checksum
p = 0
chk = 0
for d in s:
    if d.v == -1:
        p += d.width
        continue

    for _ in range(d.width):
        chk += int(d.v) * p
        p += 1

print(chk)

# dump string
expanded = "".join(
    str(x.v) * x.width if x.v != -1 else "." * x.width
    for x in s
)
False and print(f"{expanded}")
