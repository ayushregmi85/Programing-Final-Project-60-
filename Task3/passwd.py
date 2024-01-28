# passwd.py
import hashlib
import getpass

def change_password(username, current_password, new_password, password_file):
    with open(password_file, 'r') as file:
        lines = file.readlines()

    with open(password_file, 'w') as file:
        password_changed = False
        for line in lines:
            parts = line.split(':')
            if parts[0] == username and hashlib.sha256(current_password.encode()).hexdigest() == parts[2].strip():
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                file.write(f"{parts[0]}:{parts[1]}:{hashed_password}\n")
                password_changed = True
            else:
                file.write(line)

        if password_changed:
            print("Password changed.")
        else:
            print("User not found or incorrect current password.")

if __name__ == "__main__":
    username = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm:      ")

    if new_password == confirm_password:
        password_file = "passwd.txt"
        change_password(username, current_password, new_password, password_file)
    else:
        print("Passwords do not match.")
