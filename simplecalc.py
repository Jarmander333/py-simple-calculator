def add(num1, num2): # define addition as "add"
    return num1 + num2 # outputs the sum of num1 & num2

def subtract(num1, num2): # define subtraction as "subtract"
    return num1 - num2 # outputs the difference of num1 & num2

def multiply(num1, num2): # define multiplication as "multiply"
    return num1 * num2 # outputs the product of num1 & num2

def divide(num1, num2): # define division as "divide"
    return num1 / num2 # outputs the quotient of num1 & num2
    

# Prints the text below on the screen
print("Select operation.")
print("Addition is +")
print("Subtraction is -")
print("Multiplication is *")
print("Division is /")

while True: # infinite loop
    choice = input("Enter choice(+, -, *, /): ") # The user types the operator they want from the choices printed on-screen

    if choice in ('+', '-', '*', '/'): # checks IF the choice is one of the 4 operators THEN move on 
        num1 = float(input("Enter first number: ")) # User inputs the first number as a floating point which is decimal compatible
        num2 = float(input("Enter second number: ")) # User inputs the second number as a floating point which is decimal compatible

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2)) # prints first number + second number = answer (example: 1 + 4 = 5.0)

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2)) # prints first number - second number = answer (example: 1 - 4 = 5.0)

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2)) # prints first number * second number = answer (example: 1 * 4 = 5.0)
            
        elif choice == '/':
            print(num1 + "/" + num2 + "=" + divide(num1, num2)) # prints first number / second number = answer (example: 1 / 4 = 5.0)
        break
    else:
        print("Invalid Input") # if the number(s) aren't a number, and/or the operator isn't one of the choices, then an error will be displayed\
input("Press the Enter key to continue") # when the user hits the return/enter key the program shuts off