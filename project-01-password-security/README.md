# Project 01 – Password Security Basics

## Goal
Understand basic principles of password security and common weaknesses.

## Background
Passwords are still one of the most common authentication methods. Weak or reused passwords are a major security risk.

## Approach
- Compare weak and strong password characteristics
- Analyze why password length matters
- Understand common attack methods (e.g. brute force) on a conceptual level

## Key Learnings
- Short passwords are highly vulnerable
- Length is often more important than complexity
- Reusing passwords increases overall risk

## Password Comparison
| Password Example | Length | Complexity | Estimated Strength |
|------------------|--------|------------|--------------------|
| 12345            | 5      | Low        | Very Weak          |
| Pa55word         | 8      | Medium     | Medium             |
| My$ecur3P@ss2025!| 17     | High       | Strong             |

### Observation
Short passwords like '12345' are extremely weak and vulnerable to brute-force attacks.
Longer, complex passwords are much stronger and harder to guess.
This exercise highlights the importance of password length and complexity.

## Python Exercise

A simple Python script `password_check.py` demonstrates password strength based on password length.

The script iterates over a list of example passwords, calculates their length, and classifies their strength as Very Weak, Medium, or Strong.

This allows us to see how shorter passwords are weaker than longer, more complex ones.


## Next Steps

- Explore password hashing algorithms
- Learn about two-factor authentication
- Investigate password managers

### Sample Output

Password: 12345 | Length: 5 | Estimated Strength: Very Weak
Password: Pa55word | Length: 8 | Estimated Strength: Medium
Password: My$ecur3P@ss2025! | Length: 17 | Estimated Strength: Strong
