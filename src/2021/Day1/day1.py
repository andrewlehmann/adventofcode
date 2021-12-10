def main(): 
    input_data = open("src/2021/Day1/input.txt")
    lines = input_data.readlines()
    depths = [int(line.rstrip('\n')) for line in lines]

    increasesCount = 0

    last_sum = depths[0] + depths[1] + depths[2]

    for i in range(2, len(depths)):
      cur_sum = depths[i] + depths[i-1] + depths[i-2]
      if cur_sum > last_sum:
        increasesCount += 1
      
      last_sum = cur_sum

    print(increasesCount)


if __name__ == "__main__":
    main()
