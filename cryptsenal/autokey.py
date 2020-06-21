"""
description: autokey cipher
author: ao wang
date: june 20, 2020
"""

from cryptsenal.cipher import Cipher


class AutoKey(Cipher):
    """The Autokey Cipher class

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: str
    """

    def __init__(self, text, key):
        super().__init__(text, key.upper())

    def encrypt(self):
        cipherText = ""
        arr = self.removePunctuation()
        for idx, char in enumerate(arr):
            if len(self.key) > idx:
                shift = self.charToInt(self.key[idx])
            else:
                shift = self.charToInt(self.text[idx-len(self.key)])
            cipherText += self.intToChar(self.charToInt(char)+shift)
        return cipherText

    def decrypt(self):
        plainText = ""
        arr = self.removePunctuation()
        for idx, char in enumerate(self.text):
            if len(self.key) > idx:
                shift = self.charToInt(self.key[idx])
            else:
                shift = self.charToInt(plainText[idx-len(self.key)])
            plainText += self.intToChar(self.charToInt(char)-shift)
        return plainText


if __name__ == "__main__":
    msg = "ISWXVIBJEXIGGZEQPBIMOIGAKMHE"
    key = "FORTIFICATION"
    print(AutoKey(msg, key).decrypt())
