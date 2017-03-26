

class Shooter:
    def __init__(self):
        self.data = [(y, x) for y in range(10) for x in range(10)]

    def shot(self):
        return self.data.pop()