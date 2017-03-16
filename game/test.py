import copy

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "{}".format(self.x)

x1 = A(1)
x2 = A(2)
a = {1:x1, 2: x2}
b = copy.deepcopy(a)
print(b)
a[1].x = 99
print(a)
print(b, b)
a.clear()
a.update(b)
print(a)