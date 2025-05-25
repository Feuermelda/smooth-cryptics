from caesar import caesar_encrypt
from mono_substitution import encrypt_mono_sub
from vigenere import vigenere_encrypt
import random
import string


def onion_encrypt(message, layers, relays):
    random.shuffle(layers)
    random.shuffle(relays)

    encrypted = message
    relay1, relay2, relay3 = random.sample(relays, k=3)

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

    return encrypted, shift, substitution_key, random_key, relay1, relay2, relay3


if __name__ == "__main__":

    layers_options = [encrypt_mono_sub, vigenere_encrypt, caesar_encrypt]
    nodes = ["RaccoonLover69", "DijonardoSalad500", "EelParty001",
             "MilkShake9999", "MoelzmatTime420", "PickleOracle123"]
    text = input("Please enter a message to encrypt:\n").strip().upper()

    onion, shift_c, sub_k, ran_k, n1, n2, n3 = onion_encrypt(
        text, layers_options, nodes)
    print("\nMessage Path:")
    print(f"-> [{n1}] Caesar shift: {shift_c}")
    print(f"-> [{n2}] Vigenènere key: {ran_k}")
    print(f"-> [{n3}] Mono key: {sub_k}")
    print(f"\nFinal Encrypted Message:\n{onion}")
