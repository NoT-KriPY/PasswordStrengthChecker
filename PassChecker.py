import re
import string

while True:
    print("Welcome to the Password Strength Checker!")
    password = input("Enter a password to check: ")
    length = len(password)
    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        else:
            has_symbol = True 


    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1

    print("\n--- Results ---")
    if score == 5:
        print("Strong password! Excellent.")
        break
    elif score >= 3:
        print("Medium password. It's okay, but could be better.")
    else:
        print("Weak password! Too easy to guess.")

    if not has_upper:
        print("- Missing an uppercase letter.")
    if not has_lower:
        print("- Missing a lowercase letter.")
    if not has_number:
        print("- Missing a number.")
    if not has_symbol:
        print("- Missing a symbol (like !, @, #, $).")
    if length < 8:
        print("- Too short. Make it at least 8 characters.")