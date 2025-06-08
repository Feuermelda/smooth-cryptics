import hashlib

msg = input("Please enter a message: ").strip()
key = input("Please enter a secret key: ").strip()


key_bytes = key.encode()


# Modify key size if necessary
if len(key_bytes) > 64:
    secret_key = hashlib.sha256(key_bytes).digest()
elif len(key_bytes) < 64:
    length = 64 - len(key_bytes)
    padding = (length * b'\x00')
    secret_key = key_bytes + padding
else:
    secret_key = key_bytes

print("Modified key (hex): ", secret_key.hex())
print("Original key: ", key)


# build inner and outer padded keys

ipad_bytes = bytes([0x36]) * 64

opad_bytes = bytes([0x5c]) * 64


# inner and outer hash

ipad_bytes = list(ipad_bytes)
secret_key = list(secret_key)
ipad_key = [x ^ y for x, y in zip(secret_key, ipad_bytes)]

ipad_key = bytes(ipad_key)
inner_concat = ipad_key + msg.encode()

inner_hash = hashlib.sha256(inner_concat).digest()

opad_bytes = list(opad_bytes)
opad_key = [x ^ y for x, y in zip(secret_key, opad_bytes)]

opad_key = bytes(opad_key)
outer_concat = opad_key + inner_hash

outer_hash = hashlib.sha256(outer_concat).digest()

print("Outer hash (hex):", outer_hash.hex())
