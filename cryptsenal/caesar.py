"""
description: caesar cipher
author: ao wang
date: june 16, 2020
"""


from cipher import Cipher


class Caesar(Cipher):
    def __init__(self, text, key):
        super().__init__(text)
        self.key = key

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def getKey(self):
        return key

    def setKey(self, key):
        self.key = key
