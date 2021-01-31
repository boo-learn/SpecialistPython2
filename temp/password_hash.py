import os
import hashlib

def get_hash(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    return salt + key


def check_password(password, hash):
    salt = hash[:32] # 32 is the length of the salt
    key = hash[32:]
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        salt,
        100000
    )
    return new_hash == key

password = 'password246'

hash = get_hash(password)

if check_password(password, hash):
    print("Password is correct")
else:
    print("Password is incorrect")