"""
This module converts strings of text and numerical values from widely used number systems: decimal, binary, octal, and hexadecimal.

Example:
    $ python number_system.py

    import number_system as ns
    print(ns.convert_dec_to_bin(10))
    > 1010

Methods:
    convert_dec_to_bin(decimal)
        Returns the decimal number into binary
    convert_bin_to_dec(binary)
        Returns the binary number into decimal
    convert_dec_to_oct(decimal)
        Return the decimal number into octal
    convert_oct_to_dec(octal)
        Returns the octal number into decimal
    convert_dec_to_hex(decimal)
        Returns the decimal number into hexadecimal
    convert_hex_to_dec(hexadecimal)
        Returns the hexadecimal number into decimal
    convert_text_to_bin(text)
        Returns the converted text into a string of binary
    convert_text_to_oct(text)
        Returns the converted text into a string of octal
    convert_text_to_hex(text)
        Returns the converted text into a string of hexadecimal
    convert_bin_to_text(binary)
        Returns the string of binary into ASCII text
    convert_oct_to_text(octal)
        Returns the string of octal into ASCII text
    convert_hex_to_text(hexadecimal)
        Returns the string of hexadecimal into ASCII text
"""


def convert_dec_to_bin(decimal):
    """The function converts the decimal number into binary and returns the value.

    Args:
        decimal (int): decimal number

    Returns:
        str: The binary value of the decimal number

    Raises:
        ValueError
            If the decimal number is passed as an invalid literal for int().
        TypeError
            If no decimal number is passed in as an argument.
    """
    return bin(int(decimal)).replace("0b", "")


def convert_bin_to_dec(binary):
    """The function converts the binary number into decimal and returns the value.
    Args:
        binary (str): binary number

    Returns:
        int: The decimal number of the binary value

    Raises:
        ValueError
            If the binary number is passed as an invalid literal for int().
        TypeError
            If no binary number is passed in as an argument.
    """
    return int(str(binary), 2)


def convert_dec_to_oct(decimal):
    """ The function converts the decimal number into octal and returns the value.
    Args:
        decimal (int): decimal number

    Returns:
        str: The octal value of the decimal number

    Raises:
        ValueError
            If the decimal number is passed as an invalid literal for int().
        TypeError
            If no decimal number is passed in as an argument.
    """
    return oct(int(decimal)).replace("0o", "")


def convert_oct_to_dec(octal):
    """The function converts the octal number into decimal and returns the value.
    Args:
        octal (str): octal number

    Returns:
        int: The decimal number of the octal value

    Raises:
        ValueError
            If the octal number is passed as an invalid literal for int().
        TypeError
            If no octal number is passed in as an argument.
    """
    return int(str(octal), 8)


def convert_dec_to_hex(decimal):
    """The function converts the decimal number into hexadecimal and returns the value.
    Args:
        decimal (int): decimal number

    Returns:
        str: The hexadecimal value of the decimal number

    Raises:
        ValueError
            If the decimal number is passed as an invalid literal for int().
        TypeError
            If no decimal number is passed in as an argument.
    """
    return hex(int(decimal)).replace("0x", "")


def convert_hex_to_dec(hexadecimal):
    """The function converts the hexadecimal number into decimal and returns the value.
    Args:
        hexadecimal (str): hexadecimal value

    Returns:
        int: The decimal number of the hexadecimal value

    Raises:
        ValueError
            If the hexadecimal number is passed as an invalid literal for int().
        TypeError
            If no hexadecimal number is passed in as an argument.
    """
    return int(str(hexadecimal), 16)


def convert_text_to_bin(text):
    """The function goes through every symbol in the text and converts the ASCII value of each symbol
       to binary, then returns it.
    Args:
        text (str): The string of text

    Returns:
        str: The text converted into a string of binary text

    Raises:
        TypeError
            If no text is passed in as an argument.
    """
    binary_msg = ""
    for symbol in str(text):
        binary_msg += convert_dec_to_bin(ord(symbol))
        binary_msg += " "

    return binary_msg


def convert_text_to_oct(text):
    """The function goes through every symbol in the text and converts the ASCII value of each symbol
       to octal, then returns it.
    Args:
        text (str): The string of text

    Returns:
        str: The text converted into a string of octal text

    Raises:
        TypeError
            If no text is passed in as an argument.
    """
    oct_msg = ""
    for symbol in str(text):
        oct_msg += convert_dec_to_oct(ord(symbol))
        oct_msg += " "

    return oct_msg


def convert_text_to_hex(text):
    """The function goes through every symbol in the text and converts the ASCII value of each symbol
       to hexadecimal, then returns it.
    Args:
        text (str): The string of text

    Returns:
        str: The text converted into a string of hexadecimal text

    Raises:
        TypeError
            If no text is passed in as an argument.
    """
    hex_msg = ""
    for symbol in str(text):
        hex_msg += convert_dec_to_hex(ord(symbol))
        hex_msg += " "

    return hex_msg


def convert_bin_to_text(binary):
    """The function splits the binary message into a list by spaces, goes through the list converting
       the binary values into decimal, and turning them back into ASCII symbols, then returning the message.
    Args:
        binary (str): A string of binary text

    Returns:
        str: The binary text converted into ASCII decimal text

    Raises:
        TypeError
            If no binary string is passed in as an argument.
        ValueError
            If the string of binary numbers is passed as an invalid literal for int().
    """
    text = ""
    binary_list = str(binary).split(" ")
    for symbol in binary_list:
        text += chr(convert_bin_to_dec(symbol))
    return text


def convert_oct_to_text(octal):
    """The function splits the octal message into a list by spaces, goes through the list converting
       the octal values into decimal, and turning them back into ASCII symbols, then returning the message.
    Args:
        octal (str): A string of octal text

    Returns:
        str: The octal text converted into ASCII decimal text

    Raises:
        TypeError
            If no octal string is passed in as an argument.
        ValueError
            If the string of octal numbers is passed as an invalid literal for int().
    """
    text = ""
    oct_list = str(octal).split(" ")
    for symbol in oct_list:
        text += chr(convert_oct_to_dec(symbol))
    return text


def convert_hex_to_text(hexadecimal):
    """The function splits the hexadecimal message into a list by spaces, goes through the list converting
       the hexadecimal values into decimal, and turning them back into ASCII symbols, then returning the message.
    Args:
        hexadecimal (str): A string of hexadecimal text

    Returns:
        str: The hexadecimal text converted into ASCII decimal text

    Raises:
        TypeError
            If no hexadecimal string is passed in as an argument.
        ValueError
            If the string of hexadecimal numbers is passed as an invalid literal for int().
    """
    text = ""
    hexa_list = str(hexadecimal).split(" ")
    for symbol in hexa_list:
        text += chr(convert_hex_to_dec(symbol))
    return text
