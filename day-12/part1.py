import sys
import math

direction = 0.0
position = [0.0, 0.0]

dir_map = {
    'N': (0.0, 1.0),
    'E': (1.0, 0.0),
    'S': (0.0, -1.0),
    'W': (-1.0, 0.0)
}

for line in (x.strip() for x in sys.stdin):
    dir_char, val = line[0], float(line[1:])

    if dir_char in dir_map:
        position[0] += dir_map[dir_char][0] * val
        position[1] += dir_map[dir_char][1] * val

    elif dir_char == 'L':
        direction += val
    elif dir_char == 'R':
        direction -= val
    elif dir_char == 'F':
        position[0] += val * math.cos(direction * math.pi / 180)
        position[1] += val * math.sin(direction * math.pi / 180)

print(round(sum(abs(x) for x in position)))

'''
F10
N3
F7
R90
F11
'''
