# RSA PGP-style Secure Messenger
This Python script simulates a basic **PGP-style message exchange** using RSA encryption, digital signatures, and key handling.

## Requirements
- Python 3.x
- `pycryptodome` library (`pip install pycryptodome`)

## Features
- Accepts two user-defined names: sender and recipient
- Loads existing RSA keys or generates new ones
- Lets the sender enter a secret message
- Encrypts the message using `PKCS1_OAEP`
- Signs the message with `SHA256` and `pkcs1_15`
- Simulates attacker tampering with random probability
- Encodes and decodes messages with `base64`
- Decrypts and verifies the message
- Warns if the message has been tampered
- Displays message and optionally saves keys to .pem files

## Usage
1. Enter two names - sender and recipient
2. Choose wether to load existing keys or generate new ones
3. Type a secret message
4. Simulate message transfer
5. Output:
   - If the message and signature match: print the decrypted message and optionally save keys
   - If the message has been tampered with: print a warning

## Learning Outcomes
- Gain a better understanding of secure message transfer
- Explore real-world dangers through simulated tampering
- Learn to use real cryptographic tools like `PKCS1_OAEP` and `pkcs1_15`
- Practice proper key storage using `.pem` files
