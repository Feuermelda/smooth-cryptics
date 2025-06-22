# Diffie-Hellman Key Exchange Simulation
This python scripts demonstrates a secure key exchange using the Diffie-Hellman method.

## Requirements
- Python 3.x
- `secrets` (built-in)
- `sympy` library
- `shutil` library (built-in)

## Features
- Prompts user for a prime number
- Asks for a base (ideally a primitive root of the prime)
- Generates two random private keys using `secrets.randbelow`
- Computes and prints public keys
- Simulates key exchange by using public keys to compute a shared secret
- Verifies if both computed secrets match
- **Displays a warning if the secrets differ - simulating tampering**

## Usage
1. Enter a valid prime number
2. Enter a base smaller than the prime number (ideally a primitive root)
3. Watch the public key generation and exchange
4. Output:
    - If matching: Shared Secret Key will be displayed
    - If not matching: Warning that message may be tampered

# Learning Outcomes
- Understand how secure key sharing works without transmitting the secret
- Simulate real-world cryptographic key exchange
- Learn about modular arithmetic and efficient functions like `pow()` (used instead of `g**a % p` for performance and safety)