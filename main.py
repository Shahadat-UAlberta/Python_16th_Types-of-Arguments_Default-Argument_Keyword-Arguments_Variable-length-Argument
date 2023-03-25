##  Types of Arguments


### 01. Default arguments

### 02. Keyword arguments

### 03. Variable-length arguments  [ *args / **kwargs ]

"""
# Type - 01
def add(num1=0, num2=0):
    return num1 + num2


print(add(10, 20))
print(add(10))
print(add())


# Type - 02
def getStudentName(firstName, lastName):
    print(firstName, lastName)


getStudentName("A. ", "Rahim")
getStudentName(lastName="A. ", firstName="Rahim")

# Type - 03
def add(*nums): # arguments - value arguments
    print(type(nums))  # <class 'tuple'> | Ordered and Unchangeable |

    sum = 0

    for arg in nums:
        sum += arg

    return sum


print(add())
print(add(10))
print(add(10, 20, 10))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))

# keywords argument

def getKeyValue(**kwargs):
    print(type(kwargs)) # <class 'dict'>

    for key, value in kwargs.items(): # Return key-value paris
        print(key, value)

getKeyValue(firstLanguage = "Python", secondLanguage = "Java")
print("---------------")
getKeyValue(firstLanguage = "Python", secondLanguage = "Java", thirdLanguage= "C++")
print("---------------")
getKeyValue(firstLanguage = "Python")
"""
