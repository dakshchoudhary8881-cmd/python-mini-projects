password = input("Enter your password: ")

length = len(password)

has_digit = False
has_letter = False

for ch in password:
    if ch >= '0' and ch <= '9':
        has_digit = True
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        has_letter = True

if length < 6:
    print("Password Strength: Weak")
    print("Reason: Password is too short")

elif length >= 6 and has_letter and not has_digit:
    print("Password Strength: Medium")
    print("Reason: Add numbers to make it stronger")
    
elif length >= 6 and has_digit and not has_letter:
    print("Password Strength: Medium")
    print("Reason: Add letters to make it stronger")

elif length >= 8 and has_letter and has_digit:
    print("Password Strength: Strong")
    print("Good job! Your password is strong")

else:
    print("Password Strength: Weak")
