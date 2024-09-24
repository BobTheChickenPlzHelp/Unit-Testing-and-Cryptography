# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def vig_encode(text, keyword):
  """
  Encodes text using vigenere cipher.
  :param text: The text to be encoded.
  :param keyword: The key to be used.
  :return: Returns the encoded text.
  """
  new_str = ""
  text = text.upper()
  for i in range(len(text)):
    if text[i] in alpha:
      num = alpha.find(text[i]) + alpha.find(keyword[i % len(keyword)])
      new_str += alpha[num % 27]
    else:
      new_str += text[i]
  return new_str


def vig_decode(text, keyword):
  """
  Decodes text using vigenere cipher.
  :param text: The text to be decoded.
  :param keyword: The key to be used.
  :return: Returns the decoded text.
  """
  new_str = ""
  text = text.upper()
  for i in range(len(text)):
    if text[i] in alpha:
      num = alpha.find(text[i]) - alpha.find(keyword[i % len(keyword)])
      new_str += alpha[num % 27]
    else:
      new_str += text[i]
  return new_str


test = "apple"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!