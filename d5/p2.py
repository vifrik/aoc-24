import re
from u import u

with open("i.txt", "r") as f:
    data = f.read()
    p1, p2 = re.split(r"\n\n", data)

p1 = u.read_numbers(p1)
p2 = u.read_numbers(p2)

# l must go before r
d = dict()
for p in p1:
    l, r = p
    if l not in d:
        d[l] = [r]
    else:
        d[l].append(r)

iis = list()
for i in p2:
    wrong = False
    irev = i[::-1]
    # print(irev)
    for n_idx, n in enumerate(irev[:-1]):
        for _, nn in enumerate(irev[n_idx + 1 :]):
            if n in d and nn in d[n]:
                iis.append(i)
                wrong = True
                break
        if wrong:
            break

s = 0
for i in iis:
    wrong = False
    right_order = list()

    for n in i:
        found = False

        if len(right_order) == 0:
            right_order.append(n)
            continue

        for v_idx, v in enumerate(right_order):
            if n in d and v in d[n]:
                continue
            right_order.insert(v_idx, n)
            found = True
            break

        if not found:
            right_order.append(n)

    median = right_order[len(right_order) // 2]
    s += median


print(s)
