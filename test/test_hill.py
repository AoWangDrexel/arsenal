from cryptsenal.hill import Hill
import pytest


def test_encrypt():
    plainText = 'LESTERSHILLWASANAMERICANMATHEMATICIANANDEDUCATOR'
    cipherTexts = ["taxtxlbvtpnkuknnwyxlwknniwgzqolzwkognamttjeglzvz",
                   "xqedsxsnalposyanmqsxemanqopzamgvemcsnadrenuagvon",
                   "ttgxuxabwtpnwuangwuxywancilgyqqlywkonnvmataeqlav",
                   "pnxcripuxsbzmmnaiiriemnaeqyrswreemucnncpzqicrede",
                   "cfnpdjtjlngbewnnugdjwcnnciromaxdwckoanfixpykxdjh"]
    keys = (((5, 17),
             (4, 15)),
            ((23, 14),
             (12, 23)),
            ((245, 20),
             (5, 17)),
            ((35, 31),
             (23, 44)),
            ((24, 19),
             (5, 7)))
    for cipherText, key in zip(cipherTexts, keys):
        assert(Hill(plainText, key).encrypt() == cipherText.upper())


def test_bad_keys():
    plainText = 'LESTERSHILLWASANAMERICANMATHEMATICIANANDEDUCATOR'
    keys = (((9, 18),
             (3, 45)),
            ((11, 118),
             (55, 4)),
            ((100, 99),
             (98, 97)),
            ((1, 2),
             (3, 4)),
            ((2, 2),
             (3, 4)))
    with pytest.raises(Exception):
        for key in keys:
            Hill(plainText, key)


def test_decrypt():
    plainText = 'LESTERSHILLWASANAMERICANMATHEMATICIANANDEDUCATOR'
    cipherTexts = ["taxtxlbvtpnkuknnwyxlwknniwgzqolzwkognamttjeglzvz",
                   "xqedsxsnalposyanmqsxemanqopzamgvemcsnadrenuagvon",
                   "ttgxuxabwtpnwuangwuxywancilgyqqlywkonnvmataeqlav",
                   "pnxcripuxsbzmmnaiiriemnaeqyrswreemucnncpzqicrede",
                   "cfnpdjtjlngbewnnugdjwcnnciromaxdwckoanfixpykxdjh"]
    keys = (((5, 17),
             (4, 15)),
            ((23, 14),
             (12, 23)),
            ((245, 20),
             (5, 17)),
            ((35, 31),
             (23, 44)),
            ((24, 19),
             (5, 7)))
    for cipherText, key in zip(cipherTexts, keys):
        assert(Hill(cipherText, key).decrypt() == plainText)
