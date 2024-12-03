import re


def calc_sum_of_multiples(entries):
    sum = 0
    for entry in entries:
        sum += entry[0] * entry[1]
    return sum


def main():
    with open('input.txt', 'r') as file:
        contents = file.read()
        groups = [(int(x[0]), int(x[1]))
                  for x in re.findall("mul\((\d+),(\d+)\)", contents)]
        print(calc_sum_of_multiples(groups))


if __name__ == "__main__":
    main()
