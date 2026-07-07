# ==========================================================
# CryptoVault Security Suite
# File      : password.py
# Version   : 1.0
# Developer : Lexy
# Studio    : Lexy Studio
# ==========================================================

import secrets
import string

# Karakter Grupları
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{}<>?/"

# Tüm karakterler
ALL = LOWER + UPPER + DIGITS + SYMBOLS


def generate_password(length=16):
    """
    Güçlü rastgele parola oluşturur.
    En az 8 karakter olmalıdır.
    """

    if length < 8:
        length = 8

    password = [
        secrets.choice(LOWER),
        secrets.choice(UPPER),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]

    while len(password) < length:
        password.append(secrets.choice(ALL))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
