from cryptsenal.cipher import Cipher
from cryptsenal.simple_substitution import SimpleSubstitution


class Enigma(Cipher):
    def __init__(self, text, key):
        super().__init__(text, key)

    def encrypt(self):
        return super().encrypt()

    def decrypt(self):
        return super().decrypt()
