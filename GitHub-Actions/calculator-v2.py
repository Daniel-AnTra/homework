import argparse
import random

class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="operation to perform")
    parser.add_argument("x", type=float, help="first operand")
    parser.add_argument("y", type=float, help="second operand")
    
    args = parser.parse_args()
    
    calculator = Calculator()
    
    # Generate random values for operation and operands
    operations = ["add", "subtract", "multiply", "divide"]
    op = random.choice(operations)
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    
    # Perform the selected operation
    if op == "add":
        result = calculator.add(x, y)
    elif op == "subtract":
        result = calculator.subtract(x, y)
    elif op == "multiply":
        result = calculator.multiply(x, y)
    else:
        try:
            result = calculator.divide(x, y)
        except ValueError as e:
            print(e)
            exit(1)
    
    # Print the result
    print(f"{op}({x}, {y}) = {result}")
