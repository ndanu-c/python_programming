#defining variables to store the user input
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operator = input("Enter operator (+, -, *, /, %)")

#Doing operations based on user input
if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

#Displaying the results of the operations to the console
print(f"The result of {num1} {operator} {num2} is {result}")
print("Just made the first simple calculator program!!")
