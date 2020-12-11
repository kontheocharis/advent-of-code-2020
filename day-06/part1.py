import sys

def get_input():
    current = set()
    for line in sys.stdin:
        if line.strip() == '':
            if len(current) != 0:
                yield current
                current = set()
        else:
            current = current | set(line.strip())
    if len(current) != 0:
        yield current

inp = get_input()

print(sum(len(s) for s in inp))
