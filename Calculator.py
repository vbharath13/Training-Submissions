# Recursive Factorial Calculator

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Main program
try:
    num = int(input("Enter a number to calculate its factorial: "))

    if num < 0:
        print("❌ Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"✅ The factorial of {num} is {result}")

except ValueError:
    print("⚠️ Please enter a valid integer.")
