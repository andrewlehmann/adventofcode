def get_distance_between_lists(first_list, second_list):
    first_list.sort()
    second_list.sort()
    distance = 0
    for i in range(len(first_list)): # assuming lists are same length
        print(first_list[i], second_list[i])
        distance += abs(first_list[i] - second_list[i])
    return distance

def main():
    first_list = []
    second_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            columns = line.split()
            first_list.append(int(columns[0]))
            second_list.append(int(columns[1]))

    print(get_distance_between_lists(first_list, second_list))


if __name__ == "__main__":
    main()
