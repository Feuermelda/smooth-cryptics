import random
import string


def encrypt_mono_sub(text, sub_key):
    encrypted = []
    for letter in text:
        if letter.isalpha():
            new_letter = sub_key[letter]
            encrypted.append(new_letter)
        else:
            encrypted.append(letter)

    return "".join(encrypted)


if __name__ == "__main__":
    plaintext = input("Please enter string to encrypt:\n").strip().upper()

    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)

    substitution_key = dict(zip(alphabet, shuffled))

    ciphertext = encrypt_mono_sub(plaintext, substitution_key)

    print("Your encrypted message:", ciphertext)
    print("Your substitution key:\n", substitution_key)
