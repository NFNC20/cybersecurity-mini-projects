# Project 02 - Password Hashing Demo

## Goal
Demonstrate hashing of passwords to avoid storing them in plain text. 
This helps improve security and protect user data

## Background
Storing passwords as hashes ensures that even if a database is compromised, the actual passwords are not exposed. 
Hashing is a one-way function that converts any input into a fixed-length string.

## Approach 
- User inouts a password
- SHA-256 hash is generated using Python's 'hashlib' module
- The hashed password is displayed

### Sample Output 
Enter a password to hash: mypassword123
Hashed password: 6e659deaa85842cdabb5c6305fcc40033ba43772ec00d45c2a3c921741a5e377

### Key Learnings
- Hashing is a one-way function
- SHA-256 provides a consistent, secure hash for passwords
- Never store passwords in plain text
