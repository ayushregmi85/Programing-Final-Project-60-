import hashlib
import getpass  # Import getpass module to securely input passwords


def change_password(username, current_password, new_password, password_file):
    # Read all lines from the password file
    with open(password_file, 'r') as file:
        lines = file.readlines()

    # Open the password file in 'write' mode
    with open(password_file, 'w') as file:
        password_changed = False
        # Iterate through each line in the file
        for line in lines:
            # Split the line into parts using ':' as the delimiter
            parts = line.split(':')

            # Check if the username and hashed current password match the provided credentials
            if parts[0] == username and hashlib.sha256(current_password.encode()).hexdigest() == parts[2].strip():
                # Hash the new password and write the updated information to the file
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                file.write(f"{parts[0]}:{parts[1]}:{hashed_password}\n")
                password_changed = True
            else:
                # If the username or current password doesn't match, write the line back to the file
                file.write(line)

        # Print a message based on whether the password was changed or not
        if password_changed:
            print("Password changed.")
        else:
            print("User not found or incorrect current password.")


if __name__ == "__main__":
    # Get user input for username and passwords
    username = input("User:             ")
    current_password = getpass.getpass("Current Password: ")  # Use getpass for secure password input
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm:      ")

    # Check if the new password and confirmation match
    if new_password == confirm_password:
        # Define the password file name
        password_file = "passwd.txt"

        # Call the change_password function to update the user's password
        change_password(username, current_password, new_password, password_file)
    else:
        print("Passwords do not match.")