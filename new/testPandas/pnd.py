



class Ship:


    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.z = 4

    @classmethod
    def set_get(cls):
        cls.z = 5


s1 = Ship(1, 2)
s2 = Ship(3, 4)
print(s1.z)
s2.set_get()
print(s1.z)
