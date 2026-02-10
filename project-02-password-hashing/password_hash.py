# password_hash.py 
import hashlib

print("Password Hashing Demo\n")

password = input("Gib ein Passwort ein, das gehasht werden soll: ")

# SHA-256 Hash erzeugen
hashed = hashlib.sha256(password.encode()).hexdigest()

print(f"Gehashtes Passwort: {hashed}")
