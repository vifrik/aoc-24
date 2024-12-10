with open("i.txt", "r") as f:
    content = f.read().strip()


# p // 2 >> 9, needs more than char to store
class Datum:
    def __init__(self, v) -> None:
        self.v = v


p = 0
s = list()
while p < len(content):
    f_id = content[p]
    for _ in range(int(f_id)):
        s.append(Datum(p // 2))
    p += 1
    if p >= len(content):
        break
    p_id = content[p]
    for _ in range(int(p_id)):
        s.append(Datum(-1))
    p += 1


# shift
p1 = 0
p2 = len(s) - 1
while p1 < p2:
    while p1 < p2 and s[p1].v != -1:
        p1 += 1
    while p1 < p2 and s[p2].v == -1:
        p2 -= 1

    t = s[p1]
    s[p1] = s[p2]
    s[p2] = t

# checksum
p = 0
chk = 0
while s[p].v != -1:
    chk += p * s[p].v
    p += 1

print(chk)
