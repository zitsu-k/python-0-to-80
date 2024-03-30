import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars:{chars}")
# print(f"keys: {key}")

# ENCRYPTION

plain_text = input("Entre a message to encrypt: ")
clipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    clipher_text += key[index]

print(f"original message:{plain_text}")
print(f"encrypted message: {clipher_text}")

#DECRYPT
clipher_text= input("Entre a message to encrypt: ")
plain_text = ""
for letter in clipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {clipher_text}")
print(f"original message:{plain_text}")













