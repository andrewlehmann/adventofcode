def main(): 
    input_data = open("src/2021/Day9/input.txt")
    lines = input_data.readlines()
    height_data = [[int(char) for char in line.rstrip('\n')] for line in lines]

    print(calc_risk_value(height_data))

def calc_risk_value(height_data):
  risk_value = 0

  for i in range(0, len(height_data)):
    for j in range(0, len(height_data[0])):
      if (check_if_low_point(i, j, height_data)):
        risk_value = risk_value + height_data[i][j] + 1

  return risk_value

def check_if_low_point(x, y, height_data): 
  value = height_data[x][y]

  if ((x < len(height_data) - 1) and height_data[x+1][y] <= value):
    return False
  if (x > 0 and height_data[x-1][y] <= value):
    return False
  if ((y < len(height_data[x]) - 1) and height_data[x][y+1] <= value):
    return False
  if (y > 0 and height_data[x][y-1] <= value):
    return False
  return True

if __name__ == "__main__":
    main()
