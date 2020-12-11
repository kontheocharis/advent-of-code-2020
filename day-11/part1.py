from itertools import product
import sys

def get_new_seats(seats):
    return [list(x) for x in seats]

def count_adjacent(x, y, seats, cond):
    x_indices = [x]
    y_indices = [y]

    if x > 0:
        x_indices.append(x - 1)
    if y > 0:
        y_indices.append(y - 1)
    if x < len(seats[0]) - 1:
        x_indices.append(x + 1)
    if y < len(seats) - 1:
        y_indices.append(y + 1)

    return sum(int(cond(seats[j][i])) for i, j in product(x_indices, y_indices) if (x, y) != (i, j))

def run_automata(seats):
    modified = False
    new_seats = get_new_seats(seats)
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == 'L':
                occupied = count_adjacent(x, y, seats, lambda s: s == '#')
                if occupied == 0:
                    new_seats[y][x] = '#'
                    modified = True
            elif seats[y][x] == '#':
                occupied = count_adjacent(x, y, seats, lambda s: s == '#')
                if occupied >= 4:
                    new_seats[y][x] = 'L'
                    modified = True
    return modified, new_seats

orig_seats = [list(x.strip()) for x in sys.stdin]
modified = True
curr_seats = get_new_seats(orig_seats)
while modified:
    modified, new_seats = run_automata(curr_seats)
    curr_seats = new_seats

print(sum(1 for x in range(len(curr_seats[0])) for y in range(len(curr_seats)) if curr_seats[y][x] == '#'))
