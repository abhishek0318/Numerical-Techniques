import random
from tqdm import trange

class BisectionMethod:
    def __init__(self, function, epsilon=1e-6):
        self.function = function
        self.epsilon = epsilon

    def find(self, ends):
        """Finds root within ends.
        
        Args:
            ends: a tuple containing the ends of interval where to check for roots.
        """

        if self.function(ends[0]) * self.function(ends[1]) > 0:
            raise ValueError('Sign of function at both the end points must be opposite.')
        
        a = min(ends)
        b = max(ends)

        while (b - a > self.epsilon):
            mid = (a + b) / 2
            if self.function(mid) * self.function(a) > 0:
                a = mid
            else:
                b = mid
        
        return (a + b) / 2

    def find_all(self, iterations=100, Range=10):
        """Finds all root of an equation.
        
        Args:
            iterations: number of iterations to initialise the ends
            Range: range of values used to initialise the ends
        """
        roots = []
        for _ in trange(iterations):
            a = 0
            b = 0
            while self.function(a) * self.function(b) >= 0:
                a = (random.random() - 0.5) * Range
                b = (random.random() - 0.5) * Range
            a, b = min(a, b), max(a, b)

            root = self.find(ends=(a, b))

            exists = False
            for r in roots:
                if abs(r - root) < self.epsilon:
                    exists = True
            if not exists:
                roots.append(root)
        
        return roots

if __name__ == "__main__":
    solver = BisectionMethod(lambda x: x ** 5 - 25 * x ** 4 + 184 * x ** 3 - 640 * x ** 2 - 2223 * x - 4905, 1e-10)
    # solver = BisectionMethod(lambda x: x ** 3 - 6 * (x ** 2) + 11 * x - 6, 1e-8)
    print (solver.find((0, 1000)))
    # print(solver.find_all(iterations=100))
