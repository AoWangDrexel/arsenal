from cryptsenal import detect_english as de

"""The Caesar Cipher Module.

The Caesar Implementation includes encryption and decryption. 
There is also a brute force algorithm, along with a letter freqency
cipher break.
"""


def encrypt(plain_text, key):
    """Encrypts the plain text with key.
    
    Example
    =======
    >>> from cryptsenal.caesar import *
    >>> encrypt("Hello World", 2)
    Jgnnq Yqtnf

    Args:
        plain_text (str): A plain text.
        key (int): A key shift.

    Returns:
        str: A cipher text. 
    """
    letter, cipher_text = "", ""
    for symbol in plain_text:
        if symbol.isalpha():
            letter = chr((ord(symbol.upper()) + key - ord("A")) % 26 + ord("A"))
            cipher_text += letter if symbol.isupper() else letter.lower()
        else:
            cipher_text += symbol
    return cipher_text


def letter_count(text):
    """Counts the number of each alphabet in the text.
    
    Example
    =======
    >>> from cryptsenal.caesar import *
    >>> letter_count("How was your day?")
    {'H': 1, 'O': 2, 'W': 2, 'A': 2, 'S': 1, 'Y': 2, 'U': 1, 'R': 1, 'D': 1}
    Args:
        text (str): A string of text.

    Returns:
        dict: A frequency of the alphabet in the text.
    """
    letter_dict = {}
    text = text.upper()
    for letter in text:
        if letter.isalpha():
            if letter not in letter_dict.keys():
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict


def decrypt(cipher_text, key):
    """Decrypts a cipher text.
    
    Example
    =======
    >>> from cryptsenal.caesar import *
    >>> decrypt("Jgnnq Yqtnf", 2)
    Hello World
    
    Args:
        cipher_text (str): A cipher text.
        key (int): A key.

    Returns:
        str: A plain text.
    """
    while key < 0:
        key += 26
    if key > 0:
        key = 26 - key
    return encrypt(cipher_text, key)


def cryptanalysis(cipher_text):
    """Decrypts the cipher by finding the most frequent letter.
    
    Example
    =======
    >>> from cryptsenal.caesar import *
    >>> msg = \"""
    Qctpyod, Czxlyd, nzfyecjxpy, wpyo xp jzfc plcd;T nzxp ez mfcj Nlpdlc,
    yze ez acltdp stx.Esp pgtw esle xpy oz wtgpd lqepc espx;Esp rzzo td 
    zqe tyepccpo htes esptc mzypd;Dz wpe te mp htes Nlpdlc.
    \"""
    >>> cryptanalysis(msg)
    Friends, Romans, countrymen, lend me your ears;I come to bury Caesar,
    not to praise him.The evil that men do lives after them;The good is
    oft interred with their bones;So let it be with Caesar.
    
    Args:
        cipher_text (str): A cipher text.

    Returns:
        str: A plain text.
    """
    alphabet = [chr(ord("A") + i) for i in range(26)]
    letter_dict = letter_count(cipher_text)
    key_list, val_list = list(letter_dict.keys()), list(letter_dict.values())
    key_break = key_list[val_list.index(max(letter_dict.values()))]
    break_key = alphabet.index(key_break) - alphabet.index("E")
    if break_key <= 0:
        break_key += 26
    return encrypt(cipher_text, 26 - break_key)


def brute_force(cipher_text):
    """Prints the plain text by trying all 25 keys.
    
    Example
    =======
    >>> from cryptsenal.caesar import *
    >>> brute_force("Jgnnq Yqtnf")
    Cipher hacked! :)
    Key: 2
    Decrypted text: Hello World
    English Percentage: 100.0
    
    Args:
        cipher_text (str): Encrypted text

    Returns:
        str: Decrypted cipher message
    """
    percentages = {}
    for key in range(1, 26):
        decrypted_text = encrypt(cipher_text, key)
        threshold = 80
        if de.get_english_count(decrypted_text) > threshold:
            percentages[key] = de.get_english_count(decrypted_text)
    key_list, val_list = list(percentages.keys()), list(percentages.values())
    key_break = key_list[val_list.index(max(percentages.values()))]
    if key_break != -1:
        print("Cipher hacked! :)")
        print("Key: " + str(26 - key_break))
        print("Decrypted text: " + encrypt(cipher_text, key_break))
        print("English Percentage: " + str(percentages[key_break]))
    else:
        print("Failed to hack cipher :(")