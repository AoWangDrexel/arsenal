"""
This module implements two verions of the Columnar Transposition Cipher.

Example:
    $ python transposition.py

    import transposition as tp
    print(tp.ColumnarSimple.encrypt("Hello World", 3))
    > HlWleoodl r

    print(tc.ColumnarComplex.encrypt("Hello World", "zebras"))
    > odlreoll  HW
"""

import numpy as np
import math
import random
from itertools import permutations
from crypto import detect_english as de


class ColumnarSimple:
    """
    A class used to encrypt messages in the simplified version of the Columnar cipher.

    Methods:
        encrypt(plain_text, key)
            Returns the encrypted plain text
        decrypt(cipher_text, key)
            Returns the decrypted cipher text
        brute_force(cipher_text)
            Returns the decrypted cipher text by testing every possibility
    """
    def encrypt(plain_text, key):
        """The function encrypts the plain text using a certain key from 1-length of plain text and returns it.

            Args:
                plain_text (str): the plain text
                key (int): the number of columns to encrypt the text

            Returns:
                str: the cipher text

            Raises:
                TypeError
                    If there are any missing arguments or if plain_text is not a string and key is not an int.
        """
        cipher_text = [""] * key

        for i in range(key):
            row = i
            while row < len(plain_text):
                cipher_text[i] += plain_text[row]
                row += key
        return "".join(cipher_text)

    def decrypt(cipher_text, key):
        """The function decrypts the cipher text and returns the decrypted text.

            Args:
                cipher_text (str): the encrypted text
                key (int): the number of columns that was used to encrypt the text

            Returns:
                str: the decrypted cipher text

            Raises:
                TypeError
                    If there are any missing arguments or if cipher_text is not a string and key is not an int.
        """
        num_of_col = math.ceil(len(cipher_text) / float(key))
        num_of_row = key

        excess = num_of_col * num_of_row - len(cipher_text)
        plain_text = [""] * num_of_col

        col = 0
        row = 0
        for letter in cipher_text:
            plain_text[col] += letter
            col += 1
            if (col == num_of_col) or (col == num_of_col - 1
                                       and row >= num_of_row - excess):
                col = 0
                row += 1
        return "".join(plain_text)

    def brute_force(cipher_text):
        """The function hacks the Columnar Transposition Cipher and prints out the key and percentage
           of the words in the dictionary and returns the decrypted cipher text.

            Args:
                cipher_text (str): the encrypted text

            Returns:
                str: the decrypted cipher text

            Raises:
                TypeError
                    If there is any missing argument or if cipher_text is not a string.
        """
        print("Hacking...")

        percentages = {}

        for key in range(1, len(cipher_text)):
            decrypted_text = ColumnarSimple.decrypt(cipher_text, key)
            threshold = 80
            if de.get_english_count(decrypted_text) > threshold:
                percentages[key] = de.get_english_count(decrypted_text)

        key_break = de.find_max_ind(percentages)

        if key_break == -1:
            print("Failed to hack cipher :(")
        else:
            print("Cipher hacked! :)")

            print("The key is: " + str(key_break))
            print(
                "Decrypted text: " +
                ColumnarSimple.decrypt(
                    cipher_text,
                    key_break))
            print("Percentage of words in dictionary: " +
                  str(percentages[key_break]))
            return ColumnarSimple.decrypt(cipher_text, key_break)
        return -1


class ColumnarComplex:
    """
    A class used to encrypt messages using the complex columnar cipher.

    Methods:
        __order(word)
            Returns a list of the sorting order of the key
        encrypt(plain_text, key)
            Returns the encrypted plain text
        decrypt(cipher_text, key)
            Returns the decrypted cipher text
        brute_force(cipher_text)
            Returns the decrypted cipher text by testing all the possibilites until an acceptable
            percentage returns from the English detection
        __break_cipher(key_break, cipher_text)
            Returns the decrypted cipher text and the helper method for the brute_force method
    """

    def __order(word):
        """The function returns a list of the order the letter of the words should be
           alphabetically i.e. ZEBRAS 632415

           Args:
               word (str): the key for encryption

           Returns:
               list: the sorting order of the word

           Raises:
               TypeError:
                   If word is not passed as an argument or word is not a string type.
        """

        word_list = []
        for letter in word:
            word_list.append(letter)

        order_list = list(range(len(word)))
        letters = np.array(word_list)
        nums = np.array(order_list)
        inds = letters.argsort()
        nums = nums[inds]
        nums = list(nums)
        new_nums = list(range(len(nums)))
        n = 0

        for i in nums:
            new_nums[i] = n
            n += 1

        return new_nums

    def encrypt(plain_text, key):
        """The function encrypts the plain text and returns the cipher text.

            Args:
                plain_text (str): the plain text
                key (str): the word key

            Returns:
                str: the encrypted plain text

            Raises:
                TypeError
                    If there are any missing arguments or if the plain_text and key are not strings.
        """

        col = key
        ordering = ColumnarComplex.__order(col)
        col = len(col)
        row = math.ceil(len(plain_text) / col)
        grid = np.full((row, col), " ")
        idx = 0

        for i in range(row):
            for j in range(col):
                if(idx < len(plain_text)):
                    grid[i, j] = plain_text[idx]
                    idx += 1
    #             else:
    #                 r = random.randint(ord("A"), ord("Z"))
    #                 grid[i,j] = chr(r)

        cipher_text = ""
        idx = 0

        while idx != col:
            i = ordering.index(idx)
            for j in range(row):
                cipher_text += grid[j, i]
            idx += 1

        return cipher_text

    def decrypt(cipher_text, key):
        """The function decrypts the cipher text.

           Args:
               cipher_text (str): the encrypted text
               key (str): the word key

           Returns:
               str: the decrypted cipher text

           Raises:
               TypeError
                   If there are any missing arguments or if the cipher_text and key are not strings.
        """

        col = key
        ordering = ColumnarComplex.__order(col)
        col = len(col)
        row = math.ceil(len(cipher_text) / col)
        grid = np.full((row, col), " ")
        idx = 0
        l = 0

        while idx < col:
            i = ordering.index(idx)
            for j in range(row):
                if l < len(cipher_text):
                    grid[j, i] = cipher_text[l]
                    l += 1
            idx += 1

        plain_text = ""
        for i in range(row):
            for j in range(col):
                plain_text += grid[i, j]

        return plain_text

    def brute_force(cipher_text):
        """The function decrypts the cipher text by testing all the permutations from 1-length of cipher text. However
           once a permutation reaches a certain satification of English detection, the algorithm ends and returns the
           supposed encryption.

           Args:
               cipher_text (str): the encrypted text

           Returns:
               str: the decrypted cipher text

           Raises:
               TypeError:
                   If cipher_text is not passed in as an argument or cipher_text is not a string.
        """
        print("Hacking...")
        global percentages
        percentages = {}

        for length in range(1, len(cipher_text)):
            ordering = list(range(0, 1 + length))
            permutation_list = list(permutations(ordering))

            for p in permutation_list:
                len_of_col = len(p)
                row = math.ceil(len(cipher_text) / len_of_col)
                grid = np.full((row, len_of_col), " ")

                idx = 0
                l = 0

                while idx < len_of_col:
                    i = p.index(idx)
                    for j in range(row):
                        if l < len(cipher_text):
                            grid[j, i] = cipher_text[l]
                            l += 1
                    idx += 1

                plain_text = ""
                for i in range(row):
                    for j in range(len_of_col):
                        plain_text += grid[i, j]

                threshold = 85
                if de.get_english_count(
                        plain_text) >= threshold and de.get_english_count(plain_text) <= 100:
                    print("Percentage of English text: " +
                          str(de.get_english_count(plain_text)))
                    return ColumnarComplex.__break_cipher(p, cipher_text)
        return -1

    def __break_cipher(key_break, cipher_text):
        """The function is just a separate part of brute force to make it more concise.

           Args:
               key_break (tuple): the key order that decrypts the cipher text
               cipher_text (str): the cipher text

           Returns:
                str: the decrypted cipher text

           Raises:
               TypeError:
                   If any of the arguments are not passed as arguments or if key_break is not a list or tuple or
                   cipher_text is not a string type.
        """
        
        len_of_col = len(key_break)
        row = math.ceil(len(cipher_text) / len_of_col)
        grid = np.full((row, len_of_col), "")
        idx = 0
        l = 0

        while idx < len_of_col:
            i = key_break.index(idx)
            for j in range(row):
                if l < len(cipher_text):
                    grid[j, i] = cipher_text[l]
                    l += 1
            idx += 1

        plain_text = ""
        for i in range(row):
            for j in range(len_of_col):
                plain_text += grid[i, j]
        print("Key: " + str(key_break))
        return plain_text
