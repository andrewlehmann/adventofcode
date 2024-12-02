def get_similarity_score(first_list, second_list):
    first_list.sort()
    second_list.sort()
    
    occurrences = {entry: second_list.count(entry) for entry in first_list}
    score = 0

    for i in range(len(first_list)): # assuming lists are same length
        score += first_list[i] * occurrences[first_list[i]]
    return score

def main():
    first_list = []
    second_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            columns = line.split()
            first_list.append(int(columns[0]))
            second_list.append(int(columns[1]))

    print(get_similarity_score(first_list, second_list))


if __name__ == "__main__":
    main()
