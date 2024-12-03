import re


def read_grid(filename, dataparser):
    with open(filename, "r") as f:
        lines = f.readlines()

        d = list()

        for line in lines:
            rd = list()
            for col in line:
                v = dataparser(col)
                if v is None:
                    continue

                rd.append(v)

            if len(rd) > 0:
                d.append(rd)

        return d


def read_ssv(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

        d = list()

        for line in lines:
            rd = re.split(r"\s+", line.strip())
            rd = [int(r) for r in rd]

            if len(rd) > 0:
                d.append(rd)

        return d

def read_tokens(filename, regex):
    with open(filename, 'r') as f:
        content = f.read()
        return re.findall(regex, content)
