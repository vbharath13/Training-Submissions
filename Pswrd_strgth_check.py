# Simple Password Strength Checker

import re

def check_password_strength(password):
    try:
        if len(password) < 8:
            return "Weak: Password too short. Use at least 8 characters."
        if not re.search("[a-z]", password):
            return "Weak: Add lowercase letters."
        if not re.search("[A-Z]", password):
            return "Weak: Add uppercase letters."
        if not re.search("[0-9]", password):
            return "Weak: Add numbers."
        if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            return "Weak: Add special characters."

        return "Strong: Great password!"
    except Exception as e:
        return f"Error occurred: {e}"

# Main function
try:
    pwd = input("Enter your password to check strength: ")
    result = check_password_strength(pwd)
    print(result)
except Exception as e:
    print(f"Unexpected error: {e}")
