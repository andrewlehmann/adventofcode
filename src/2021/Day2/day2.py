def main(): 
    input_data = open("src/2021/Day2/input.txt")
    lines = input_data.readlines()
    commands = [ line.rstrip('\n') for line in lines]
    print(commands)

    horizontal_position = 0
    depth = 0

    for command in commands:
      direction, amt = command.split(' ', 1)

      if (direction == 'forward'):
        horizontal_position += int(amt)
      
      if (direction == 'down'):
        depth += int(amt)
      
      if (direction == 'up'):
        depth -= int(amt)

    print(depth * horizontal_position)

if __name__ == "__main__":
    main()
