import re


def get_passports(f):
    current = []
    for line in f:
        if line.strip() == '':
            if current != []:
                yield current
                current = []
        else:
            current.extend(line.strip().split())
    if len(current) != 0:
        yield current


REQUIRED_PASSPORT_FIELD_RULES = {
    'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    'hgt': lambda x: x[-2:] in {"cm", "in"} and
    (150 <= int(x[:-2]) <= 193 if x[-2:] == "cm" else 59 <= int(x[:-2]) <= 76),
    'hcl': lambda x: re.match("^#[0-9a-f]{6}$", x) is not None,
    'ecl': lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    'pid': lambda x: re.match("^[0-9]{9}$", x) is not None,
}

REQUIRED_PASSPORT_FIELDS = set(REQUIRED_PASSPORT_FIELD_RULES.keys())

OPTIONAL_PASSPORT_FIELDS = {
    'cid',
}


def is_valid(passport):
    props = dict(x.split(':') for x in passport)
    if not REQUIRED_PASSPORT_FIELDS.issubset(set(props.keys())) and (
            REQUIRED_PASSPORT_FIELDS
            | OPTIONAL_PASSPORT_FIELDS).issuperset(set(props.keys())):
        return False
    for prop, value in ((k, v) for (k,v) in props.items() if k not in OPTIONAL_PASSPORT_FIELDS):
        try:
            if not REQUIRED_PASSPORT_FIELD_RULES.get(prop, lambda x: False)(value):
                return False
        except ValueError:
            return False
    return True


print(sum(int(is_valid(p)) for p in get_passports(open('input.txt'))))
