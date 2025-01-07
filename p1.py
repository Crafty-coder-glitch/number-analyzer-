# Function to find the largest and smallest of three numbers
def maxim(a, b, c):
    # Find the largest number
    largest = max(a, b, c)
    # Find the smallest number
    smallest = min(a, b, c)
    return largest, smallest

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Get the largest and smallest numbers
largest, smallest = maxim(num1, num2, num3)

# Display the results
print("The largest number is:", largest)
print("The smallest number is:", smallest)

