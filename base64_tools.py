import base64

def encode_base64(text):
    encoded = base64.b64encode(text.encode())
    return encoded.decode()

def decode_base64(encoded_text):
    try:
        decoded = base64.b64decode(encoded_text)
        return decoded.decode()
    except:
        return "❌ Geçersiz Base64!"
