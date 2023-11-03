import os

# Define the alphabet list with characters for encryption and decryption
alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get the direction (encode or decode) from the user
direction = input("Type 'encode' to encrypt, 'decode' to decrypt the Message:\n")
text = input("Input your Message: \n").lower()
shift = int(input("Input the Shift Number: ")

# Function to encrypt plain text
def encrypt(plain_text, shift_amount):
    os.system('cls')  # Clear the terminal (for Windows, use 'clear' for Linux)
    cypher_text = ""
    for letters in plain_text:
        position = alphabet.index(letters)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The Cypher Text is {cypher_text}")

# Function to decrypt cypher text
def decode(cypher_text, shift_amount):
    os.system('cls')  # Clear the terminal (for Windows, use 'clear' for Linux)
    plain_text = ""
    for letters in cypher_text:
        position = alphabet.index(letters)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The Plain Text is {plain_text}")

# Decrypt the user input message (if needed)
decode(cypher_text=text, shift_amount=shift)

# Check the user's chosen operation (encode or decode)
if direction == "encode".lower():
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode".lower():
    decode(cypher_text=text, shift_amount=shift)
