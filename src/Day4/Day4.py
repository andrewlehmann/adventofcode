

def validate_passport(passport, required_keys, allowed_hair_color_chars): 
    if any([key not in passport.keys() for key in required_keys]):
        return False

    birth_year = int(passport["byr"])
    if birth_year < 1920 or birth_year > 2002:
        return False

    issue_year = int(passport["iyr"])
    if issue_year < 2010 or issue_year > 2020:
        return False
    
    expiration_year = int(passport["eyr"])
    if expiration_year < 2020 or expiration_year > 2030:
        return False

    height_num = passport["hgt"][:-2]
    height_unit = passport["hgt"][-2:]

    if not height_num: 
        return False

    height_num_int = int(height_num)
    if height_unit == "cm" and (height_num_int < 150 or height_num_int > 193):
        return False

    if height_unit == "in" and (height_num_int < 59 or height_num_int > 76):
        return False

    hair_color = passport["hcl"]
    if len(hair_color) != 7 or hair_color[0] != '#':
        return False

    if not all([char in allowed_hair_color_chars for char in hair_color[-6:]]):
        return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    passport_id = passport["pid"]

    if len(passport_id) != 9 or not passport_id.isnumeric():
        return False

    return True

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
allowed_hair_color_chars = list('abcdefABCDEF0123456789')

with open("src\Day4\input.txt") as myfile:
    lines = myfile.read().split('\n\n')
    input = [line.replace('\n', ' ').split(' ') for line in lines]

    input_dict = [dict([entry.split(':') for entry in passport]) for passport in input]

    result = [validate_passport(passport, required_keys, allowed_hair_color_chars) for passport in input_dict].count(True)
    print(result)