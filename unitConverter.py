# Simple Unit Converter: Kilometers <-> Miles

def convert_units():
    try:
        print("Unit Converter")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        choice = input("Choose conversion (1 or 2): ")

        if choice not in ["1", "2"]:
            raise ValueError("Invalid choice. Please enter 1 or 2.")

        value = float(input("Enter the value to convert: "))

        if choice == "1":
            result = value * 0.621371
            print(f"{value} kilometers = {result:.2f} miles")
        else:
            result = value / 0.621371
            print(f"{value} miles = {result:.2f} kilometers")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")

convert_units()
