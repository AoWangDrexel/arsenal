"""
description: RSA Cryptosystem
author: ao wang
date: june 24, 2020
"""


from cryptsenal.cipher import Cipher
from cryptsenal.generate_rsa_key import RSAKey


class RSA(Cipher):
    """The RSA Cryptosystem

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: list

    Example
    =======
    key = [e, d, N]
    """

    def __init__(self, text, key):
        super().__init__(text, key)

    def encrypt(self):
        e, N = self.key[0], self.key[2]
        arr = self.removePunctuation()
        return "".join([self.intToChar(pow(self.charToInt(char), e, N)) for char in arr])

    def decrypt(self):
        d, N = self.key[1], self.key[2]
        arr = self.removePunctuation()
        return "".join([self.intToChar(pow(self.charToInt(char), d, N)) for char in arr])


if __name__ == "__main__":
    e, d, N = (17, 413, 3233)
    rsa = RSA("BEWARETHEWOLFE", [e, d, N])
    e_rsa = RSA("BJKAYJRDJKBTSJ", [e, d, N])
    print(rsa.encrypt())
    print(e_rsa.decrypt())
