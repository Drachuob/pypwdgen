import unittest
from pypwdgen import PasswordGenerator, PGF


class TestPasswordGenerator(unittest.TestCase):

    def test_size(self):
        """Test the password generate size."""
        size = 6
        generator = PasswordGenerator(PGF.LOWER, size=size)

        self.assertEqual(len(str(generator)), size)

    def test_only_lower(self):
        """Test lower password."""
        generator = PasswordGenerator(PGF.LOWER, size=6)
        password = str(generator)

        self.assertTrue(password.islower())

    def test_only_upper(self):
        """Test upper password."""
        generator = PasswordGenerator(PGF.UPPER, size=6)
        password = str(generator)

        self.assertTrue(password.isupper())

    def test_only_numeric(self):
        """Test numeric password."""
        generator = PasswordGenerator(PGF.NUMERIC, size=6)
        password = str(generator)

        self.assertTrue(password.isnumeric())

    def test_only_special(self):
        """Test special password."""
        generator = PasswordGenerator(PGF.SPECIAL, size=6)
        password = str(generator)
        tokens = "&~\"#'{([-|_\\^@)]=}¨£$¤*µ%!§:/;.,?<>"

        self.assertTrue(any(c in tokens for c in password))


if __name__ == '__main__':
    unittest.main()

