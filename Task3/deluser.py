def delete_user(username, password_file):
    # Read all lines from the password file
    with open(password_file, 'r') as file:
        lines = file.readlines()

    # Open the password file in 'write' mode
    with open(password_file, 'w') as file:
        user_deleted = False
        # Iterate through each line in the file
        for line in lines:
            # Check if the username in the current line matches the one to be deleted
            if line.split(':')[0] != username:
                # If not, write the line back to the file
                file.write(line)
            else:
                # If the username matches, mark the user as deleted
                user_deleted = True

        # Print a message based on whether the user was deleted or not
        if user_deleted:
            print("User Deleted.")
        else:
            print("User not found.")


if __name__ == "__main__":
    # Get user input for the username to be deleted
    username = input("Enter username: ")

    # Define the password file name
    password_file = "passwd.txt"

    # Call the delete_user function to delete the specified user
    delete_user(username, password_file)
