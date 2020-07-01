"""
description: enigma machine
author: ao wang
date: june 31, 2020
"""

from cryptsenal.cipher import Cipher
import string


class Enigma(Cipher):
    """The Enigma Machine (M3) class

    :param text: the plain/cipher text
    :type text: str
    :param keySetting: the key setting
    :type keySetting: tuple
    :param ringSetting: the ring setting
    :type ringSetting: tuple
    :param rotorOrder: the rotor order
    :type rotorOrder: tuple
    :param reflector: the B/C reflectors
    :type reflector: str
    :param plugBoard: the plug board
    :type plugBoard: str
    """

    def __init__(self, text, keySetting, ringSetting, rotorOrder, reflector, plugBoard):
        self.keySetting = keySetting
        self.ringSetting = ringSetting
        self.rotorOrder = rotorOrder

        plugBoard = plugBoard.split()
        plugBoardDict = {}
        for pair in plugBoard:
            f, s = list(pair)
            plugBoardDict[f] = s
            plugBoardDict[s] = f
        self.plugBoard = plugBoardDict

        self.relector = reflector
        self.rotors = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                       "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                       "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
        self.inverseRotors = ["UWYGADFPVZBECKMTHXSLRINQOJ",
                              "AJPCZWRLFBDKOTYUQGENHXMIVS",
                              "TAGBPCSDQEUFVNZHYIXJWLRKOM"]
        self.reflectors = {"B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                           "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}

    def __str__(self):
        return self.plugBoard

    def applyRotors(self, char):
        for i in range(3):
            pos = string.ascii_uppercase.find(char)
            char = self.rotors[i][pos]
        return char

    # Steckerverbindungen
    def reflect(self, char):
        return self.reflectors[self.relector][string.ascii_uppercase.find(char)]

    def encrypt(self):
        cipherText = ""
        arr = self.removePunctuation()
        for char in arr:
            letter = self.applyRotors(char)
            letter = self.reflect(letter)

        return super().encrypt()

    def decrypt(self):
        return super().decrypt()

    def getKeySetting(self):
        return self.keySetting

    def setKeySetting(self, keySetting):
        self.keySetting = keySetting

    def getRingSetting(self):
        return self.ringSetting

    def setKeySetting(self, ringSetting):
        self.ringSetting = ringSetting

    def getRotorOrder(self):
        return self.rotorOrder

    def setRotorOrder(self, rotorOrder):
        self.rotorOrder = rotorOrder

    def getPlugBoard(self):
        return self.plugBoard

    def setPlugBoard(self, plugBoard):
        self.plugBoard = plugBoard


if __name__ == "__main__":
    pass
