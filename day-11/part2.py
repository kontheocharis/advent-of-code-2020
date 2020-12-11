from itertools import product
import sys

def get_new_seats(seats):
    return [list(x) for x in seats]

def count_adjacent(x, y, seats):
    dirs = list(dir for dir in product([1, 0, -1], repeat=2) if dir != (0, 0))

    count = 0
    for step_x, step_y in dirs:
        curr_x = x + step_x
        curr_y = y + step_y
        while True:
            if not (0 <= curr_x < len(seats[0]) and 0 <= curr_y < len(seats)):
                break

            if seats[curr_y][curr_x] == '#':
                count += 1
                break
            elif seats[curr_y][curr_x] == 'L':
                break

            curr_x += step_x
            curr_y += step_y

    return count

def run_automata(seats):
    modified = False
    new_seats = get_new_seats(seats)
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == 'L':
                occupied = count_adjacent(x, y, seats)
                if occupied == 0:
                    new_seats[y][x] = '#'
                    modified = True
            elif seats[y][x] == '#':
                occupied = count_adjacent(x, y, seats)
                if occupied >= 5:
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
