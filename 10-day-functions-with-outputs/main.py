from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    print("Those're the valid operations: ")
    for key in operations.keys():
        print(key)
    more_operations = True

    num1 = float(input("What is the first number?: "))
    while more_operations:
        num2 = float(input("What is the next number?: "))
        operation = input("Pick an operation: ")
        if operations.get(operation, None) != None:
            function = operations[operation]
            result = function(num1, num2)
            print(f'The result of {num1} {operation} {num2} = {result}')
        else:
            print("You don't select a valid operation!")

        validation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.:")
        if validation != 'y':
            more_operations = False
            calculator()
        else:
            num1 = result

calculator()