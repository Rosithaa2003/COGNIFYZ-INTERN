def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def modulus(x, y):
    if y == 0:
        return "Cannot perform modulus with zero"
    return x % y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %): ")


if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
elif operator == '%':
    result = modulus(num1, num2)
else:
    result = "Invalid operator"

print(f"Result: {result}")
