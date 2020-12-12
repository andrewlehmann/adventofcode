def validate_passport(passport, required_keys): 
    if (all([key in passport.keys() for key in required_keys])):
        return True
    return False

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("src\Day4\input.txt") as myfile:
    lines = myfile.read().split('\n\n')
    input = [line.replace('\n', ' ').split(' ') for line in lines]

    input_dict = [dict([entry.split(':') for entry in passport]) for passport in input]

    result = [validate_passport(passport, required_keys) for passport in input_dict].count(True)
    print(result)