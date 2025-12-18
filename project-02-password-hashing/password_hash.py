# password_hash.py 
import hashlib

print("Password Hashing Demo\n")

password = input("Enter a password to hast: ")

# SHA-256 Hash erzeugen
hashed = hashlib.sha256(password.encode()).hexdigest()

print(f"Hashed password: {hashed}")