# practice.py

def greet(name):
    """Return a greeting aaa message."""
    return f"Hello, {name}! Welcome to GitHub practice."


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    name = input("My name:is Hima ")
    print(greet(name))

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()
