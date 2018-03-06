#! /usr/bin/env python3.6
"""Password generator module."""

import enum
import secrets


class PGF(enum.IntFlag):
    """PGF for Password Generator Flags."""
    LOWER = 1
    UPPER = 2
    NUMERIC = 4
    SPECIAL = 8


class PasswordGenerator(object):
    """A password generator class."""

    def __init__(self, flags, size=32):
        """Initialize the password generator.
        
        Args:
            flags: The alphabet options (See PGF).
            size: The password size, default 32.

        Raises:
            ValueError: If the flags equal 0.
        """
        self.size = size
        self.tokens = []

        if flags == 0:
            raise ValueError("Wrong flag")
        if flags & PGF.LOWER:
            self.tokens += "abcdefghijklmnopqrstuvwxyz"
        if flags & PGF.UPPER:
            self.tokens += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if flags & PGF.NUMERIC:
            self.tokens += "0123456789"
        if flags & PGF.SPECIAL:
            self.tokens += "&~\"#'{([-|_\\^@)]=}¨£$¤*µ%!§:/;.,?<>"

        self.alphabet = []
        while len(self.tokens) != 0:
            size = len(self.tokens)
            self.alphabet.append(self.tokens.pop(secrets.randbelow(size)))

    def __str__(self):
        """Generate a new password each time it's called.
        
        Raises:
            ValueError: If no alphabet is set.

        Returns:
            The password in a string.
        """
        pwd = ''
        size = len(self.alphabet)

        if self.alphabet == "":
            raise ValueError("Alphabet is not set.")
        pwd = [self.alphabet[secrets.randbelow(size)] for i in range(self.size)]
        return ''.join(pwd)

if __name__ == "__main__":
    import pyperclip


    flags = 0

    flags ^= PGF.UPPER
    flags ^= PGF.LOWER
    flags ^= PGF.NUMERIC
    flags ^= PGF.SPECIAL
    pwd = str(PasswordGenerator(flags))
    pyperclip.copy(pwd)
    print("Copy password on the clipboard.")
