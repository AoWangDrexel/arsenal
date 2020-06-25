"""
description: RSA Cryptosystem
author: ao wang
date: june 24, 2020
"""


from cryptsenal.cipher import Cipher
from cryptsenal.generate_rsa_key import RSAKey
import binascii
import random


class RSA():
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
        self.text = text
        self.key = key

    def _toHex(self):
        hexData = binascii.hexlify(self.text.encode())
        return int(hexData, 16)

    def encrypt(self):
        """
        c(m) = m^e mod N
        """
        e, N = self.key[0], self.key[2]
        text = self._toHex()
        return pow(text, e, N)

    def decrypt(self):
        """
        m(c) = c^d mod N
        """
        d, N = self.key[1], self.key[2]
        return binascii.unhexlify(hex(pow(self.text, d, N))[2:]).decode()


if __name__ == "__main__":
    random.seed(0)
    msg = "Beware the White Hat Hacker."
    key = RSAKey()
    e, d, n = key.e, key.d, key.N
    rsa1 = RSA(msg, [e, d, n])
    encryptedMessage = rsa1.encrypt()
    print("e: ", encryptedMessage)
    rsa2 = RSA(encryptedMessage, [e, d, n])
    print("d: ", rsa2.decrypt())
