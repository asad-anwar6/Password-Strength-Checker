password = input("Enter your password: ")

password_length = len(password)

print("Password Length:", password_length)

if password_length >= 8:
    print("Password length is good.")
else:
    print("Password is too short.")

# Uppercase Check
has_uppercase = False

for character in password:
    if character.isupper():
        has_uppercase = True

print("Contains Uppercase:", has_uppercase)

# Number Check
has_digit = False

for character in password:
    if character.isdigit():
        has_digit = True

print("Contains Number:", has_digit)

has_lowercase = False

for character in password:
    if character.islower():
        has_lowercase = True

print("Contains Lowercase:", has_lowercase)

has_special = False
for character in password:
    if character in "@#$%&!*?":
        has_special = True

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

   