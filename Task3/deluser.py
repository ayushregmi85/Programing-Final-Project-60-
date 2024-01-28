def delete_user(username, password_file):
    # Read all lines from the password file
    with open(password_file, 'r') as file:
        lines = file.readlines()