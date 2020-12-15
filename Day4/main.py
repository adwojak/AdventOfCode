from re import match

ALL_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
REQUIRED_KEYS_LENGTH = len(REQUIRED_KEYS)
CM = 'cm'
IN = 'in'
BYR = 'byr'
IYR = 'iyr'
EYR = 'eyr'
HGT = 'hgt'
HCL = 'hcl'
ECL = 'ecl'
PID = 'pid'
CID = 'cid'
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
RE_HAIR_COLOR_PATTERN = r'#(\d|[a-f]){6}'
RE_PASSPORT_ID = r'\d{9}'


def parse_single_passport(passport):
    parsed_passport = {}
    for element in passport.split(' '):
        if element:
            key, value = element.split(':')
            parsed_passport[key] = value
    return parsed_passport


with open('input') as f:
    passports = []
    single_passport = ''
    for line in f.read().split('\n'):
        if line:
            single_passport += f' {line}'
        else:
            passports.append(parse_single_passport(single_passport))
            single_passport = ''
    passports.append(parse_single_passport(single_passport))


def count_passports_with_required_keys(passports):
    valid_passports = 0
    for passport in passports:
        valid_keys = len(passport) - 1 if CID in passport.keys() else len(passport)
        if valid_keys >= REQUIRED_KEYS_LENGTH:
            valid_passports += 1
    return valid_passports


def validate_heigth(value):
    length_unit = value[-2:]
    if not length_unit.isalpha():
        return False
    length_value = int(value[:-2])
    if length_unit == CM:
        return 150 <= length_value <= 193
    elif length_unit == IN:
        return 59 <= length_value <= 76
    return False


VALIDATION_MAP = {
    BYR: lambda value: 1920 <= int(value) <= 2002,
    IYR: lambda value: 2010 <= int(value) <= 2020,
    EYR: lambda value: 2020 <= int(value) <= 2030,
    HGT: validate_heigth,
    HCL: lambda value: match(RE_HAIR_COLOR_PATTERN, value),
    ECL: lambda value: value in EYE_COLORS,
    PID: lambda value: match(RE_PASSPORT_ID, value),
    CID: lambda value: True
}


def is_valid_passport(passport):
    return all([VALIDATION_MAP[key](value) for key, value in passport.items()])


def part_one():
    return count_passports_with_required_keys(passports)


def part_two():
    # qwe = [passport for passport in passports if is_valid_passport(passport)]
    # print([len(a) for a in qwe])
    # for aaa in qwe:
    #     if len(aaa) < 6:
    #         print(aaa)
    #         # blad ze jedno wylicza jako poprawne mimo ze nie jest
    return count_passports_with_required_keys([passport for passport in passports if is_valid_passport(passport)])


# print(part_one())
print(part_two())
