# Built-in imports
# Part 1
def reverse(text):
    """
    takes a string of text and returns the reversed text

    Parameter
    ---------
    text : str

    Returns
    -------
    text : str
    in the opposite order of the original text
    """
    if len(text) <= 1:
        return text
    elif len(text) > 1:
        return reverse(text[1:]) + text[0]

# Part 2
def is_palindrome(text):
    """
    takes a string of text and returns a boolean value of whether the text is a palindrome

    Parameter
    ---------
    text : str

    Returns
    -------
    boolean
    """
    if len(text) == 2:
        if text[0] == text[len(text)-1]:
            return True
        else:
            return False
    elif len(text) <= 1:
        return True
    elif len(text) > 2:
        if text[0] == text[len(text)-1] and is_palindrome(text[1:len(text)-1]):
            return True
        else:
            return False


