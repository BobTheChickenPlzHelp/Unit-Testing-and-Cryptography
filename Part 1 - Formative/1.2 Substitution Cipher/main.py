# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    """
    Encodes text using a substitution cipher.
    :param text: The text to be encoded.
    :param codebet: The encoded alphabet.
    :return: Returns the encoded text.
    """
    new_str = ""
    text = text.upper()
    for let in text:
        if let in alpha:
            index = alpha.index(let)
            new_str += cipher_alphabet[(index) % 26]
        else:
            new_str += let
    return new_str


def sub_decode(text, codebet):
    """
    Decodes text using a substitution cipher.
    :param text: The text to be decoded.
    :param codebet: The decoded alphabet.
    :return: Returns the decoded text.
    """
    new_str = ""
    for let in text:
        if let in alpha:
            index = cipher_alphabet.index(let)
            new_str += alpha[(index) % 26]
        else:
            new_str += let
    return new_str


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
