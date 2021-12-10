from statistics import mode

def main(): 
    input_data = open("src/2021/Day3/input.txt")
    lines = input_data.readlines()
    positions = [[char for char in line.rstrip('\n')] for line in lines]

    columns = [list(x) for x in zip(*positions)]

    gamma = ''
    epsilon = ''

    for column in columns:
      next_gamma, next_epsilon = get_values(column)
      gamma += next_gamma
      epsilon += next_epsilon

    power_consumption = int(gamma, 2) * int(epsilon, 2)
    
    print(power_consumption)

def get_values(position): 
  most_common = mode(position)
  print(most_common)
  return most_common, '0' if most_common == '1' else '1'

if __name__ == "__main__":
    main()
