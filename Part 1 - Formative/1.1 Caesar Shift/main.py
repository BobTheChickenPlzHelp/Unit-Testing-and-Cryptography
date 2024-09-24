# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    """
    Encodes text to be encrypted using Caesar Cipher.
    :param text: The text to be encrypted.
    :param n: The amount the text is shifted.
    :return: Returns the encrypted text.
    """
    new_str = ""
    text = text.upper()
    for let in text:
        if let in alpha:
            index = alpha.index(let) #finds the index of the letter in alpha
            new_str += alpha[(index + n) % 26] #adds the number into new_str
        else:
            new_str += let
    return new_str


def caesar_decode(text, n):
    """
    Decodes text to be decrypted using Caesar Cipher.
    :param text: The text to be decrypted.
    :param n: The amount the text was shifted.
    :return: Returns the decrypted text.
    """
    new_str = ""
    for let in text:
        if let in alpha:
            index = alpha.index(let)
            new_str += alpha[(index - n) % 26]
        else:
            new_str += let
    return new_str


test = "HELLOWORLD!"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
