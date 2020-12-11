import sys
from operator import and_
from functools import reduce

def get_input():
    current = []
    for line in sys.stdin:
        if line.strip() == '':
            if len(current) != 0:
                yield reduce(and_, current)
                current = []
        else:
            current.append(set(line.strip()))
    if len(current) != 0:
        yield reduce(and_, current)

inp = get_input()

print(sum(len(s) for s in inp))
