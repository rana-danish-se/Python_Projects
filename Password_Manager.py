import os
from cryptography.fernet import Fernet

KEY_FILE = "key.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
fernet = Fernet(key)

master_password = input("Enter your master password: ")
if master_password == "your_secure_master_password":
    print("Access granted.")
    # Continue with the password manager functionality
else:
    print("Access denied. Incorrect master password.")
    exit(1)

def add_password():
    name = input("Enter the name of Account: ")
    password = input("Enter the password: ")
    encrypted_password = fernet.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as file:
        file.write(f"{name}:{encrypted_password}\n")
    print("Password added successfully.")

def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
            if not passwords:
                print("No passwords stored.")
            else:
                print("Stored Passwords:")
                for line in passwords:
                    name, encrypted_password = line.strip().split(":")
                    try:
                        password = fernet.decrypt(encrypted_password.encode()).decode()
                    except Exception:
                        password = "[Decryption failed]"
                    print(f"Account: {name}, Password: {password}")
    except FileNotFoundError:
        print("No passwords stored yet.")

while True:
    choice = input("Choose an option: (1) Add Password (2) View Passwords (3) Exit: ")
    if choice == "3":
        print("Exiting the password manager.")
        break
    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    else:
        print("Invalid choice. Please try again.")
        continue


     