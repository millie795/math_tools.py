# Import the custom math module
import math_tools

# Display available operations
print("===== BASIC MATH OPERATIONS =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get user's choice
choice = input("Choose an operation (1-4): ")

# Perform selected operation
if choice == "1":
    result = math_tools.addition(num1, num2)
    print("Result of Addition:", result)

elif choice == "2":
    result = math_tools.subtraction(num1, num2)
    print("Result of Subtraction:", result)

elif choice == "3":
    result = math_tools.multiplication(num1, num2)
    print("Result of Multiplication:", result)

elif choice == "4":
    result = math_tools.division(num1, num2)
    print("Result of Division:", result)

else:
    print("Invalid choice! Please select between 1 and 4.")