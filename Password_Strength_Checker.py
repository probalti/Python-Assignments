def password_strength_checker(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1  # Bonus for extra length

    # Character type checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in symbols:
            has_symbol = True

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    # Final rating
    if score <= 2:
        return "Very Weak"
    elif score == 3:
        return "Weak"
    elif score == 4:
        return "Moderate"
    elif score == 5:
        return "Strong"
    else:
        return "Very Strong"

# Run it!
user_pass = input("Enter a password: ")
strength = password_strength_checker(user_pass)
print(f"Password Strength: {strength}")
