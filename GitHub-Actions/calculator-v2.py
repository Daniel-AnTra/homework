import argparse

class Calculator:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y != 0:
            return x / y
        else:
            print("You can't divide by 0")
            return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple calculator.')
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help='The operation to perform.')
    parser.add_argument('x', type=float, help='The first number.')
    parser.add_argument('y', type=float, help='The second number.')
    args = parser.parse_args()

    calculator = Calculator()

    if args.operation == 'add':
        result = calculator.addition(args.x, args.y)
    elif args.operation == 'subtract':
        result = calculator.subtraction(args.x, args.y)
    elif args.operation == 'multiply':
        result = calculator.multiplication(args.x, args.y)
    elif args.operation == 'divide':
        result = calculator.division(args.x, args.y)

    if result is not None:
        print(f"The result is {result}")