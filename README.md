# Caesar Cipher

Small command-line Caesar cipher helper in Python. It shifts each alphabetic character by a key you choose and works for both encryption and decryption.

## Requirements
- Python 3.8+

## Usage
1. Run the script:
   ```bash
   python caesar_cipher.py
   ```
2. When prompted, choose `encrypt` or `decrypt`, provide a key (1-26), then enter your message.

Example session:
```text
*--*CAESAR CIPHER*--*
Do you want to encrypt or decrypt? encrypt
Enter the key (1 through 26): 3
Enter the message: attack at dawn
The result is: dwwdfn dw gdzq
```


## Notes
- Non-letter characters pass through unchanged.
- Keys wrap around the alphabet; a key of 26 returns the original text.

## License
This project is released under the MIT License. See LICENSE for details.
