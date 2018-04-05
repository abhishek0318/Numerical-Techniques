class NewtonBackwardInterpolator:
    def __init__(self, function_values):
        """Initialises the object and computes the del_yns.
        
        Args:
            function_values: list of tuples containing a node and value of function at the node
        """

        self.function_values = function_values
        self.function_values.sort()
        if not self.check_equidistant_nodes:
            raise ValueError('Newton backward interpolation works only with equidistant nodes.')
        self.h = self.function_values[1][0] - self.function_values[0][0]
        self.del_yns = [column[-1] for column in self.calculate_backward_difference_table(self.function_values)]

    @staticmethod
    def check_equidistant_nodes(function_values):
        """Returns true if nodes in `function_values` are equidistant.    

        Args:
            function_values: list of tuples containing a node and value of function at the node"""
        function_values.sort()
        h = function_values[1][0] - function_values[0][0]
        for i in range(2, len(function_values)):
            if h != (function_values[i][0] - function_values[i - 1][0]):
                return False
        return True

    @staticmethod
    def calculate_backward_difference_table(function_values):
        """Returns the forward difference table.    

        Args:
            function_values: list of tuples containing a node and value of function at the node"""
        table = [[0 for i in range(len(function_values))] for j in range(len(function_values))]        
        table[0] = [y for x, y in function_values]
        for del_superscript in range(1, len(function_values)):
            for y_subscript in range(del_superscript, len(function_values)):
                table[del_superscript][y_subscript] = table[del_superscript - 1][y_subscript] - table[del_superscript - 1][y_subscript - 1]
        return table
        
    def interpolate(self, x):
        """Interpolates the function at x"""

        p = (x - self.function_values[-1][0]) / self.h
        y = 0
        coefficient = 1
        for term_num, del_yn in enumerate(self.del_yns):
            y += coefficient * del_yn
            coefficient *= (p + term_num) / (term_num + 1)
        return y


if __name__ == "__main__":
    interpolator = NewtonBackwardInterpolator([(1, 0), (2, 7.01), (3, 25.91), (4, 63.014), (5, 123.909)])
    print(interpolator.interpolate(1.5))