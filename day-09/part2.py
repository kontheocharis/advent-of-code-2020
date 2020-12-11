import sys

numbers = list(enumerate((int(x.strip()) for x in sys.stdin)))

INVALID_NUM = 776203571

def find_invalid():
    for i, num_start in numbers:
        for j, num_end in numbers[i+1:]:
            rng = list(zip(*numbers[i:j+1]))[1]
            if sum(rng) == INVALID_NUM:
                print(max(rng) + min(rng))
                return


find_invalid()

