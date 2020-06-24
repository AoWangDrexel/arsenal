"""
description: generates RSA keys
author: ao wang
date: june 24, 2020
"""

from math import gcd
from sympy import isprime, mod_inverse
from numpy import lcm


class RSAKey():
    """The RSAKey class

    1. pick 2 prime numbers, p and q
    2. multiply them to get N = p * q, becomes the modulus
    3. phi function phi(N) =  (p-1)(q-1) or number of coprimes with N
    4. find e, got to be between 1 < e < phi(N),
        coprime with N, phi(N)
    5. find d, (d * e) % phi(N) = 1
    """
    def __init__(self, p, q):
        self.p = p
        self.q = q
        if isprime(p) and isprime(q):
            self.N = p * q
            self.totient = lcm(p-1, q-1)
        else:
            raise Exception("p or q are not prime numbers")

    def getE(self):
        return [i for i in range(2, self.totient) if gcd(i, self.totient) == 1]

    def getD(self, E):
        return mod_inverse(E, self.totient)

    def getP(self):
        return self.p

    def setP(self, p):
        if isprime(p):
            self.p = p
        else:
            raise Exception("p is not a prime number")

    def getQ(self):
        return self.q

    def setQ(self, q):
        if isprime(q):
            self.q = q
        else:
            raise Exception("q is not a prime number")


if __name__ == "__main__":
    rsa = RSAKey(61, 53)
    print(rsa.N, rsa.getE(), rsa.getD(17))
