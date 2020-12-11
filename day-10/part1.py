import sys

nums = [int(x.strip()) for x in sys.stdin]

sorted_nums = sorted(nums)
sorted_nums.insert(0, 0)
sorted_nums.append(max(sorted_nums) + 3)

one_diffs = 0
three_diffs = 0

for i in range(0, len(sorted_nums) - 1):
    curr = sorted_nums[i]
    next = sorted_nums[i + 1]
    if next - curr == 0:
        continue
    if next - curr == 1:
        one_diffs += 1
    elif next - curr == 2:
        continue
    elif next - curr == 3:
        three_diffs += 1
    else:
        print(f"Found too large difference! {next-curr}")
        break

print(one_diffs * three_diffs)

