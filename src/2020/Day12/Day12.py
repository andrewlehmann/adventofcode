import math


def rotate(x, y, direction_to_rotate, degrees_to_rotate):

    if x == 0 and y == 0:
      return (0, 0)
    elif y == 0:
      curr_direction = round(math.atan(math.radians(x / y)) / 90) * 90
    else: 
      curr_direction = 90 if y > 0 else 270

    if direction_to_rotate == 'L':
        new_direction = (curr_direction + degrees_to_rotate) % 360
    elif direction_to_rotate == 'R':
        new_direction = (curr_direction - degrees_to_rotate) % 360

    if new_direction == 90:
        return (-y, x)
    elif new_direction == 180:
        return (-x, -y)
    elif new_direction == 270:
        return (y, -x)
    elif new_direction == 0:
        return (x, y)

input_data = open("src/2020/Day12/input.txt")
lines = input_data.readlines()
actions = [line.rstrip('\n') for line in lines]

ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1

for action in actions:
    action_type = action[0]
    value = int(action[1:])

    if action_type == 'L':
        waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, action_type, value)
    elif action_type == 'R':
        waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, action_type, value)
    elif action_type == "N":
        waypoint_y += value
    elif action_type == "S":
        waypoint_y -= value
    elif action_type == "E":
        waypoint_x += value
    elif action_type == "W":
        waypoint_x -= value
    elif action_type == 'F':
        ship_x = ship_x + value * waypoint_x
        ship_y = ship_y + value * waypoint_y


print(ship_x, ship_y)
print(abs(ship_x) + abs(ship_y))
