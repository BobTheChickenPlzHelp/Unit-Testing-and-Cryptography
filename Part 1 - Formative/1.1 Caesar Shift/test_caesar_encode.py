from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class Testcaesar_encode(TestCase):
    def test_caesar_encode_lowercase(self):
        self.assertEqual(caesar_encode("apple", 2), "CRRNG")

    def test_caesar_encode_uppercase(self):
        self.assertEqual(caesar_encode("Apple", 2), "CRRNG")

    def test_caesar_encode_empty_num(self):
        self.assertEqual(caesar_encode("apple", 2), "CRRNG")

    def test_caesar_encode_empty_text(self):
        self.assertEqual(caesar_encode("Apple!", 2), "CRRNG!")

    def test_caesar_encode_whitespace(self):
        self.assertEqual(caesar_encode(" APPLE ", 2), " CRRNG ")

    def test_caesar_encode_sentnce(self):
        self.assertEqual(caesar_encode("Hola comoestas or something like that :)", 5), "MTQF HTRTJXYFX TW XTRJYMNSL QNPJ YMFY :)")