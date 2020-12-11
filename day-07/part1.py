import sys

lines = list(sys.stdin)
bags = {}

for line in lines:
    split_by_str = line.split()
    bag_name = " ".join(split_by_str[:2])
    bag_deps = " ".join(split_by_str[4:]).split(',')

    bags[bag_name] = {}

    if "no other bags" in line:
        continue

    for dep in bag_deps:
        formatted_dep = dep.strip('. ').split()
        dep_name = " ".join(formatted_dep[1:3])
        bags[bag_name][dep_name] = int(formatted_dep[0])

# print(bags)

def contains_shiny_gold(stuff):
    if len(stuff) == 0:
        return False

    if "shiny gold" in set(stuff.keys()):
        return True

    return any(contains_shiny_gold(bags[k]) for k in stuff.keys())


print(sum((1 for stuff in bags.values() if contains_shiny_gold(stuff))))

