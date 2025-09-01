# Get first number from user
num1 = float(input("Enter the first number: "))

# Get second number from user
num2 = float(input("Enter the second number: "))

# Get operation from user
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculation based on operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation! Please use +, -, *, or /.")