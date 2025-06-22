from secrets import randbelow
from sympy import isprime
import shutil

width = shutil.get_terminal_size(fallback=(80, 20)).columns


def less_than_prime(num):
    if num > p:
        print("\nNumber must be less than your prime number! Try again.\n")
        return True
    else:
        return False


while True:
    try:
        print("=" * width)
        p = int(input("\nPlease enter a prime number:\n"))
        if not isprime(p):
            print("\nNumber must be a valid prime number! Try again.\n")
            continue
        g = int(input("\nPlease enter a base thats smaller than your prime number:\n"))
        if less_than_prime(g):
            continue

        else:
            break
    except ValueError:
        print("\nPlease only enter numbers!\n")

a = randbelow(p-2)+2
b = randbelow(p-2)+2

public_a = pow(g, a, p)
public_b = pow(g, b, p)

print(f"Public Key Sender: {public_a}")
print(f"Public Key Recipient: {public_b}")

shared_secret_A = pow(public_b, a, p)
shared_secret_B = pow(public_a, b, p)

if shared_secret_A == shared_secret_B:
    print(f"\nShared Secret is: {shared_secret_A}\n")
else:
    print("\nShared Secret doesn't match. Message might be tampered!\n")
    print(f"Sender's shared secret: {shared_secret_A}")
    print(f"Recipient's shared secret: {shared_secret_B}\n")
