"""The English Dectection Module.

An English detection implementation using two English dictionary text files.

Attributes:
    ENGLISH_WORDS: List
        A list of the English words.
"""


def load_dictionary():
    """Creates a dictionary of English words.
    
    Example
    =======
    >>> from cryptsenal.detect_english import *
    >>> load_dictionary()
    ['aarhus','aaron','ababa','aback','abaft',....]
    
    Args:
        None
    
    Returns:
        List (str): A list of English words.
    """
    with open("words.txt", "r") as f1, open("morewords.txt", "r") as f2:
        file1, file2 = f1.read().split("\n"), f2.read().split("\n")
    file1 = [word.lower() for word in file1]
    file2 = [word.lower() for word in file2]
    file2.extend(file1)
    return file2


ENGLISH_WORDS = load_dictionary()


def remove_non_letters(msg):
    """Removes non-alphabetic symbols, except for whitespace.
    
    Example
    =======
    >>> from cryptsenal.detect_english import *
    >>> remove_non_letters("How are? you? I am good....?")
    How are you I am good
    
    Args:
        msg (str): A string of text.

    Returns:
        str: A cleaned string of text.  
    """
    clean_words = []
    for symbol in msg:
        if symbol.isalpha() or symbol.isspace():
            clean_words.append(symbol)
    return "".join(clean_words)


def get_english_count(msg):
    """The function returns the percentage of words in the dictionary.
    
    Example
    =======
    >>> from cryptsenal.detect_english import *
    >>> get_english_count("How are you? I am good. Also wdffdsifnid Ha!")
    88.88888888888889
    
    Args:
        msg (str): A string of text.
        
    Returns:
        float: A percentage of words in English. 
    """
    msg = remove_non_letters(msg.lower())
    possible_words = msg.split()
    if possible_words == []:
        return 0
    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return 100 * float(matches) / len(possible_words)