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
    msg = 'hell'
    key = RSAKey()
    e = key.e
    d = key.d
    n = key.N
    rsa1 = RSA(msg, [e, d, n])
    print("e: ", rsa1.encrypt())
    msg1 = 12075635579884793402937353706728104107680795696111912688365121642370022039503841911509666172059463730616240559218465405131290741951641447396412585016619482104385666711668837233123750678128284043779688196442204711362334623540775963807257018693750579925195875466161460720679838900341639370809425445882070730987841095146311535819683870045544675921373792210473151936545750524813673211617121645966327655279058574183695003047772817377789387514290835954627296539144271218460326596428874442561310108275675624775073901542481882398061147749845294873123412078765327197348698683226986020428249913990660913137678272945240004174206
    rsa2 = RSA(msg1, [e, d, n])
    print("d: ", rsa2.decrypt())
