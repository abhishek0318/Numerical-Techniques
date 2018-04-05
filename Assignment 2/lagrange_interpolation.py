class LagrangeInterpolator:
    def __init__(self, function_values):
        """Initialises the object.
        
        Args:
            function_values: list of tuples containing a node and value of function at the node
        """

        self.function_values = function_values
        
    def interpolate(self, x):
        """Interpolates the function at x"""

        y = 0
        for term_num in range(len(self.function_values)):
            coefficient_num = 1
            for i in range(len(self.function_values)):
                if i == term_num:
                    continue
                coefficient_num *= x - self.function_values[i][0]

            coefficient_den = 1
            for i in range(len(self.function_values)):
                if i == term_num:
                    continue
                coefficient_den *= self.function_values[term_num][0] - self.function_values[i][0]

            y += (coefficient_num / coefficient_den) *self.function_values[term_num][1]

        return y

if __name__ == "__main__":
    interpolator = LagrangeInterpolator([(1, 0), (2, 7.01), (4, 63.014), (5, 123.909), (8,541)])
    print(interpolator.interpolate(1.5))
