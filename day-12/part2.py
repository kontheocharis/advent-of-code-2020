import sys
import math

waypoint_position = [10.0, 1.0]
ship_position = [0.0, 0.0]

dir_map = {
    'N': (0.0, 1.0),
    'E': (1.0, 0.0),
    'S': (0.0, -1.0),
    'W': (-1.0, 0.0)
}

def rotate_waypoint_by_deg(deg):
    theta = deg * math.pi / 180
    sin_theta = math.sin(theta)
    cos_theta = math.cos(theta)

    p = waypoint_position
    new_x = p[0] * cos_theta - p[1] * sin_theta
    new_y = p[0] * sin_theta + p[1] * cos_theta
    p[0] = new_x
    p[1] = new_y

for line in (x.strip() for x in sys.stdin):
    dir_char, val = line[0], float(line[1:])

    if dir_char in dir_map:
        waypoint_position[0] += dir_map[dir_char][0] * val
        waypoint_position[1] += dir_map[dir_char][1] * val

    elif dir_char == 'L':
        rotate_waypoint_by_deg(val)
    elif dir_char == 'R':
        rotate_waypoint_by_deg(-val)
    elif dir_char == 'F':
        for _ in range(int(val)):
            ship_position[0] += waypoint_position[0]
            ship_position[1] += waypoint_position[1]

print(int(sum(abs(s) for s in ship_position)))
