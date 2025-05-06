print("Let's add two ODD number!")

# Ask for first number
num1 = int(input("Enter the first odd number: "))

# Ask for second number
num2 = int(input("Enter the second odd number: "))

# Check if both are odd
if num1 % 2 != 0 and num2 % 2 != 0:
    print("Great! Both numbers add odd.")
    total = num1 + num2 
    print("The sum of the two odd number is:", total)
else:
    print("Oops! One or both numbers are not odd. Try again!")