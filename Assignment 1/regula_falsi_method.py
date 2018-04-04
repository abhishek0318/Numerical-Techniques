import math

class RegulaFalsiMethod:
    def __init__(self, f, epsilon=1e-6):
        self.f = f
        self.epsilon = epsilon

    def find(self, a, b):
        """Finds root in interval `a` to `b`."""
        
        while abs(self.f(a)) > self.epsilon and abs(self.f(b)) > self.epsilon:
            c = (a * self.f(b) - b * self.f(a)) / (self.f(b) - self.f(a))
            if self.sign(self.f(a), self.f(c)):
                a = c
            elif self.sign(self.f(b), self.f(c)):
                b = c
        
        if abs(self.f(a)) < self.epsilon:
            return a
        else:
            return b 

    @staticmethod
    def sign(a, b):
        """Returns true if sign of a and b is same"""
        return a * b > 0

if __name__ == "__main__":
    solver = RegulaFalsiMethod(lambda x: x * math.sin(x) + math.cos(x))
    print(solver.find(0, 3 * math.pi / 2))


# a b
# f(a) f(b)
# (y - f(a)) / (x - a) = (f(b) - f(a)) / (b - a)
# Put y = 0,
# x = (af(a) - bf(a)) / (f(b) - f(a)) + a
# x = (af(b) - bf(a)) / (f(b) - f(a)

