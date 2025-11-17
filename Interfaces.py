def get_text(prompt):
    """Get non-empty text input from user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠ Input cannot be empty. Please try again.")

def get_number(prompt):
    """Get a valid number input."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("⚠ Please enter a valid number (digits only).")

def get_option(prompt, options):
    """Get a valid option from a list."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"⚠ Invalid option. Choose from: {', '.join(options)}")
