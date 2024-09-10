import os
import sys
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def encrypt(original_text=text, shift_amount=shift):
    for letter in original_text.lower():
        encrypted_text=""
        if letter not in alphabet:
            encrypted_text+=letter
        else:
            encrypted_text = alphabet[alphabet.index(letter) + shift_amount]

        print(f"{encrypted_text}", end="")


def decrypt(original_text=text, shift_amount=shift):
    for letter in original_text.lower():
        decrypted_text = ""
        if letter not in alphabet:
            decrypted_text += letter
        else:
            decrypted_text = alphabet[alphabet.index(letter) - shift_amount]

        print(f"{decrypted_text}", end="")


def caesar():
    if direction == "encode":
        encrypt()
    else:
        decrypt()


caesar()

restart_option = input("\nDo you wish to restart? (y/n)\n")
if restart_option == "y":
    restart()
else:
    print("Goodbye!")





