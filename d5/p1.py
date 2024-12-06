import re
from u import u

with open("i.txt", "r") as f:
    data = f.read()
    p1, p2 = re.split(r"\n\n", data)

p1 = u.read_numbers(p1)
p2 = u.read_numbers(p2)

d = dict()
for p in p1:
    l, r = p
    if l not in d:
        d[l] = [r]
    else:
        d[l].append(r)

s = 0

for i in p2:
    wrong = False
    irev = i[::-1]
    #print(irev)
    for n_idx, n in enumerate(irev[:-1]):
        for _, nn in enumerate(irev[n_idx + 1:]):
            if n in d and nn in d[n]:
                wrong = True
                break
        if wrong:
            break

        if n_idx == len(i) - 2:
            median = i[len(i) // 2]
            s += median

print(s)
