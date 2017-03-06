
from collections import MutableSet

import random
pc_sea = set(range(100))
allow = pc_sea.copy()
currently_unavailable = {}
not_available= {}
fleet = list()

class Sea(set):
    def __init__(self):
        super().__init__()



def get_bow(size, vector):
    while True:
        b = random.choice(list(allow))
        if check_bow(allow, b, size, vector):
            return b
        else:
            allow = allow - b

def check_bow(allow, bow, size, vector):
    for s in range(bow, bow + size):
        if not s in allow:
            return False
    else:
        return True




def get_ship(bow, size, vector):
    if vector == "-":
        assert ((int(str(bow)[1]) + size-1) < 10)
        return set(x for x in range(bow, bow + size))
    elif vector == "1":
        assert (bow + (size-1) * 10) < 100
        return set(x for x in range(bow, (bow + size * 10), 10))

def get_fleet(names):
    f = []
    for n in names:
        f.append(get_ship("bow", n, "vector"))





if __name__ == '__main__':

    get_bow(allow)



