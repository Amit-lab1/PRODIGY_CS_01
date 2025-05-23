# PRODIGY_CS_01
<br>
Task Name:- Implement Caesar Cipher
Task Description:- Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.
Author:- Amit Ashok Patil
<br>
code:-
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'encrypt':
        encrypted = caesar_cipher_encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    elif choice == 'decrypt':
        decrypted = caesar_cipher_decrypt(message, shift)
        print("Decrypted Message:", decrypted)
    else:
        print("Invalid choice. Please select 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
