# login.py
import hashlib


def authenticate_user(username, password, password_file):
    with open(password_file, 'r') as file:
        for line in file:
            parts = line.split(':')
            if parts[0] == username and hashlib.sha256(password.encode()).hexdigest() == parts[2].strip():
                return True
    return False


if __name__ == "__main__":
    username = input("User:     ")
    password = input("Password: ")

    password_file = "passwd.txt"
    if authenticate_user(username, password, password_file):
        print("Access granted.")
    else:
        print("Access denied.")
