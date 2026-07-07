# ==========================================================
# CryptoVault Security Suite
# crypto.py
# ==========================================================

import base64
import hashlib

from cryptography.fernet import Fernet


# ----------------------------------------------------------
# Anahtar Oluştur
# ----------------------------------------------------------

def generate_key(password):

    key = hashlib.sha256(password.encode()).digest()

    return base64.urlsafe_b64encode(key)


# ----------------------------------------------------------
# Metin Şifrele
# ----------------------------------------------------------

def encrypt_text(text, password):

    key = generate_key(password)

    cipher = Fernet(key)

    encrypted = cipher.encrypt(text.encode())

    return encrypted.decode()


# ----------------------------------------------------------
# Metin Çöz
# ----------------------------------------------------------

def decrypt_text(encrypted_text, password):

    try:

        key = generate_key(password)

        cipher = Fernet(key)

        decrypted = cipher.decrypt(encrypted_text.encode())

        return decrypted.decode()

    except Exception:

        return "❌ Hatalı parola veya bozuk veri!"
