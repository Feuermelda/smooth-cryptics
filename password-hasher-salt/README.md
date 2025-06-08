# Password Hasher with Salting
This Python script securely hashes user passwords using a **a random salt** and **PBKDF2 with SHA-256**, simulating the process of secure password storage and verification.

## Features
- accepts a custom password from the user
- generates a cryptographically secure 16-byte salt using `os.random`
- hashes the password using `hashlib.pbkdf2_hmac` (SHA-256, 100 Iterations)
- let's the user re-enter the password for verification
- compares the two hashes to determine if the input matches
- prints the salt (optionally decoded in `latin-1` for visual representation)

## Usage
1. Enter a password
2. Enter the same password again for verification
3. Output:
   - If both inputs identical: `Password match.`
   - If hashes are different: `Different passwords.`
4. View the generated salt (printed in `latin-1` encoding)

## Learning Outcomes
- Understand how password hashing and salting work
- learn to securely compare sensitive values
- use real cryptographic functions (`pbkdf2_hmac`, `os.random`)
- simulate a basic login-style verification flow