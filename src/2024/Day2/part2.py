def exclude_entry(level, index):
    if (index < 0):
        return level
    copy = level.copy()
    copy.pop(index)
    return copy


def is_level_safe(level, is_recursive=False):  # only allow one recursive call
    is_increasing = level[1] - level[0] > 0
    for i in range(len(level) - 1):
        diff = level[i+1] - level[i]
        if (is_increasing and diff < 0) or (not is_increasing and diff > 0) or (abs(diff) < 1 or abs(diff) > 3):
            if is_recursive:
                return False
            return [is_level_safe(exclude_entry(level, x), True) for x in [i-1, i, i+1]].count(True) > 0
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
