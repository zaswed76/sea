
from random import randint, choice
from itertools import product, permutations


mx = [-1, 1, -1, 0, 1, -1, 0, 1]
my = [0, 0, -1, -1, -1, 1, 1, 1]
print(list(permutations((0, 1, -1), 2)))