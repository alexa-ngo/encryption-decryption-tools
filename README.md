# `🔐` The Encryption Tool and Decryption Tool

The encryption tool and decryption tool are two separate tools that can work together to help with your encryption and decryption needs! 😃 

## 🔒 Encryption Tool

To use the **encryption tool**, you would simply provide a key and a string you would like to encrypt, and then an encrypted string is returned.

`$ python3 encrypt_input.py your-key your-msg-string`

Example:

`(.venv) super_person@pc:~/encryption-decryption-project$ python3 encrypt_input.py your-key your-msg-string`

A similar encrypted string is returned:
`gAAAAABmzg04LWC5w8sLOly-R4eyxNhSQ1OZMHZraW7MMD5Zth_LfelbiQpPU3CNgAssfyWvunxY_2fqkEbJQSuZ3MKRu_-7ww==`

## 🔑 Decryption Tool
Similarly, to use the **decryption tool**, you would use "your-key" as the first argument and the encrypted string generated from the encryption tool as the second argument.

`$ python3 decrypt_input.py your-key gAAAAABmzg04LWC5w8sLOly-R4eyxNhSQ1OZMHZraW7MMD5Zth_LfelbiQpPU3CNgAssfyWvunxY_2fqkEbJQSuZ3=MKRu_-7ww==`


### How to Use the Encryption and Decryption Tool
1. Install the virtual environment for python3.11 using `$ sudo apt install python3.11-venv`
2. Be in the encrypt-decrypt-project directory
3. Start your virtual Python environment using
`$ python3 -m venv ./.venv`, and then activate the virtual environment with `$ source ./.venv/bin/activate`
3. Install the dependencies in requirements.txt using `pip install -r requirements.txt`
4. Install the cryptography module by running `pip install cryptography` in your terminal

### Why use ASCII instead of UTF-8
For both the encryption and decryption tool, we are using ascii characters instead of UTF-8 because ascii characters are easier to work with. Each ascii character uses one byte compared to UTF-8 which uses two bytes per character. Additionally, we are not using UTF-8 because we are not working with international characters such as Chinese characters.

### How the Encryption Program Works

1. The user inputs their key argument and the string they would like to encrypt.
2. We then append 32 characters of random numbers and letters for padding to the key argument, and we would encode it.
3. Next, we take a slice of 32 bytes of the modified key in base 64 form.
4. Then a Fernet object is created using the byte array.
5. Finally, we return the binary array as a string.

### How the Decryption Program Works

The decryption program works similarly to the encryption program.

1. The user inputs their key argument and the string they would like to decrypt.
2. We then append 32 characters of random numbers and letters for padding to the key argument, and we would encode it.
3. Next, we take a slice of 32 bytes of the modified key in base 64 form.
4. Finally, we return the decrypted base 64 argument in the Fernet object.

# 🏃‍♀️Running the Tests

There were tests written for both the encryption and decryption tool, and here is how we run them!  ✅ 📝

To run the tests:

1. Be one file directory up from the test directory, and enter `python -m test.test_encrypt` to run the encryption test:

`(.venv) super_person@pc:~/encryption-decryption-project$ python -m test.test_encrypt`

After hitting `ENTER`, the terminal notification should show *"Ran 7 tests in 0.00x s"*.

We would do the same is for the decryption tests, which run 10 tests.

`(.venv) super_person@pc:~/encryption-decryption-project$ python -m test.test_decrypt`

## Conclusion

.. and that is how this *encryption tool and decryption tool* works! *Happy encrypting and decrypting!* 😃🔐 