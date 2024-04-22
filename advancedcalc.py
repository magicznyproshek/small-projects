import math

class AdvancedCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

    def exponentiate(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            raise ValueError("Square root of a negative number is undefined!")
        return math.sqrt(x)

    def logarithm(self, x, base=math.e):
        if x <= 0:
            raise ValueError("Logarithm of non-positive number is undefined!")
        return math.log(x, base)


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_operation_choice():
    while True:
        print("\nChoose the operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Natural Logarithm")
        print("8. Logarithm base 2")
        choice = input("Enter the number corresponding to the operation: ")
        if choice.isdigit() and 1 <= int(choice) <= 8:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


def main():
    calculator = AdvancedCalculator()

    while True:
        try:
            operation_choice = get_operation_choice()

            if operation_choice in [1, 2, 3, 4, 5]:
                x = get_float_input("Enter the first number: ")
                y = get_float_input("Enter the second number: ")
            elif operation_choice == 6:
                x = get_float_input("Enter the number: ")
            elif operation_choice in [7, 8]:
                x = get_float_input("Enter the number: ")

            if operation_choice == 1:
                result = calculator.add(x, y)
            elif operation_choice == 2:
                result = calculator.subtract(x, y)
            elif operation_choice == 3:
                result = calculator.multiply(x, y)
            elif operation_choice == 4:
                result = calculator.divide(x, y)
            elif operation_choice == 5:
                result = calculator.exponentiate(x, y)
            elif operation_choice == 6:
                result = calculator.square_root(x)
            elif operation_choice == 7:
                result = calculator.logarithm(x)
            elif operation_choice == 8:
                result = calculator.logarithm(x, 2)

            print("Result:", result)

        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("An error occurred:", e)

        choice = input("\nDo you want to perform another operation? (yes/no): ").lower()
        if choice != 'yes':
            break


if __name__ == "__main__":
    main()
