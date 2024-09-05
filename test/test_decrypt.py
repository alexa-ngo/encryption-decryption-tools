from crypt_lib.encrypt import encrypt
from crypt_lib.decrypt import decrypt
import unittest


class TestEncryption(unittest.TestCase):

    def test_ideal_case(self):
        the_key = "hi-key"
        the_input = "bye-string"
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "bye-string")

    def test_girls_secret(self):
        the_key = "the girl club"
        the_input = "secrets are shared"
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "secrets are shared")

    def test_gold_key(self):
        the_key = "gold key"
        the_input = "the secret message"
        encrypt_result = encrypt(the_key, the_input)

        # A different encryption result is generated each time, so we know that
        # the encrypt function works if the input and the result are different each time
        self.assertNotEqual(encrypt_result, the_input)

        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "the secret message")

    def test_missing_both_keyarg_and_strarg(self):
        the_key = ""
        the_input = ""
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "Missing either a key or string argument")

    def test_missing_keyarg(self):
        the_key = ""
        the_input = "groupoffriends"
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "Missing either a key or string argument")

    def test_missing_strarg(self):
        the_key = "running"
        the_input = ""
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "Missing either a key or string argument")

    def test_none_keyarg(self):
        the_key = None
        the_input = "hello there"
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "Missing either a key or string argument")

    def test_none_strarg(self):
        the_key = "sunnykey"
        the_input = None
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "Missing either a key or string argument")

    def test_both_none(self):
        the_key = None
        the_input = None
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)
        self.assertEqual(final_result, "Missing either a key or string argument")

    def test_bobkey_joestring(self):
        the_key = "bobkey"
        the_input = "joestring"
        encrypt_result = encrypt(the_key, the_input)
        final_result = decrypt(the_key, encrypt_result)

        # A different encryption result is generated each time, so we know that
        # the encrypt function works if the input and the result are different each time
        self.assertEqual(final_result, the_input)


if __name__ == "__main__":
    unittest.main()
