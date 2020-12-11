import sys

nums = [int(x.strip()) for x in sys.stdin]

nums.append(0)
nums.append(max(nums) + 3)

graph = {}

for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
        if i == j:
            continue

        valid_diffs = {1, 2, 3}
        curr_diff = num2 - num1

        if curr_diff in valid_diffs:
            graph.setdefault(num1, {})[num2] = curr_diff
        else:
            continue

mem = {}

def connections_for(num):
    if num not in graph:
        return 1

    if num in mem:
        return mem[num]

    connections = sum(connections_for(desc) for desc in graph[num].keys())
    mem[num] = connections

    return connections

print(connections_for(0))
