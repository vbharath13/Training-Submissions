# A simple age calculator without imports - requires user to input current date

def calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    """
    Calculates age manually.
    """
    age = current_year - birth_year

    # Check if the birthday has passed this year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1
        
    return age

# Get all required inputs from the user
print("Enter your birth date:")
birth_year = int(input("Year: "))
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))

print("\nEnter today's date:")
current_year = int(input("Year: "))
current_month = int(input("Month: "))
current_day = int(input("Day: "))

# Calculate and print the age
age_in_years = calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day)
print(f"\nYou are {age_in_years} years old.")