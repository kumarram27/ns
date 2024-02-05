def rail_fence_encrypt(message, rails):
    encrypted_message = ""
    for i in range(rails):
        encrypted_message += message[i::rails]
    return encrypted_message

def rail_fence_decrypt(encrypted_message, rails):
    decrypted_message = [""] * len(encrypted_message)
    index = 0
    for i in range(rails):
        j = i
        while j < len(encrypted_message):
            decrypted_message[j] = encrypted_message[index]
            index += 1
            j += rails
    return "".join(decrypted_message)

# Example
message = "GsGsekfrek eoe"
rails = 3
encrypted = rail_fence_encrypt(message, rails)
decrypted = rail_fence_decrypt(encrypted, rails)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
de=rail_fence_decrypt(message, 3)
print(de)