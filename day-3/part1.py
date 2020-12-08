tree_map = [x.strip() for x in open('input.txt')]

count = 0
for y in range(0, len(tree_map)):
    if tree_map[y][(3 * y) % len(tree_map[0])] == '#':
        count += 1
print(count)
