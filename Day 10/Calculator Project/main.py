import art

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
    "/": divide,
}

print(art.logo)
def calculator():
    game_state = True
    result = 0
    first = int(input("What's the first number?:    "))

    while game_state == True:
        operation = input("Pick an operation:    ")
        second = int(input("What's the next number?:    "))
        result = operations[operation](n1= first, n2= second)
        print(f"{first} {operation} {second} = {result}")
        game_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:    ")
        if game_continue == "n":
            game_state = False
            calculator()
        elif game_continue =='y':
            first = result


calculator()

#TODO: Write out the other 3 functions - subtract, multiply and divide

#TODO: Add theese 4 functions into a dictionary as the values.
#Keys = "+", "-", "*", "/"

#TODO: Use the dictionary operations to perform the calculations. Multiply 4 by 8 using the dictionary.