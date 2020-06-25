"""
description: generates RSA keys
author: ao wang
date: june 24, 2020
"""

from math import gcd
from sympy import isprime, randprime, mod_inverse
from numpy import lcm
import random
import base64


def generateLargePrime(keySize=1024):
    return randprime(2**(keySize-1), 2**keySize)


class RSAKey():
    """The RSAKey class

    1. pick 2 prime numbers, p and q
    2. multiply them to get N = p * q, becomes the modulus
    3. phi function phi(N) =  (p-1)(q-1) or number of coprimes with N
    4. find e, got to be between 1 < e < phi(N),
        coprime with N, phi(N)
    5. find d, (d * e) % phi(N) = 1
    """

    def __init__(self, keySize=1024):
        self.p = generateLargePrime(keySize)
        self.q = generateLargePrime(keySize)
        self.N = self.p * self.q
        self.keySize = keySize

        # Update using Carmichael's instead of Euler's  (p-1)(q-1)
        self.totient = lcm(self.p-1, self.q-1)

        while True:
            e = random.randrange(2**(self.keySize-1), 2**self.keySize)
            if gcd(e, self.totient) == 1:
                break

        self.e = e
        self.d = mod_inverse(e, self.totient)

    def __str__(self):
        string = "-----BEGIN PUBLIC KEY-----\n"
        string += self._toBase64(self.e)
        string += "\n-----END PUBLIC KEY-----\n\n"

        string += "-----BEGIN RSA PRIVATE KEY-----\n"
        string += self._toBase64(self.d)
        string += "\n-----END RSA PRIVATE KEY-----"
        return string

    def _toBase64(self, key):
        key = str(key)
        keyBytes = key.encode("ascii")
        return base64.b64encode(keyBytes).decode('utf-8')

    def saveAsText(self, key):
        pass


if __name__ == "__main__":
    rsa = RSAKey()
    print(rsa.e)
    print(rsa.d)
    print(rsa.N)
