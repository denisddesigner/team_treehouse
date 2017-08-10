import random

cells = range(0, 100)

def get_locations(cells, number):
    return random.sample(cells, number)

print(get_locations(cells, 3))