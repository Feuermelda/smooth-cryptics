# Write a short message from Eel to Milk, using Vigenère with the keyword BUBBLES. I’ll try to decode it!

def vigenere_encrypt(plaintext, keyword):

    result = ""
    textlist = list(plaintext)

    for i, plain_char in enumerate(textlist):
        if plain_char.isalpha():

            key_char = keyword[i % len(keyword)]
            shift_base = ord('A') if key_char.isupper() else ord('a')
            shift = (ord(key_char) - shift_base) % 26

            shift_base = ord('A') if plain_char.isupper() else ord('a')
            shifted = (ord(plain_char) - shift_base + shift) % 26
            new_char = (shifted + shift_base)
            result += chr(new_char)

        else:
            result += plain_char

    return result


if __name__ == "__main__":
    message = vigenere_encrypt(
        "the blades are sharp and so is my mind, but at night every sauce is black.", "milk")

    print(message)
