import base64
from cryptography.fernet import Fernet


def encrypt(key_arg, str_arg):

    if key_arg == '' or str_arg == '' or key_arg is None or str_arg is None:
        return "Missing either a key or string argument"

    # The Fernet object requires a 32 byte array
    constant32 = 32

    # Encode the key_arg and append 32 characters of letter "a1b2c3" for padding.
    modified_key_arg_to_byte = str(key_arg + "a1b2c3" * constant32).encode("ascii")

    # Take a slice of 32 bytes of the modified key in base 64 form.
    base_64_arg = base64.urlsafe_b64encode(modified_key_arg_to_byte[0:constant32])

    # Create a Fernet object using the base 64 argument
    # The returned object follows this format:
    # b'aGlpa2V5YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWE='
    fernet_obj = Fernet(base_64_arg)

    # Convert the binary array back to a string
    encryption_result = str(fernet_obj.encrypt(str_arg.encode()), encoding='ascii')

    return encryption_result
