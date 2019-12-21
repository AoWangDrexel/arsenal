"""The Number System Module.

Converts strings of text to widely used number systems: decimal, binary, octal, and hexadecimal.
"""


def convert_text_to_bin(text):
    """Returns a string of ASCII symbols into a binary string.

    Example
    =======
    >>> from cryptsenal.number_system import *
    >>> convert_text_to_bin("How are you?")
    1001000 1101111 1110111 100000 1100001 1110010 1100101 100000 1111001 1101111 1110101 111111

    Args:
        text (str): A string of ASCII symbols.

    Returns:
        str: A binary string.
    """
    binary_string = "".join([(bin(ord(symbol)).replace("0b", "") + " ") for symbol in str(text)])
    return binary_string[:len(binary_string) - 1]


def convert_text_to_oct(text):
    """Returns a string of ASCII symbols into an octal string.

    Example
    =======
    >>> from cryptsenal.number_system import *
    >>> convert_text_to_oct("How are you?")
    110 157 167 40 141 162 145 40 171 157 165 77

    Args:
        text (str): A string of ASCII symbols.

    Returns:
        str: An octal string.
    """
    oct_string = "".join([oct(ord(symbol)).replace("0o", "") + " " for symbol in str(text)])
    return oct_string[:len(oct_string) - 1]


def convert_text_to_hex(text):
    """Returns a string of ASCII symbols into a hexidecimal string.

    Example
    =======
    >>> from cryptsenal.number_system import *
    >>> convert_text_to_hex("How are you?")
    48 6f 77 20 61 72 65 20 79 6f 75 3f

    Args:
        text (str): A string of ASCII symbols.

    Returns:
        str: A hexidecimal string.
    """
    hex_string = "".join([hex(ord(symbol)).replace("0x", "") + " " for symbol in str(text)])
    return hex_string[:len(hex_string) - 1]


def convert_bin_to_text(binary):
    """Returns a binary string into a string of ASCII symbols.

    Example
    =======
    >>> from cryptsenal.number_system import *
    >>> convert_bin_to_text("1001000 1101111 1110111 100000 1100001 1110010 1100101 100000 1111001 1101111 1110101 111111")
    How are you?

    Args:
        binary (str): A binary string.

    Returns:
        str: A string of ASCII symbols.
    """
    return "".join([chr(int(symbol, 2)) for symbol in str(binary).split(" ")])


def convert_oct_to_text(octal):
    """Returns an octal string into a string of ASCII symbols.

    Example
    =======
    >>> from cryptsenal.number_system import *
    >>> convert_oct_to_text("110 157 167 40 141 162 145 40 171 157 165 77")
    How are you?

    Args:
        octal (str): An octal string.

    Returns:
        str: A string of ASCII symbols.
    """
    return "".join([chr(int(symbol, 8)) for symbol in str(octal).split(" ")])


def convert_hex_to_text(hexadecimal):
    """Returns a hexidecial string into a string of ASCII symbols.

    Example
    =======
    >>> from cryptsenal.number_system import *
    >>> convert_hex_to_text("48 6f 77 20 61 72 65 20 79 6f 75 3f")
    How are you?

    Args:
        hexadecimal (str): A hexideciaml string.

    Returns:
        str: A string of ASCII symbols.
    """
    return "".join([chr(int(symbol, 16)) for symbol in str(hexadecimal).split(" ")])