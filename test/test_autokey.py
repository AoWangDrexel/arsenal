from cryptsenal.autokey import AutoKey
import pytest


def test_encrypt():
    plainText = "THEFISHSWIMSATMIDNIGHT"
    keys = ["gesture", "highlight", "enemy", "cane", "executive"]
    cipherTexts = ["zlwycjlldmrasaeelzagaf",
                   "apkmtanzpbtwfbepvjqszt",
                   "xuirglowbqezspuuvnbspw",
                   "vhrjbzlxeatkwbyadguokg",
                   "xeihclpnabtwfbepvjqszt"]
    for key, cipherText in zip(keys, cipherTexts):
        assert AutoKey(plainText, key).encrypt() == cipherText.upper()


def test_decrypt():
    plainText = "THEFISHSWIMSATMIDNIGHT"
    keys = ["gesture", "highlight", "enemy", "cane", "executive"]
    cipherTexts = ["zlwycjlldmrasaeelzagaf",
                   "apkmtanzpbtwfbepvjqszt",
                   "xuirglowbqezspuuvnbspw",
                   "vhrjbzlxeatkwbyadguokg",
                   "xeihclpnabtwfbepvjqszt"]
    for key, cipherText in zip(keys, cipherTexts):
        assert AutoKey(cipherText, key).decrypt() == plainText
