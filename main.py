password = input("Enter your password: ")

password_length = len(password)

print("Password Length:", password_length)

if password_length >= 8:
    print("Password length is good.")
else:
    print("Password is too short.")

# Character Checks (Optimized)

has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for character in password:
    if character.isupper():
        has_uppercase = True

    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_digit = True

    if character in "@#$%&!*?":
        has_special = True

print("Contains Uppercase:", has_uppercase)
print("Contains Lowercase:", has_lowercase)
print("Contains Number:", has_digit)
print("Contains Special Character:", has_special)
score = 0

if password_length >= 8:
    score += 1

if has_uppercase:
    score += 1


if has_lowercase:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("Password Score:", score)

if score <= 2:
    print("Weak Password")

elif score <= 4:
    print("Medium Password")

else:
    print("Strong Password")


print("\nPassword check completed successfully.")

# Suggestions

if score == 5:
    print("\nExcellent! Your password meets all basic security requirements.")
else:
    print("\nSuggestions:")

    if password_length < 8:
        print("- Password should be at least 8 characters long.")

    if not has_uppercase:
        print("- Add at least one uppercase letter.")

    if not has_lowercase:
        print("- Add at least one lowercase letter.")

    if not has_digit:
        print("- Add at least one number.")

    if not has_special:
        print("- Add at least one special character (@#$%&!*?).")