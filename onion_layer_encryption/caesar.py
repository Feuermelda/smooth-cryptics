def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - shift_base + shift) % 26
            result += chr(shift_base + shifted)
        else:
            result += char  # Leave puncuation/spaces/etc untouched

    return result


def caesar_decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - shift_base - shift) % 26
            result += chr(shift_base + shifted)
        else:
            result += char

    return result


if __name__ == "__main__":

    print(
        f"decryption: {caesar_decrypt("ymnx nx f hnumjw rjxxflj tk ymj qfspnsl", 5)}")

    print(caesar_encrypt("When you are ready to set sail, we will be waiting for you. The tomatoes have yet to ripe and the sun has yet to shine.", 13))
