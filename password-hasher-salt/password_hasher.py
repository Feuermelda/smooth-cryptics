import hashlib
import os
import hmac

password = input("Please enter password:\n").encode()

salt = os.urandom(16)
hash_password = hashlib.pbkdf2_hmac(
    'sha256', password, salt, 100)

hash_pw_saved = hash_password.hex()
print("Hashed Password: ", hash_pw_saved)

user = input("please enter password again:\n")
user = user.encode()

hash_user = hashlib.pbkdf2_hmac('sha256', user, salt, 100)

if hmac.compare_digest(hash_password, hash_user):
    print("Password match.")
else:
    print("Different passwords.")

iterations = 100
salt_hex = salt.hex()
hash_hex = hash_password.hex()
entry = f"{iterations}${salt_hex}${hash_hex}"

salt = bytes.fromhex(salt_hex).decode('latin-1')

print("Salt (decoded):", salt)
print("Stored format for DB:", entry)
