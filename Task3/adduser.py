import hashlib

def add_user(username, real_name, password, password_file):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Open the password file in 'append' mode and write the user information
    with open(password_file, 'a') as file:
        file.write(f"{username}:{real_name}:{hashed_password}\n")

    # Print a message indicating that the user has been created
    print("User Created.")

if __name__ == "__main__":
    # Get user input for new user details
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")