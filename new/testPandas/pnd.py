

class Cell:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "{}".format(self.x)

a = [Cell(x) for x in range(5)]
c = Cell(1)
print(c in a)
