"""This is a bad four operation calculator"""

success: bool = False

while success == False:
    number1: str = input("What is your first number? ")
    number1 = float(number1)

    operation: str = input("Would you like to add, subtract, multiply, or divide? ")
    operation = operation.lower()
    
    number2: str = input("What is your second number? ")
    number2 = float(number2)

    if operation == "add":
        answer = (number1 + number2)
        success = True
    elif operation == "subtract":
        answer = (number1 - number2)
        success = True
    elif operation == "multiply":
        answer = (number1 * number2)
        success = True
    elif operation == "divide":
        answer = (number1 / number2)
        success = True
    else:
        print("Something went wrong! Let's try again.")

    print(answer)

    repeat: str = input("Would you like to perform another operation? Y or N?")
    repeat = repeat.upper()

    if repeat == "Y":
        success = False
    elif repeat == "N":
        print("Have a good day!")
    else:
        print("I'll take that as a no")