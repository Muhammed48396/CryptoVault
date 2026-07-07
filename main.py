# ==========================================================
# CryptoVault Security Suite
# Version : 1.0
# Developer : Lexy
# Studio : Lexy Studio
# ==========================================================

import os
import time
import platform
from datetime import datetime

from colorama import init, Fore, Style

from crypto import encrypt_text, decrypt_text
from password import generate_password
from security_menu import security_menu

# ==========================================================
# COLORAMA
# ==========================================================

init(autoreset=True)

# ==========================================================
# APP INFO
# ==========================================================

APP_NAME = "CryptoVault"
VERSION = "1.0"
DEVELOPER = "Lexy"
STUDIO = "Lexy Studio"

# ==========================================================
# COLORS
# ==========================================================

SUCCESS = Fore.GREEN
ERROR = Fore.RED
WARNING = Fore.YELLOW
INFO = Fore.CYAN
TITLE = Fore.MAGENTA
MENU = Fore.BLUE
TEXT = Fore.WHITE
RESET = Style.RESET_ALL

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(
        WARNING +
        "\nDevam etmek için Enter'a bas..."
    )


def line():
    print(MENU + "═" * 65)


def header(title):
    clear()

    line()

    print(
        TITLE +
        f"🔐 {APP_NAME} Security Suite v{VERSION}"
    )

    print(
        INFO +
        title
    )

    line()


def success(message):
    print(
        SUCCESS +
        f"\n✔ {message}"
    )


def error(message):
    print(
        ERROR +
        f"\n✖ {message}"
    )


def warning(message):
    print(
        WARNING +
        f"\n⚠ {message}"
    )


def info(message):
    print(
        INFO +
        f"\nℹ {message}"
    )


# ==========================================================
# SYSTEM INFO
# ==========================================================

def current_time():
    return datetime.now().strftime("%H:%M:%S")


def current_date():
    return datetime.now().strftime("%d/%m/%Y")


def python_version():
    return platform.python_version()


def operating_system():
    return platform.system()

# ==========================================================
# BOOT SCREEN
# ==========================================================

def splash_screen():

    clear()

    logo = f"""{TITLE}

 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝

{RESET}
"""

    print(logo)

    print(INFO + f"Developer : {DEVELOPER}")
    print(INFO + f"Studio    : {STUDIO}")
    print(INFO + f"Version   : {VERSION}")
    print()

    print(WARNING + "Başlatılıyor...\n")

    for i in range(0, 101, 5):

        bar = "█" * (i // 5)
        space = "░" * (20 - (i // 5))

        print(
            SUCCESS + f"\r[{bar}{space}] {i}%",
            end="",
            flush=True
        )

        time.sleep(0.05)

    time.sleep(0.5)

    clear()


# ==========================================================
# MAIN MENU
# ==========================================================

def show_menu():

    header("🏠 Ana Menü")

    print(INFO + f"📅 Tarih   : {current_date()}")
    print(INFO + f"🕒 Saat    : {current_time()}")
    print(INFO + f"💻 Sistem  : {operating_system()}")
    print(INFO + f"🐍 Python  : {python_version()}")

    line()

    print(SUCCESS + "[1] 🔒 Metin Şifrele")
    print(SUCCESS + "[2] 🔓 Metin Çöz")
    print(SUCCESS + "[3] 🔑 Güçlü Parola Üret")
    print(SUCCESS + "[4] 🛡 Security Tools")
    print(INFO    + "[5] ℹ Hakkında")
    print(ERROR   + "[0] 🚪 Çıkış")

    line()

# ==========================================================
# MENÜ FONKSİYONLARI
# ==========================================================

def encrypt_menu():

    header("🔒 Metin Şifreleme")

    text = input("\nŞifrelenecek metin : ")
    password = input("Parola             : ")

    try:

        encrypted = encrypt_text(text, password)

        success("Metin başarıyla şifrelendi.")

        print("\nŞifreli Metin:\n")
        print(encrypted)

    except Exception as e:

        error(f"Hata: {e}")

    pause()


def decrypt_menu():

    header("🔓 Metin Çözme")

    encrypted = input("\nŞifreli metin : ")
    password = input("Parola        : ")

    try:

        decrypted = decrypt_text(encrypted, password)

        success("Metin başarıyla çözüldü.")

        print("\nÇözülen Metin:\n")
        print(decrypted)

    except Exception as e:

        error(f"Hata: {e}")

    pause()


def password_menu():

    header("🔑 Güçlü Parola Oluştur")

    try:

        length = input("\nParola uzunluğu (Boş bırak = 16): ")

        if length.strip() == "":
            length = 16
        else:
            length = int(length)

        password = generate_password(length)

        success("Parola oluşturuldu.")

        print("\nYeni Parolan:\n")
        print(password)

    except ValueError:

        error("Lütfen geçerli bir sayı gir.")

    except Exception as e:

        error(str(e))

    pause()


def about_menu():

    header("ℹ Hakkında")

    print(f"Program      : {APP_NAME}")
    print(f"Sürüm        : {VERSION}")
    print(f"Geliştirici  : {DEVELOPER}")
    print(f"Stüdyo       : {STUDIO}")

    print("\nBu uygulama güvenli metin şifreleme,")
    print("parola oluşturma ve güvenlik")
    print("araçlarını tek yerde toplamak")
    print("amacıyla geliştirilmektedir.")

    pause()

# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    splash_screen()

    while True:

        show_menu()

        choice = input(
            Fore.GREEN +
            "\n➜ Seçimin : " +
            Fore.WHITE
        ).strip()

        if choice == "1":

            encrypt_menu()

        elif choice == "2":

            decrypt_menu()

        elif choice == "3":

            password_menu()

        elif choice == "4":

            try:
                security_menu()
            except Exception as e:
                error(f"Security Tools açılamadı!\n{e}")
                pause()

        elif choice == "5":

            about_menu()

        elif choice == "0":

            header("Çıkış")

            success("CryptoVault güvenli şekilde kapatıldı.")

            print(INFO)
            print("Görüşmek üzere 👋")

            time.sleep(1)

            clear()

            break

        else:

            warning("Geçersiz seçim!")

            time.sleep(1)


# ==========================================================
# START
# ==========================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        clear()

        warning("Program kullanıcı tarafından durduruldu.")

    except Exception as e:

        clear()

        error(f"Beklenmeyen hata:\n{e}")

