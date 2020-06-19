from cryptsenal.columnar_transposition import ColumnarTransposition
import pytest


def test_encrypt():
    plainText = "YESWHITEHATHACKERSCANWEARWHITEHATSAFTERLABORDAY"
    keys = ["harvest", "insure", "encourage", "ego", "volunteer"]
    cipherTexts = ["eheeetrhhcwtlyyekwtfosarahediaahsaxtcniabxwtsrara",
                   "ihsaefbxytacrhtoeecawaerhtretaayshknhtrdwaewisla",
                   "tersoxshnerxyacitahshfdxerwarxetateywawhlxikatbxhceaax",
                   "ywtaaecwrihstloaehetcraewtaaearysihhksnahetfrbdx",
                   "tersoxerwarxshnerxhceaaxetateyhshfdxikatbxwawhlxyacita"]
    for key, cipherText in zip(keys, cipherTexts):
        assert ColumnarTransposition(
            plainText, key).encrypt() == cipherText.upper()


def test_decrypt():
    plainText = "YESWHITEHATHACKERSCANWEARWHITEHATSAFTERLABORDAY"
    keys = ["harvest", "insure", "encourage", "ego", "volunteer"]
    cipherTexts = ["eheeetrhhcwtlyyekwtfosarahediaahsaxtcniabxwtsrara",
                   "ihsaefbxytacrhtoeecawaerhtretaayshknhtrdwaewisla",
                   "tersoxshnerxyacitahshfdxerwarxetateywawhlxikatbxhceaax",
                   "ywtaaecwrihstloaehetcraewtaaearysihhksnahetfrbdx",
                   "tersoxerwarxshnerxhceaaxetateyhshfdxikatbxwawhlxyacita"]

    for key, cipherText in zip(keys, cipherTexts):
        fit = ColumnarTransposition(plainText, key).completeTheSquare()
        assert ColumnarTransposition(
            cipherText.upper(), key).decrypt() == fit
