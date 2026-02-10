# password_check.py

# Liste der Beispielpasswörter
passwords = ["12345", "Pa55word", "My$ecur3P@ss2025!"]

print("Password Strength Check\n")

for pwd in passwords:
    length = len(pwd)
    if length < 6:
        strength = "Sehr schwach"
    elif length < 12:
        strength = "Mittel"
    else:
        strength = "Stark"
    print(f"Password: {pwd} | Length: {length} | Estimated Strength: {strength}")
