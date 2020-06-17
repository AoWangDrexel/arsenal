from cryptsenal.vigenere import Vigenere
import pytest


def test_encrypt():
    plainText = "GIOVANBATTISTABELLASOWASANITALIANCRYPTOLOGIST"
    cipherTexts = ["BQUZNRSEOBOWGESIGTGWBARWVVOXNPZEIKXCCXFPJOOWG",
                   "IZMKTFFNTEKJRPUWPYADQNYHTFMGAWKRLRKQTGOWQXGHM",
                   "GWKVNTBOPTVYTOXEYRAGKWNYABETNRIOJCEEPHKLBMIGP",
                   "VGHCOAQYMAWFIYULZYPQHDOFPLBAOYXYGJFLERHSCTXQM",
                   "HMZGAFPBXETSLOCIWWAKCXEDLNAHBPTLNUFZTEZLGUJWE"]
    for cipherText, key in zip(cipherTexts, ("vigenere", "cryptsenal", "aowang", "python", "bellaso")):
        assert Vigenere(plainText, key).encrypt() == cipherText


def test_decrypt():
    plainText = "GIOVANBATTISTABELLASOWASANITALIANCRYPTOLOGIST"
    cipherTexts = ["BQUZNRSEOBOWGESIGTGWBARWVVOXNPZEIKXCCXFPJOOWG",
                   "IZMKTFFNTEKJRPUWPYADQNYHTFMGAWKRLRKQTGOWQXGHM",
                   "GWKVNTBOPTVYTOXEYRAGKWNYABETNRIOJCEEPHKLBMIGP",
                   "VGHCOAQYMAWFIYULZYPQHDOFPLBAOYXYGJFLERHSCTXQM",
                   "HMZGAFPBXETSLOCIWWAKCXEDLNAHBPTLNUFZTEZLGUJWE"]
    for cipherText, key in zip(cipherTexts, ("vigenere", "cryptsenal", "aowang", "python", "bellaso")):
        assert Vigenere(cipherText, key).decrypt() == plainText
