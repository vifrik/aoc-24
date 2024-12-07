import itertools

from tqdm import tqdm

operators = ["+", "*", "||"]
found_results = set()


def apply(op_list, val_list, value, target_value):
    if target_value in found_results:
        return False

    if len(op_list) == 0:
        found = value == target_value
        if found:
            found_results.add(target_value)
        return found

    op = op_list[0]
    val = val_list[0]
    if op == "+":
        value += val
    elif op == "*":
        value *= val
    elif op == "||":
        value = int(str(value) + str(val))

    return apply(op_list[1:], val_list[1:], value, target_value)


s = 0
with open("i.txt", "r") as f:
    content = f.read().strip().splitlines()
    for line in tqdm(content):
        result, rest = line.split(": ")
        result = int(result)
        rest = [int(n) for n in rest.strip().split(" ")]

        permuataions = list(itertools.product(operators, repeat=len(rest) - 1))

        for comb in permuataions:
            if apply(list(comb), rest[1:].copy(), rest[0], result):
                s += result

print(s)
