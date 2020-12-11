import os

entries = []
with open('input.txt') as f:
    for line in f:
        entries.append(int(line))

for idx1, entry1 in enumerate(entries):
    for idx2, entry2 in enumerate(entries[idx1+1:]):
        sum = entry1 + entry2
        if sum == 2020:
            print(f"Found entries {entry1} (line {idx1 + 1}) and {entry2} (line {idx2 + 1}) that sum to 2020, and their product is {entry1 * entry2}")

