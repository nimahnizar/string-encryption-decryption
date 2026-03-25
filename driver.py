import subprocess
import sys


# Checks that a string contains only alphabets
def is_letters_only(a):
    return a.isalpha()
    
# Sends a formatted log message to the logger process
def log(logger_in,action,message):
    logger_in.write(f"{action} {message}\n")
    logger_in.flush() # Flush so the logger receives the message immediately


# Reads a single line response from the encryption program
def read_response(proc):
    return proc.stdout.readline().strip()


# Displays the history menu and allows the user to select a value
# Returns the selected string or None if the user wants to enter a new one
def display_history(history):
    if not history:
        print("History is empty")
        return None

    while True:
        print("\nHistory:")
        for i, item in enumerate(history):
            print(f"{i + 1}. {item}")
        print("0. Enter a new string")

        choice = input("Choose an option: ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(history):
            return history[int(choice) - 1]

        print("Invalid choice.")


def main():

    # Ensure the log file name is provided
    if len(sys.argv) != 2:
        print("Usage: python driver.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]

    # Start logger
    logger = subprocess.Popen(
        ["python3", "logger.py", logfile],
        stdin=subprocess.PIPE,
        text=True
    )

    # Start encryption program
    encryptor = subprocess.Popen(
        ["python3", "encryptor.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    history = []  # Stores strings entered and results for this session only

    log(logger.stdin, "START", "Driver started") # Log the start of the driver


    while True:
        print("\nCommands: password, encrypt, decrypt, history, quit")
        cmd = input("Enter command: ").strip().lower()

        if cmd == "password":
            log(logger.stdin, "COMMAND", "password")

            choice = display_history(history)
            if choice is None:
                pwd = input("Enter new password (letters only): ").strip()
                if not is_letters_only(pwd):
                    print("Error: Password must contain only letters.")
                    log(logger.stdin, "ERROR", "Invalid password")
                    continue
            else:
                pwd = choice

            # Send passkey to encryption program
            encryptor.stdin.write(f"PASSKEY {pwd.upper()}\n")
            encryptor.stdin.flush()
            response = read_response(encryptor)

            log(logger.stdin, "RESULT", response)
            print(response)

        # Handles encrypt command
        elif cmd == "encrypt":
            log(logger.stdin, "COMMAND", "encrypt")

            choice = display_history(history)
            if choice is None:
                text = input("Enter string to encrypt (letters only): ").strip()
                if not is_letters_only(text):
                    print("Error: Input must contain only letters.")
                    log(logger.stdin, "ERROR", "Invalid encryption input")
                    continue
                history.append(text)
            else:
                text = choice

            encryptor.stdin.write(f"ENCRYPT {text.upper()}\n")
            encryptor.stdin.flush()
            response = read_response(encryptor)

            print(response)
            log(logger.stdin, "RESULT", response)

            # Stores the encrypted result in history
            if response.startswith("RESULT"):
                result = response.split(" ", 1)[1] if " " in response else ""
                history.append(result)

        # Handles decrypt command
        elif cmd == "decrypt":
            log(logger.stdin, "COMMAND", "decrypt")

            choice = display_history(history)
            if choice is None:
                text = input("Enter string to decrypt (letters only): ").strip()
                if not is_letters_only(text):
                    print("Error: Input must contain only letters.")
                    log(logger.stdin, "ERROR", "Invalid decryption input")
                    continue
                history.append(text)
            else:
                text = choice

            encryptor.stdin.write(f"DECRYPT {text.upper()}\n")
            encryptor.stdin.flush()
            response = read_response(encryptor)

            print(response)
            log(logger.stdin, "RESULT", response)

            # Stores the decrypted result in history
            if response.startswith("RESULT"):
                result = response.split(" ", 1)[1] if " " in response else ""
                history.append(result)

        # Displays the current history
        elif cmd == "history":
            log(logger.stdin, "COMMAND", "history")
            print("\nHistory:")
            for item in history:
                print(item)

        elif cmd == "quit":
            log(logger.stdin, "EXIT", "Driver exiting")

            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()

            logger.stdin.write("QUIT\n")
            logger.stdin.flush()

            break

        else:
            # Handles unknown commands
            print("Unknown command.")
            log(logger.stdin, "ERROR", "Unknown command")

    # Wait for child processes to exit
    encryptor.wait()
    logger.wait()

if __name__ == "__main__":
    main()


