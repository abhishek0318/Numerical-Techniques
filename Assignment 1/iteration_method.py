"""
Abhishek Sharma
16123002
Mathematics and Computing
Department of Mathematical Sciences
"""

import math

class IterationMethod:
    def __init__(self, phi, epsilon=1e-6):
        self.phi = phi
        self.epsilon = epsilon

    def find(self, starting_value):
        """Finds root starting with `starting_value`.
        
        Args:
            starting_value: starting_value
        """

        old_value = starting_value + 2 * self.epsilon
        new_value = starting_value
        while abs(new_value - old_value) > self.epsilon:
            # print(old_value, new_value)
            old_value = new_value
            new_value = self.phi(new_value)

        return new_value


if __name__ == "__main__":
    solver = IterationMethod(lambda x: 1 / ((x + 1) ** (1 / 2)))
    print(solver.find(0.5))

    # solver = IterationMethod(lambda x: (math.cos(x) + 3) / 2)
    # print(solver.find(0))