from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class Testcaesar_encode(TestCase):
    def test_caesar_encode_lowercase(self):
        self.assertEqual(sub_encode("apple", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "WZZTX")

    def test_caesar_encode_uppercase(self):
        self.assertEqual(sub_encode("Apple", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "WZZTX")

    def test_caesar_encode_empty_num(self):
        self.assertEqual(sub_encode("apple", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "WZZTX")

    def test_caesar_encode_empty_text(self):
        self.assertEqual(sub_encode("Apple!", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "WZZTX!")

    def test_caesar_encode_whitespace(self):
        self.assertEqual(sub_encode(" APPLE ", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), " WZZTX ")

    def test_caesar_encode_sentnce(self):
        self.assertEqual(sub_encode("Hola comoestas or something like that :)", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MHTW KHPHXNCWN HO NHPXCMILB TIDX CMWC :)")