import base64
import hashlib
from cryptography.fernet import Fernet

def create_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_text(text, password):
    key = create_key(password)
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

def decrypt_text(text, password):
    key = create_key(password)
    f = Fernet(key)
    return f.decrypt(text.encode()).decode()

