# Simple Calculator in Python

# Ask for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"

print("The sum of", num1, "and", num2, "is", sum_result)
print("The difference between", num1, "and", num2, "is", diff_result)
print("The product of", num1, "and", num2, "is", prod_result)
print("The division of", num1, "by", num2, "is", div_result)