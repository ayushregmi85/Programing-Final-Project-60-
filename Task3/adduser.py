import hashlib

def add_user(username, real_name, password, password_file):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()