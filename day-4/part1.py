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


REQUIRED_PASSPORT_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}

OPTIONAL_PASSPORT_FIELDS = {
    'cid',
}


def is_valid(passport):
    props = {x.split(':')[0] for x in passport}
    return REQUIRED_PASSPORT_FIELDS.issubset(props) and (
        REQUIRED_PASSPORT_FIELDS | OPTIONAL_PASSPORT_FIELDS).issuperset(props)


print(sum(int(is_valid(p)) for p in get_passports(open('input.txt'))))
