# AES - CBC encryption

This Python script demonstrates AES encryption in **CBC (Cipher Block Chaining)** mode using a sample `.txt` file as input. It includes full encryption, binary file output, decryption, and result verification.

---

## Features
- Reads plaintext from a `.txt` file
- Uses user-supplied key (auto-adjusted to valid AES lengths: 16, 24, or 32 bytes)
- Encrypts using AES-CBC with a randomly generated IV
- Saves encrypted output as binary `.bin` file (IV + ciphertext)
- Decrypts the output and verifies message integrity

---

## Usage
1. Run the script:
```bash
python aes_cbc_encryption
```
2. Follow the prompts:
   - Enter the filename (without `.txt` extension)
   - Enter an encryption key of any length (it will be padded or trimmed as needed)
3. Output:
   - Original plaintext
   - Encrypted data in hex format
   - Decrypted plaintext
   - Final match check: `True` if encryption/decryption round-trip succeeded

---

## Files
- `aes_cbc_encryption.py` - main encryption/decryption script
- `ingredient.txt` - sample plaintext input file
- `sealed_ingredient.bin` - binary file containing IV + ciphertext

