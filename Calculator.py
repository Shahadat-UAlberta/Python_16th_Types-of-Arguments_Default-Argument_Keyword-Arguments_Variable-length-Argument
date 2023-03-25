# Add
# Sub
# Mul
# Div

"""
>> [S-O]-[L-I-D]
-------------------------------------------------------------
1. Single Responsibility Principle
2. Open Closed Principle [Open for Extension but closed for modification]
"""
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def getUserInput(parameter):
    num = float(input(parameter))
    return num


while True:

    print("Please select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = getUserInput("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        break

    num1 = getUserInput("Enter first number: ")
    num2 = getUserInput("Enter second number: ")

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Result")