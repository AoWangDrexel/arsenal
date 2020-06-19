from cryptsenal.cipher import Cipher


class SimpleSubstitution(Cipher):
    def __init__(self, text, key):
        super().__init__(text, key)

    def encrypt(self):
        return super().encrypt()

    def decrypt(self):
        return super().decrypt()
