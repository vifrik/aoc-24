from collections import Counter

with open("i.txt", "r") as f:
    content = f.read().strip()
    stones = [int(s) for s in content.split()]
    sc = Counter(stones)

for _ in range(25):
    new_sc = Counter()
    for s, c in sc.items():
        ss = str(s)
        if s == 0:
            new_sc[1] += c
        elif len(ss) % 2 == 0:
            s1, s2 = int(ss[len(ss) // 2 :]), int(ss[: len(ss) // 2])
            new_sc[s1] += c
            new_sc[s2] += c
        else:
            new_sc[s * 2024] += c
    sc = new_sc

print(sum(sc.values()))
