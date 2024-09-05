import sys
from crypt_lib.decrypt import decrypt


def decrypt_user_inputs():

    if len(sys.argv) < 3:
        print("\nMissing key or string! Please provide a key and a string to encrypt!\n")
        exit()

    key_arg = sys.argv[1]
    str_arg = sys.argv[2]

    result = decrypt(key_arg, str_arg)

    return result


print(decrypt_user_inputs())

