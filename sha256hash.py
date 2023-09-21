import hashlib

def simple_hash(input_str):
    # Create a hashlib object (in this case, SHA-256 is used)
    hash_object = hashlib.sha256()

    # Update the hash object with the input string encoded as bytes
    hash_object.update(input_str.encode('utf-8'))

    # Get the hexadecimal digest of the hash
    hash_hex = hash_object.hexdigest()

    return hash_hex

