from dataclasses import dataclass

total = 0
with open('input.txt') as f:
    for line in f:
        policy, password = map(str.strip, line.split(':'))
        min_max, letter = policy.split(' ')
        min, max = map(int, min_max.split('-'))
        occ = len(list(c for c in password if c == letter))
        if occ >= min and occ <= max:
            total += 1

print(total)
