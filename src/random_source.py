import random


class FakeRandom(object):
    def __init__(self, results=range(1000000)):
        self.results = iter(results)
    def randint(self, a, b):
        return next(self.results)
    

class SystemRandom(object):
    def randint(self, a, b):
        return random.randint(a, b)
    
if __name__ == "__main__":
    t = FakeRandom()
    print t.randint(0, 100)
    print t.randint(0, 100)
    