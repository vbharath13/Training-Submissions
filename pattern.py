# Pattern Printer: Right Triangle

try:
    rows = int(input("Enter number of rows: "))
    for i in range(1, rows + 1):
        print("*" * i)
except ValueError:
    print("Please enter a valid integer.")
