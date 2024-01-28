# adduser.py
import hashlib

def add_user(username, real_name, password, password_file):
    with open(password_file, 'a') as file:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        file.write(f"{username}:{real_name}:{hashed_password}\n")
    print("User Created.")

if __name__ == "__main__":
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")

    password_file = "passwd.txt"  # You can hard-code the file name
    with open(password_file, 'r') as file:
        existing_users = [line.split(':')[0] for line in file]

    if username in existing_users:
        print("Cannot add. Most likely username already exists.")
    else:
        add_user(username, real_name, password, password_file)
