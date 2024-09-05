import sys
from crypt_lib.encrypt import encrypt


def encrypt_user_inputs():

    if len(sys.argv) < 3:
        print("\nMissing key or string! Please provide a key and a string to encrypt!\n")
        exit()

    key_arg = sys.argv[1]
    str_arg = sys.argv[2]

    result = encrypt(key_arg, str_arg)

    return result


print(encrypt_user_inputs())

