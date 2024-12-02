def is_level_safe(level):
    is_increasing = level[1] - level[0] > 0
    for i in range(len(level) - 1):
        diff = level[i+1] - level[i]
        if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            return False
        if (abs(diff) < 1 or abs(diff) > 3):
            return False
    return True


def main():
    levels = []
    with open('input.txt', 'r') as file:
        for line in file:
            level = [int(item) for item in line.split()]
            levels.append(level)
    safe_levels = [is_level_safe(level) for level in levels]

    print(safe_levels.count(True))


if __name__ == "__main__":
    main()
