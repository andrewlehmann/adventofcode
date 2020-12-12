# Day 3

def go_downhill(slope, hill_data):
    current_location = (0, 0)
    hill_height = len(hill_data)
    hill_length = len(hill_data[0])
    num_trees_encountered = 0

    while True:
        next_x_location = (current_location[0] + slope[0]) % hill_length
        next_y_location = current_location[1] + slope[1]

        if (next_y_location >= hill_height):
            return num_trees_encountered

        current_location = (next_x_location, next_y_location)

        if (hill_data[next_y_location][next_x_location]) == '#':
            num_trees_encountered += 1

    return num_trees_encountered


def main():
    input_data = open("input.txt")
    lines = input_data.readlines()
    parsed_data = [[char for char in line.rstrip('\n')] for line in lines]

    # Part 1
    result = go_downhill((3, 1), parsed_data)
    print("Part 1: " + str(result))

    # Part 2
    result2 = (
        go_downhill((3, 1), parsed_data) *
        go_downhill((1, 1), parsed_data) *
        go_downhill((5, 1), parsed_data) *
        go_downhill((7, 1), parsed_data) *
        go_downhill((1, 2), parsed_data))

    print("Part 2: " + str(result2))

if __name__ == "__main__":
    main()
