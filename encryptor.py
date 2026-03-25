import sys

# Encrypts a plaintext string using the Vigenère cipher and a given key
def vigenere_encrypt(plaintext,key):
    ciphertext = ""   # Stores the encrypted result
    key = key.upper() # Converts key to uppercase
    key_index = 0     # Tracks which character of the key is used

    for char in plaintext:
    
        # Only letters are encrypted; characters are preserved
        if char.isalpha():  
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
            key_index += 1  # Moves to the next character in the key
        else:
            ciphertext += char

    return ciphertext

# Decrypts a ciphertext string using the Vigenère cipher and a given key
def vigenere_decrypt(ciphertext, key):
    plaintext = ""     # Stores the encrypted result
    key = key.upper()  # Converts key to uppercase
    key_index = 0      # Tracks which character of the key is used

    for char in ciphertext:
    
        # Only letters are decrypted; characters are preserved
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr(((ord(char.upper()) - ord('A') - shift + 26) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char

    return plaintext

def main():
    passkey = None  # Stores the current encryption/decryption key

    # Continuously read commands from standard input (sent by the driver)
    for line in sys.stdin:
        line = line.strip()
        # QUIT command ends the encryption program
        if line == "QUIT":
            break
        # Ignores empty input lines
        if not line:
            continue

        # Splits the input into a command and an optional argument
        parts = line.split(maxsplit=1)
        command = parts[0].upper()
        argument = parts[1] if len(parts) > 1 else ''

        # Sets or updates the passkey
        if command in ["PASS", "PASSKEY"]:
            passkey = argument
            # Flush ensures the driver immediately receives this response
            print("RESULT", flush=True)

        # Encrypts the provided string
        elif command == "ENCRYPT":
            if not passkey:
                print("ERROR Password not set", flush=True)
            else:
                print("RESULT", vigenere_encrypt(argument, passkey), flush=True)

        # Decrypts the provided string
        elif command == "DECRYPT":
            if not passkey:
                print("ERROR Password not set", flush=True)
            else:
                print("RESULT", vigenere_decrypt(argument, passkey), flush=True)

        else:
            # Handles any unsupported commands
            print("ERROR Unknown command", flush=True)  # <-- flush added

if __name__ == "__main__":
    main()
