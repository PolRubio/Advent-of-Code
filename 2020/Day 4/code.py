import re

file = open("input", "r")

file_list = file.read().split('\n\n')
file_list_clean = []
passports = []
for item in file_list:
    file_list_clean.append(item.replace('\n', ' '))

for item in file_list_clean:
    x = item.split()
    passport = {}
    for key_value in x:
        key_value = key_value.split(':')
        key = key_value[0]
        value = key_value[1]

        passport.update({key: value})
        # print(passport)
    passports.append(passport)


# print(passports)

def present(passport):
    if ('byr' in passport and
            'iyr' in passport and
            'eyr' in passport and
            'hgt' in passport and
            'hcl' in passport and
            'ecl' in passport and
            'pid' in passport):
        return True
    else:
        return False


def valid_byr(byr):
    if len(byr) == 4 and 1920 <= int(byr) <= 2002:
        return True
    else:
        return False


def valid_iyr(iyr):
    if len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False


def valid_eyr(eyr):
    if len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False


def valid_hgt(hgt):
    if hgt[-2:] == 'cm':
        if 150 <= int(hgt[:-2]) <= 193:
            return True
        else:
            return False

    elif hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            return True
        else:
            return False

    else:
        return False


def valid_hcl(hcl):
    if (len(hcl) == 7 and hcl[0] == "#"):
        return True
    else:
        return False


def valid_ecl(ecl):
    if ('amb' == ecl or
        'blu' == ecl or
        'brn' == ecl or
        'gry' == ecl or
        'grn' == ecl or
        'hzl' == ecl or
        'oth' == ecl):
        return True
    else:
        return False


def valid_pid(pid):
    if len(pid) == 9:
        return True
    else:
        return False


valid_passports = 0

for passport in passports:
    if (present(passport) and
        valid_byr(passport['byr']) and
        valid_iyr(passport['iyr']) and
        valid_eyr(passport['eyr']) and
        valid_hgt(passport['hgt']) and
        valid_hcl(passport['hcl']) and
        valid_ecl(passport['ecl']) and
        valid_pid(passport['pid'])):
        valid_passports += 1

print(valid_passports)
