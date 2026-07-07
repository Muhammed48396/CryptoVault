from hash_tools import *
from base64_tools import *

def security_menu():

    while True:

        print("\n==============================")
        print("🛠️ SECURITY TOOLS")
        print("==============================")
        print("1. SHA-256")
        print("2. SHA-512")
        print("3. MD5")
        print("4. Hash Doğrula")
        print("5. Base64 Encode")
        print("6. Base64 Decode")
        print("0. Geri")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            text = input("Metin: ")
            print("\nSHA-256:\n")
            print(generate_sha256(text))

        elif secim == "2":
            text = input("Metin: ")
            print("\nSHA-512:\n")
            print(generate_sha512(text))

        elif secim == "3":
            text = input("Metin: ")
            print("\nMD5:\n")
            print(generate_md5(text))

        elif secim == "4":

            print("\nAlgoritmalar:")
            print("1. SHA-256")
            print("2. SHA-512")
            print("3. MD5")

            algo = input("Seçim: ")

            if algo == "1":
                algorithm = "sha256"
            elif algo == "2":
                algorithm = "sha512"
            elif algo == "3":
                algorithm = "md5"
            else:
                print("Geçersiz seçim!")
                continue

            text = input("Metin: ")
            hash_value = input("Hash: ")

            if verify_hash(text, hash_value, algorithm):
                print("\n✅ Hash Doğru!")
            else:
                print("\n❌ Hash Eşleşmiyor!")

        elif secim == "5":
            text = input("Metin: ")
            print("\nBase64:\n")
            print(encode_base64(text))

        elif secim == "6":
            text = input("Base64: ")
            print("\nÇözülmüş Metin:\n")
            print(decode_base64(text))

        elif secim == "0":
            break

        else:
            print("❌ Geçersiz seçim!")
