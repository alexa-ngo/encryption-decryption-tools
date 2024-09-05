from crypt_lib.encrypt import encrypt
import unittest


class TestEncryption(unittest.TestCase):

    def test_missing_both_keyarg_and_strarg(self):
        the_key = ""
        the_input = ""
        result = encrypt(the_key, the_input)
        self.assertEqual(result, "Missing either a key or string argument")

    def test_missing_keyarg(self):
        the_key = ""
        the_input = "groupoffriends"
        result = encrypt(the_key, the_input)
        self.assertEqual(result, "Missing either a key or string argument")

    def test_missing_strarg(self):
        the_key = "running"
        the_input = ""
        result = encrypt(the_key, the_input)
        self.assertEqual(result, "Missing either a key or string argument")

    def test_none_keyarg(self):
        the_key = None
        the_input = "hello there"
        result = encrypt(the_key, the_input)
        self.assertEqual(result, "Missing either a key or string argument")

    def test_none_strarg(self):
        the_key = "sunnykey"
        the_input = None
        result = encrypt(the_key, the_input)
        self.assertEqual(result, "Missing either a key or string argument")

    def test_both_none(self):
        the_key = None
        the_input = None
        result = encrypt(the_key, the_input)
        self.assertEqual(result, "Missing either a key or string argument")

    def test_bobkey_joestring(self):
        the_key = "bobkey"
        the_input = "joestring"
        result = encrypt(the_key, the_input)

        # A different encryption result is generated each time, so we know that
        # the encrypt function works if the input and the result are different each time
        self.assertNotEqual(result, the_input)


if __name__ == "__main__":
    unittest.main()
