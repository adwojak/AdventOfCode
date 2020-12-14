ALL_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse_single_passport(passport):
    parsed_passport = {}
    for element in passport.split(' '):
        if element == '':
            continue
        key, value = element.split(':')
        parsed_passport[key] = value
    return parsed_passport


with open('input') as f:
    passports = []
    single_passport = ''
    for line in f.read().split('\n'):  # brakuje ostatniego elementu
        if line == '':
            passports.append(parse_single_passport(single_passport))
            single_passport = ''
        else:
            single_passport += f' {line}'


def part_one():
    for passport in passports:
        print([key in REQUIRED_KEYS for key in passport.keys()])
    # print(len(passports))


print(part_one())
