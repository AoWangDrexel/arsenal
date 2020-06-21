from cryptsenal.rail_fence import RailFence
import pytest


def test_encrypt():
    plainText = "BEWARETHEBLACKSHEEP"
    cipherTexts = ["breceeaehbakhewtlsp",
                   "beeehbhewtlspaeakrc",
                   "bwrtelcsepeaehbakhe",
                   "bceakwlsabhreeehetp",
                   "beehewspakrceatlhbe"]
    for key, cipherText in zip((3, 5, 2, 7, 9), cipherTexts):
        assert RailFence(plainText, key).encrypt() == cipherText.upper()


def test_decrypt():
    plainText = "BEWARETHEBLACKSHEEP"
    cipherTexts = ["breceeaehbakhewtlsp",
                   "beeehbhewtlspaeakrc",
                   "bwrtelcsepeaehbakhe",
                   "bceakwlsabhreeehetp",
                   "beehewspakrceatlhbe"]
    for key, cipherText in zip((3, 5, 2, 7, 9), cipherTexts):
        assert RailFence(cipherText.upper(), key).decrypt() == plainText
