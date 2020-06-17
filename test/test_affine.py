from cryptsenal.affine import Affine
import pytest


def test_encrypt():
    plainText = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    cipherTexts = ["ZRCKEWSGNPAOVHATBEQFUAJCPZRCLIDYXAM",
                   "TNSYAUEIXFKODZKVBAWRMKHSFTNSPQJCLKG",
                   "IWTFJXRZQGDLCUDMYJBEHDKTGIWTAPONSDV",
                   "CSJTFVDBAWNLKMNOYFHQZNIJWCSJEXURGNP",
                   "TJAKWMUSRNECBDEFPWYHQEZANTJAVOLIXEG"]
    for cipherText, key in zip(cipherTexts, ((5, 8), (7, 16), (1, 15), (3, 23), (3, 40))):
        assert Affine(plainText, key).encrypt() == cipherText


def test_wrong_key():
    badKeys = ((2, 10), (4, 10), (6, 10), (8, 10), (10, 10))
    plainText = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    with pytest.raises(Exception):
        for key in badKeys:
            Affine(plainText, key)


def test_decrypt():
    plainText = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    cipherTexts = ["ZRCKEWSGNPAOVHATBEQFUAJCPZRCLIDYXAM",
                   "TNSYAUEIXFKODZKVBAWRMKHSFTNSPQJCLKG",
                   "IWTFJXRZQGDLCUDMYJBEHDKTGIWTAPONSDV",
                   "CSJTFVDBAWNLKMNOYFHQZNIJWCSJEXURGNP",
                   "TJAKWMUSRNECBDEFPWYHQEZANTJAVOLIXEG"]
    for cipherText, key in zip(cipherTexts, ((5, 8), (7, 16), (1, 15), (3, 23), (3, 40))):
        assert Affine(cipherText, key).decrypt() == plainText
