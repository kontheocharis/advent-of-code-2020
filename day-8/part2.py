import sys

code = []
for line in sys.stdin:
    code.append(line)



for j in range(len(code)):
    acc = 0
    ran = set()
    i = 0
    while i < len(code):
        if i in ran:
            print(f"Stopping at {i} because loop.")
            print(f"Acc: {acc}")
            break
        ran.add(i)
        op, arg = code[i].split()

        if op == "nop":
            if i == j:
                i += int(arg)
            else:
                i += 1
        elif op == "jmp":
            if i == j:
                i += 1
            else:
                i += int(arg)
        elif op == "acc":
            acc += int(arg)
            i += 1

    else:
        print(f"Terminated fine after {i} loops")
        print(f"Acc: {acc}")
        break
