import random
class Snack(object):
    def __init__(self):
        self.x = random.randint(15,700)
        self.y = random.randint(15,500)
        self.dct = 0
    def step(self):
        if self.dct == 0:
            self.x += 1
        elif self.dct == 1:
            self.y += 1
        elif self.dct == 2:
            self.x -= 1
        elif self.dct == 3:
            self.y -= 1