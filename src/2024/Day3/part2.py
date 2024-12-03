import re


def calc_sum_of_multiples(entries):
    entries_ints = [(int(x[0]), int(x[1])) for x in entries]
    sum = 0
    for entry in entries_ints:
        sum += entry[0] * entry[1]
    return sum


def main():
    with open('input.txt', 'r') as file:
        contents = file.read()
        groups = re.findall(
            "mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))", contents)
        do = True
        for i in range(len(groups)):
            if groups[i][3] == "do()":
                do = True
                groups[i] = ('0', '0', '', '')
            if groups[i][2] == "don't()":
                groups[i] = ('0', '0', '', '')
                do = False
            if do is False:
                groups[i] = ('0', '0', '', '')

        print(calc_sum_of_multiples(groups))


if __name__ == "__main__":
    main()
