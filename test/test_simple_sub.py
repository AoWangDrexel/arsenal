from cryptsenal.simple_substitution import SimpleSubstitution
import pytest


def test_encrypt():
    plainText = "BEWAREOFTHEMANINTHEYELLOWHAT"

    keys = ["phqgiumeaylnofdxjkrcvstzwb",
            "gwyvjsqkdiltbfphanremcxuoz",
            "qmilrzdfxjnoysaevtpukbwhgc",
            "jyxawtimhobucvgkrpnzfldeqs",
            "ivkhmwqdnfocjtypzsxgaelubr"]

    cipherTexts = ["hitpkiduceiopfafceiwinndtepc",
                   "wjxgnjpsekjbgfdfekjojttpxkge",
                   "mrwqtrazufryqsxsufrgrooawfqu",
                   "ywdjpwgtzmwcjvhvzmwqwuugdmjz",
                   "vmlismywgdmjitntgdmbmccyldig"]
    for cipherText, key in zip(cipherTexts, keys):
        assert SimpleSubstitution(
            plainText, key).encrypt() == cipherText.upper()


def test_decrypt():
    plainText = "BEWAREOFTHEMANINTHEYELLOWHAT"

    keys = ["phqgiumeaylnofdxjkrcvstzwb",
            "gwyvjsqkdiltbfphanremcxuoz",
            "qmilrzdfxjnoysaevtpukbwhgc",
            "jyxawtimhobucvgkrpnzfldeqs",
            "ivkhmwqdnfocjtypzsxgaelubr"]

    cipherTexts = ["hitpkiduceiopfafceiwinndtepc",
                   "wjxgnjpsekjbgfdfekjojttpxkge",
                   "mrwqtrazufryqsxsufrgrooawfqu",
                   "ywdjpwgtzmwcjvhvzmwqwuugdmjz",
                   "vmlismywgdmjitntgdmbmccyldig"]

    for key, cipherText in zip(keys, cipherTexts):
        assert SimpleSubstitution(
            cipherText.upper(), key).decrypt() == plainText
