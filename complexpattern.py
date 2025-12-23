# Movie Ticket Price Calculator

try:
    age = int(input("Enter your age: "))
    day = input("Enter the day of the week: ").strip().lower()
    time = input("Enter show time (matinee/evening): ").strip().lower()
    student = input("Are you a student? (yes/no): ").strip().lower()

    price = 12  # Base price

    # Apply complex conditions
    if age < 5:
        price = 0
        reason = "Kids under 5 get free tickets!"
    elif age >= 60:
        price *= 0.7
        reason = "Senior citizen discount (30%) applied."
    elif student == "yes":
        price *= 0.8
        reason = "Student discount (20%) applied."
    else:
        reason = "Standard pricing applied."

    # Time-based pricing
    if time == "matinee":
        price *= 0.85
        reason += " Matinee discount (15%) applied."

    # Weekend pricing adjustment
    if day in ["saturday", "sunday"]:
        price *= 1.10
        reason += " Weekend surcharge (10%) applied."

    print("\n🎟️ Final Ticket Details 🎟️")
    print(f"Age: {age}")
    print(f"Day: {day.title()}")
    print(f"Show Time: {time.title()}")
    print(f"Final Ticket Price: ${price:.2f}")
    print(f"Note: {reason}")

except ValueError:
    print("Please enter a valid age (number only).")
except Exception as e:
    print(f"Unexpected error: {e}")
