from math import prod

tree_map = [x.strip() for x in open('input.txt')]

def calc_trees(right, down):
    count = 0
    for y in range(0, len(tree_map), down):
        if tree_map[y][int(right * y / down) % len(tree_map[0])] == '#':
            count += 1
    return count

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(prod(calc_trees(*slope) for slope in slopes))
