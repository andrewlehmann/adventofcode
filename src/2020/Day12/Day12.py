import math  

input_data = open("src/2020/Day12/input.txt")
lines = input_data.readlines()
actions = [line.rstrip('\n') for line in lines]
print(actions)

location_x = 0
location_y = 0

direction_facing = 0

for action in actions:
    action_type = action[0]
    value = int(action[1:])

    if action_type == 'L':
        direction_facing = (direction_facing + value) % 360

    elif action_type == 'R':
        direction_facing = (direction_facing - value) % 360

    elif action_type == "N":
        location_y += value

    elif action_type == "S":
        location_y -= value

    elif action_type == "E":
        location_x += value

    elif action_type == "W":
        location_x -= value

    elif action_type == 'F':
      location_x = location_x + value * math.cos(math.radians(direction_facing))
      location_y = location_y + value * math.sin(math.radians(direction_facing))


print(location_x, location_y)
print(abs(location_x) + abs(location_y))