from sys import stdin
import math

TOTAL_ROWS = 128
TOTAL_COLS = 8

boarding_passes = [line.rstrip('\n') for line in stdin]

def get_seat_id(boarding_pass):
    row_start, row_end = (0, TOTAL_ROWS - 1)
    col_start, col_end = (0, TOTAL_COLS - 1)

    for dir in boarding_pass:
        if dir == 'F':
            row_end -= int(math.ceil((row_end - row_start) / float(2)))
        elif dir == 'B':
            row_start += int(math.ceil((row_end - row_start) / float(2)))
        elif dir == 'L':
            col_end -= int(math.ceil((col_end - col_start) / float(2)))
        elif dir == 'R':
            col_start += int(math.ceil((col_end - col_start) / float(2)))
        else:
            break

    return row_start * TOTAL_COLS + col_start

sorted_ids = sorted(get_seat_id(p) for p in boarding_passes)

for i, id in enumerate(sorted_ids):
    expected_id = sorted_ids[0] + i
    if expected_id != id:
        print(expected_id)
        break
