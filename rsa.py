import sympy

def key():
    p = sympy.randprime(2, 500)
    q = sympy.randprime(2, 500)
    n = p * q
    f = (p - 1) * (q - 1)
    e = 2
    while sympy.gcd(e, f) != 1:
        e += 1
    d = sympy.mod_inverse(e, f)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [chr(pow(ord(char), e, n)) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(ord(char), d, n)) for char in ciphertext]
    return plain

text = input("Enter the Text:")
p, pr = key()
print(text)
print("Public key:", p)
print("Private key:", pr)
en_text = encrypt(p, text)
print("Encrypted:", en_text)
print("Encrypted:", ''.join([chr((ord(char) % 26) + 65) if char != ' ' else ' ' for char in en_text]))
dec_text = decrypt(pr, en_text)
print("Original text:", dec_text)
