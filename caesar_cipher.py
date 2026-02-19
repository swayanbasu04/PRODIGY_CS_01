letters= 'abcdefghijklmnopqrstuvwxyz'
num_letters= len(letters)

# Encryption and Decryption functions
# def encrypt(plaintext, key):
#     ciphertext=' '
#     for letter in plaintext:
#         letter= letter.lower()
#         if not letter == ' ':
#             index= letter.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 newindex= index + key
#                 if new_index >= 26:
#                     new_index -= 26
#                 ciphertext += letters[new_index]
#     return ciphertext


# def decrypt(ciphertext, key):
#     plaintext=' '
#     for letter in plaintext:
#         letter= letter.lower()
#         if not letter == ' ':
#             index= letter.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index= index - key
#                 if new_index >0:
#                     new_index += 26
#                 plaintext += letters[new_index]
#     return plaintext
# Combined function for encryption and decryption

def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == 'decrypt':
        key=-key

    for letter in text:
        letter = letter.lower()
        if letter.isupper():
            result += letter
        else:
            index= letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index= index+key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index+=num_letters
                result+= letters[new_index]
    return result


def main():
    print("*--*CAESAR CIPHER*--*")
    mode = input("Do you want to encrypt or decrypt? ").lower()
    while True:
         try:
            key = int(input("Enter the key (1 through 26): "))
            if not 1 <= key <= 26:
                print(f"Key {key} must be in between 1 to 26. Try again.")
                continue
            break
         except ValueError:
             print("Invalid input. Please enter a number between 1 and 26.")
    # continue
    # while True:
    #         key = int(input("Enter the key (1 through 26): "))
    #         if not 1 <= key <= 26:
    #             print("Key must be between 1 and 26. Try again.")
    #             continue
    #         except ValueError:


    text = input("Enter the message: ")
    result = encrypt_decrypt(text, mode=mode, key=key)
    print(f"The result is: {result}") 
    
    
if __name__ == "__main__":
    main()
