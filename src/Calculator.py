class Calculator:
    def add(self, a, b):
        # Check if inputs are valid numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return a + b

    def subtract(self, a, b):
        # Check if inputs are valid numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return a - b

    def multiply(self, a, b):
        # Check if inputs are valid numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return a * b

    def divide(self, a, b):
        # Check if inputs are valid numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        # Check for division by zero
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b