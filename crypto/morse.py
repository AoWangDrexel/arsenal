"""The Morse Code Module.

Attributes:
    morse_dict: dict
        the dictionary version of the morseTable.txt
"""


def load_morse_table():
    """Creates a dictionary of the Morse Code.
    
    Example
    =======
    >>> from cryptsenal.morse import *
    >>> load_morse_table()
    {',': '--..--','.': '.-.-.-','0': '-----',...,'Z': '--..'}
    
    Args:
        None
    
    Returns:
        dict (keys: str, values: str): A Morse Code dictionary. 
    """
    codes = ""
    with open("morseTable.txt", "r") as code:
        codes = code.read()
    codes = codes.split()
    keys = [codes[i] for i in range(0, len(codes), 2)]
    values = [codes[i] for i in range(1, len(codes), 2)]
    morse_dict = {keys[i]:values[i] for i in range(len(keys))}
    return morse_dict


morse_dict = {}
morse_dict = load_morse_table()


def encode(plain_text):
    """Encodes the message in Morse Code.
    
    Example
    =======
    >>> from cryptsenal.morse import *
    >>> encode("How are you today?")
    .... --- .-- | .- .-. . | -.-- --- ..- | - --- -.. .- -.-- ..--..
    
    Args:
        plain_text (str): A plain message.

    Returns:
        str: An encoded plain_text.
    """
    word = ""
    plain_text = plain_text.upper()
    for symbol in plain_text:
        if symbol in morse_dict.keys():
            word += morse_dict[symbol] + " "
        else:
            word += "| "
    return word


def values_by_keys(value):
    """Returns the dictionary key given the value.
    
    Example
    =======
    >>> from cryptsenal.morse import *
    >>> values_by_keys("-...")
    B
    
    Args:
        value (str): A Morse Code.

    Returns:
        str: A key of the Morse Code Dictionary.
    """
    for keys, values in morse_dict.items():
        if value == values:
            return keys
    return -1


def decode(encoded_text):
    """Decodes the encoded message.
    
    Example
    =======
    >>>from cryptsenal.morse import *
    >>> decode(".... --- .-- | .- .-. . | -.-- --- ..- | - --- -.. .- -.-- ..--.. ")
    HOW ARE YOU TODAY? 
    
    Args:
        encoded_text (str): A encoded Morse Code text.

    Returns:
        str: A decoded Morse code text.
    """
    decoded = ""
    encoded_text = encoded_text.split(" ")
    for code in encoded_text:
        decoded += str(values_by_keys(code))
    return decoded.replace("-1", " ")