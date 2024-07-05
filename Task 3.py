import re

def assess_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 12:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1

    if strength == 0:
        return "Weak"
    elif strength < 5:
        return "Medium"
    else:
        return "Strong"


# Example usage
password = input("Enter a password: ")
print("Password strength:", assess_password_strength(password))
