from dataclasses import dataclass

total = 0
with open('input.txt') as f:
    for line in f:
        policy, password = map(str.strip, line.split(':'))
        min_max, letter = policy.split(' ')
        min, max = map(int, min_max.split('-'))

        if (password[min - 1] == letter) ^ (password[max - 1] == letter):
            total += 1

print(total)
