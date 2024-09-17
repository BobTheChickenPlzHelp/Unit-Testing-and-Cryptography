from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class Testvig_encode(TestCase):
    def test_Vigenere_encode_lowercase(self):
        self.assertEqual(vig_encode("apple", "test"), "TTGDX")

    def test_Vigenere_encode_uppercase(self):
        self.assertEqual(vig_encode("Apple", "test"), "TTGDX")

    def test_Vigenere_encode_empty_num(self):
        self.assertEqual(vig_encode("apple", "test"), "TTGDX")

    def test_Vigenere_encode_empty_text(self):
        self.assertEqual(vig_encode("Apple!", "test"), "TTGDX!")

    def test_Vigenere_encode__whitespace(self):
        self.assertEqual(vig_encode(" APPLE ", "test"), " TTGDX ")

    def test_Vigenere_encode_sentnce(self):
        self.assertEqual(vig_encode("Hola comoestas or something like that :)", "test"), " SCTSGFEGIJLTWRGJDJGEIK ARYSDMBXSXZTLD:)")