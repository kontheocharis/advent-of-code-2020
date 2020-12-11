import sys

numbers = list(enumerate((int(x.strip()) for x in sys.stdin)))

for i, number in numbers[25:]:
    for j, prev1 in numbers[i-25:i]:
        found = False
        for k, prev2 in numbers[i-25:i]:
            if j != k:
                if prev1 + prev2 == number:
                    found = True
        if found:
            break
    else:
        print(number)
        break


