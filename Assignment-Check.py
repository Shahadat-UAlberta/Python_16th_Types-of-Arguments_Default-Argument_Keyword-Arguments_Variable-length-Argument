def Addition(num1, num2) :
    return num1 + num2

def Subtract(num1, num2):
    return num1 - num2

def Multiply(num1, num2):
    return num1 * num2

def Divide(num1, num2):
    return num1 / num2

def Percent(num1, num2):
    return num1 % num2

def floor(num1, num2):
    return num1 // num2

def exponent(num1, num2):
    return num1 ** num2

a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))

result = Addition(a, b), Subtract(a, b), Multiply(a, b), Divide(a,b), Percent(a,b),\
floor(a,b),exponent(a,b)

print(result)
