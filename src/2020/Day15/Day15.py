
def get_new_number(number, turn, number_cache):
  if number not in number_cache.keys():
    return 0
  elif type(number_cache[number]) is list:
    return number_cache[number][-1] - number_cache[number][-2]
  else:
    return turn - number_cache[number]

def update_cache(number, turn, number_cache):  
  if number not in number_cache.keys():
    number_cache[number] = turn - 1
    return number_cache
  elif type(number_cache[number]) is list:
    number_cache[number] = [number_cache[number][-1], turn - 1]
    return number_cache
  else:
    number_cache[number] = [number_cache[number], turn - 1]
    return number_cache


input = [1,0,16,5,17,4]
turn = len(input) + 2
cache = {x : ind + 1 for ind, x in enumerate(input)}
number = 0
last_number = 0

while (turn <= 30000000):
  cache = update_cache(number, turn, cache)
  if number in cache.keys() and type(cache[number]) is not list:
    number = 0
  else:
    number = get_new_number(number, turn, cache)
  turn += 1


print(number)