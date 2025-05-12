def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Error"
    else: 
        return x / y
    
def multiply (x, y):
    return x * y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")

    choice = input("Enter choice (1,2,3,4):")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

    if choice == '1':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))

    if choice == '2':
        print("{} - {} = {}".format(num1, num2, subtract(num1, num2)))

    if choice == '3':
        print("{} / {} = {}".format(num1, num2, divide(num1, num2)))

    if choice == '4':
        print("{} * {} = {}".format(num1, num2, multiply(num1, num2)))

    else:
        print("Invalid input, please select from the option choices")

calculator()
