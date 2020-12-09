import sys

code = []
for line in sys.stdin:
    code.append(line)

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
        i += 1
    elif op == "jmp":
        i += int(arg)
    elif op == "acc":
        acc += int(arg)
        i += 1
else:
    print(f"Terminated fine after {i} loops")
    print(f"Acc: {acc}")


