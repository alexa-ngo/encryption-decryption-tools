import base64
from cryptography.fernet import Fernet


def decrypt(key_arg, encrypted_msg):

    if encrypted_msg == "Missing either a key or string argument" or "" or None:
        return "Missing either a key or string argument"

    # The Fernet object requires a 32 byte array
    constant32 = 32

    # Encode the key_arg and append 32 characters of letter "a1b2c3" for padding.
    modified_key_arg_to_byte = str(key_arg + "a1b2c3" * constant32).encode("ascii")

    # Take a slice of 32 bytes of the modified key in base 64 form.
    base_64_arg = base64.urlsafe_b64encode(modified_key_arg_to_byte[0:constant32])

    # The base_64_arg is a byte array that follows this format:
    # b'aGlpa2V5YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWE=
    decrypted_msg = Fernet(base_64_arg).decrypt(encrypted_msg).decode()

    return decrypted_msg
