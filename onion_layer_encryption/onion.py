from caesar import caesar_encrypt
from mono_substitution import encrypt_mono_sub
from vigenere import vigenere_encrypt
import random
import string


def onion_encrypt(message, layers):
    random.shuffle(layers)

    encrypted = message

    shift = random.randint(1, 25)  # random shift for caesar

    # random substitiution key for mono_sub
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    substitution_key = dict(zip(alphabet, shuffled))

    length = random.randint(1, len(message))  # length of the keyword
    # random string for keyword for vigenere
    random_key = ''.join(random.choices(string.ascii_uppercase, k=length))

    for layer in layers:
        if layer == encrypt_mono_sub:  # pylint: disable=comparison-with-callable
            encrypted = encrypt_mono_sub(encrypted, substitution_key)
        elif layer == vigenere_encrypt:  # pylint: disable=comparison-with-callable
            encrypted = vigenere_encrypt(encrypted, random_key)
        elif layer == caesar_encrypt:  # pylint: disable=comparison-with-callable
            encrypted = caesar_encrypt(encrypted, shift)

    return encrypted, shift, substitution_key, random_key


if __name__ == "__main__":

    layers_options = [encrypt_mono_sub, vigenere_encrypt, caesar_encrypt]
    text = input("Please enter a message to encrypt:\n").strip().upper()

    onion, shift_c, sub_k, ran_k = onion_encrypt(text, layers_options)
    print("\nMessage Path:")
    print(f"-> Caesar shift: {shift_c}")
    print(f"-> Vigenènere key: {ran_k}")
    print(f"-> Mono key: {sub_k}")
    print(f"\nFinal Encrypted Message:\n{onion}")
