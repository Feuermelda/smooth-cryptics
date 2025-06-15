from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import random
import re


# Prompt user for sender and recipient names
# Input is split into two names to simulate two parties
while True:
    choose_name = input(
        "Please choose a name for the two parties (separated by whitespace, 1. Sender, 2. Recipient):\n").strip().split()

    try:
        sender = choose_name[0]
        recipient = choose_name[1]
        break

    except IndexError:
        print("Please enter exactly TWO names!")

# Ask if the user wants to load previously saved RSA keys
load_keys = input(
    "Do you want to load previous keys? [Y for Yes / N for No]:\n").strip().lower()

if load_keys == "y":
    try:
        # Read and decode PEM key files
        with open(f"{sender}_private.pem", "rb") as f:
            sender_data = f.read().decode("utf-8")  # decodes bytes to string
        with open(f"{recipient}_private.pem", "rb") as f:
            recipient_data = f.read().decode("utf-8")

        # Extract the RSA key blocks using regex
        pem_blocks_sender = re.findall(
            r"-----BEGIN RSA PRIVATE KEY-----(.*?)-----END RSA PRIVATE KEY-----", sender_data, re.DOTALL)
        pem_blocks_recipient = re.findall(
            r"-----BEGIN RSA PRIVATE KEY-----(.*?)-----END RSA PRIVATE KEY-----", recipient_data, re.DOTALL)

        if not pem_blocks_sender or not pem_blocks_recipient:
            raise ValueError(
                "One saved PEM file does not contain a valid RSA private key.")

        # Reconstruct full PEM strings
        sender_pem = "-----BEGIN RSA PRIVATE KEY-----" + \
            pem_blocks_sender[0] + "-----END RSA PRIVATE KEY-----"
        recipient_pem = "-----BEGIN RSA PRIVATE KEY-----" + \
            pem_blocks_recipient[0] + "-----END RSA PRIVATE KEY-----"

        # Convert PEM strings into usable RSA key objects
        sender_key = RSA.import_key(sender_pem)
        recipient_key = RSA.import_key(recipient_pem)

        print("\nLoading keys for sender and recipient...\n")

    except FileNotFoundError:
        print("Error. No saved keys.")


else:
    # If no keys are loaded, generate new 2048-bit RSA key pairs
    print("\nGenerating keys for sender and recipient...\n")

    sender_key = RSA.generate(2048)
    recipient_key = RSA.generate(2048)

# Derive public keys for encryption and verification
sender_public = sender_key.publickey()
recipient_public = recipient_key.publickey()

# Prompt sender for a secret message
message = input(
    f"{sender}, please enter a secret message to {recipient}:\n").strip()
message_bytes = message.encode()

# Encrypt message using recipient's public key and OAEP padding for confidentiality
encryptor = PKCS1_OAEP.new(recipient_public)
encrypted_message = encryptor.encrypt(message_bytes)

# Create a SHA-256 hash of the original message
message_hash = SHA256.new(message_bytes)

# Sign the hash with sender's private key to ensure integrity and authenticity
signature = pkcs1_15.new(sender_key).sign(message_hash)

# 20% chance of a simulated "attacker" altering the message and signature
attacker_chance = random.random()

if attacker_chance >= 0.8:
    # Tamper with the encrypted message and break the signature
    encrypted_message = encryptor.encrypt(
        b"Hello, I am an attacker and I am hacking you.")
    signature = b"FAKE"

# Encode the message and signature to base64 for simulated transmission
encoded_message = base64.b64encode(encrypted_message)
encoded_signature = base64.b64encode(signature)

# Print the simulated transmission
print(
    f"\nEncrypted message:\n{encoded_message.decode()}\n\nSignature from {sender}:\n{encoded_signature.decode()}")
print(f"\nNow sending both to {recipient}...\n")

# Simulate the recipient receiving and decoding the message
received_message = base64.b64decode(encoded_message)
received_signature = base64.b64decode(encoded_signature)

# Decrypt the message using recipient's private key
decryptor = PKCS1_OAEP.new(recipient_key)
decrypted_message = decryptor.decrypt(received_message)

# Hash the decrypted message again for signature verification
decrypted_hash = SHA256.new(decrypted_message)

try:
    # Verify that the signature matches the decrypted message and sender's public key
    pkcs1_15.new(sender_public).verify(decrypted_hash, received_signature)
    print(f"Signature valid ✔\n\nMessage from {sender}:")
    print(decrypted_message.decode())

    # Offer to save keys if they were newly generated
    if load_keys != "y":
        save_key = input(
            "Do you want to save both keys for future use? [Y for Yes / N for No]:\n").strip().lower()

        if save_key == "y":
            with open(f"{sender}_private.pem", "wb") as f:
                f.write(sender_key.export_key())
            with open(f"{recipient}_private.pem", "wb") as f:
                f.write(recipient_key.export_key())

        elif save_key == "n":
            print("\nAll right, have a nice day! And stay safe!\n")

        else:
            print("Invalid command. Keys not saved.")

except (ValueError, TypeError):
    # Signature verification failed - possible tampering detected
    print("Signature invalid or tampered. Do not trust sender!")
