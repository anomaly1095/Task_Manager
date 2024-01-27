import hashlib
import secrets

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)  # Generate a random salt

    # Combine the password and salt and hash the result
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    
    # Return the salt and hashed password
    return salt, hashed_password

def verify_password(plaintext_password, stored_salt, stored_hashed_password):
    # Verify the password against the stored salt and hashed password
    hashed_password = hashlib.sha256((plaintext_password + stored_salt).encode('utf-8')).hexdigest()
    return hashed_password == stored_hashed_password