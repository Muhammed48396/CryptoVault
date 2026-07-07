import hashlib

def generate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def generate_sha512(text):
    return hashlib.sha512(text.encode()).hexdigest()

def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def verify_hash(text, hash_value, algorithm):
    algorithm = algorithm.lower()

    if algorithm == "sha256":
        return generate_sha256(text) == hash_value

    elif algorithm == "sha512":
        return generate_sha512(text) == hash_value

    elif algorithm == "md5":
        return generate_md5(text) == hash_value

    else:
        return False
