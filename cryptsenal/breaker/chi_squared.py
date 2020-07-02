from cryptsenal.caesar import Caesar
from pprint import pprint


class BreakCaesar():
    def __init__(self, cipherText):
        self.cipherText = cipherText
        self.frequency = {"A": 0.08497, "B": 0.01492, "C": 0.02202, "D": 0.04253, "E": 0.11162,
                          "F": 0.02228, "G": 0.02015, "H": 0.06094, "I": 0.07546, "J": 0.0153,
                          "K": 0.01292, "L": 0.04025, "M": 0.02406, "N": 0.06749, "O": 0.07507,
                          "P": 0.01929, "Q": 0.0095, "R": 0.07587, "S": 0.06327, "T": 0.09356,
                          "U": 0.02758, "V": 0.00978, "W": 0.0256, "X": 0.0015, "Y": 0.01994,
                          "Z": 0.0077}
        self.plainText = None
        self.key = None

    def __str__(self):
        return "Decrypted Message: {}\nKey: {}".format(self.plainText, self.key)

    def _chiSquared(self, text):
        def f(c, e): return (c-e)**2/e
        return sum([f(text.count(char), len(text) * self.frequency[char]) for char in self.frequency])

    def decrypt(self, show=False):
        chiSquaredDict = {}
        for key in range(26):
            c = Caesar(self.cipherText, key).decrypt()
            chiSquaredDict[self._chiSquared(c)] = key
        self.key = chiSquaredDict[min(chiSquaredDict)]
        self.plainText = Caesar(self.cipherText, self.key).decrypt()
        pprint(chiSquaredDict)
        return self.plainText

    def getCipherText(self):
        return self.cipherText

    def setCipherText(self, cipherText):
        self.cipherText = cipherText

    def getKey(self):
        return self.key

    def getPlainText(self):
        return self.plainText


if __name__ == "__main__":
    msg = """aoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwoly
zpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwsh
pualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohila"""
    b = BreakCaesar(msg)
    print(b.decrypt())
