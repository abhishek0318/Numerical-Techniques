import math

class NewtonRaphsonMethod:
    def __init__(self, f, f_dash, epsilon=1e-6):
        self.f = f
        self.f_dash = f_dash
        self.epsilon = epsilon

    def find(self, starting_value):
        """Finds root starting with `starting_value`.
        
        Args:
            starting_value: starting value
        """

        old_value = starting_value + 2 * self.epsilon
        new_value = starting_value
        while abs(new_value - old_value) > self.epsilon:
            old_value = new_value
            new_value = new_value - self.f(new_value) / self.f_dash(new_value)

        return new_value

    @staticmethod
    def sign(a, b):
        """Returns true if sign of a and b is same."""
        return a * b > 0

if __name__ == "__main__":
    solver = NewtonRaphsonMethod(lambda x: x * math.sin(x) + math.cos(x), lambda x: x * math.cos(x))
    print(solver.find(starting_value=3))

