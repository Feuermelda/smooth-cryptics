import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


filename = input("Please enter filename:\n")
try:
    with open(filename + ".txt", "rb") as f:

        data = f.read()
except FileNotFoundError:
    print(f"Sorry, {filename}.txt was not found.")
    sys.exit()

key = input("Please enter a key (16, 24 or 32 bytes only):\n").strip()


key_lengths = [16, 24, 32]
for target_len in key_lengths:
    if len(key) < target_len:
        key = key.ljust(target_len, "x")
        break
    elif len(key) > key_lengths[-1]:
        key = key[:key_lengths[-1]]
        break

key_bytes = key.encode("utf-8")

padded = pad(data, AES.block_size)

iv = get_random_bytes(16)

cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(padded)

with open("sealed_ingredient.bin", "wb") as f:
    f.write(iv + ciphertext)

with open("sealed_ingredient.bin", "rb") as f:
    full = f.read()

iv = full[:16]
c_text = full[16:]

cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(c_text), AES.block_size)
hex_decrypted = decrypted.hex()
decrypted = decrypted.decode("utf-8")
str_data = data.decode("utf-8")

if decrypted == str_data:
    match = True
else:
    match = False


print("Original message: ", str_data)
print("Encrypted (hex): ", hex_decrypted)
print("Decrypted message: ", decrypted)
print("Match: ", match)
