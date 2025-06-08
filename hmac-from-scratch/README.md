# Hash-based Message Authentication Code (HMAC)

This Python projects demonstrates a **manually implemented HMAC algorithm**, built from scratch **without using the `hmac` library**.

## Features
- Accepts a custom message and secret key.
- Automatically adjusts the key to match the HMAC block size (64 bytes for SHA-256).
- Uses inner and outer padding with XOR logic.
- Returns the final HMAC hash (**digest**) of the message.


## Usage
1. Run the script
2. Enter a message
3. Enter a key
4. View the modified key (in hex) and the resulting HMAC digest

## Learning Outcome
A hands-on exploration of how HMAC works internally, including:
- Byte padding
- XOR operations
- SHA-256 usage
- Basic message **integrity checking**