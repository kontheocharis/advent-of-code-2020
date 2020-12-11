import os

entries = []
with open('input.txt') as f:
    for line in f:
        entries.append(int(line))

for idx1, entry1 in enumerate(entries):
    for idx2, entry2 in enumerate(entries):
        for idx3, entry3 in enumerate(entries):
            if idx1 == idx2 or idx1 == idx3 or idx2 == idx3:
                continue
            sum = entry1 + entry2 + entry3
            if sum == 2020:
                print(f"{entry1} + {entry2} + {entry3} = 2020. Product is {entry1 * entry2 * entry3}")

